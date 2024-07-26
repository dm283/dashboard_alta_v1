import sys, os, json, dash_bootstrap_components as dbc, pandas as pd
from dash import Dash, dcc, html, Input, Output, State, ALL
from datetime import datetime

import functions_library as dfl, content_create_functions as ccf
from widgets.common_widgets import common_widgets
from widgets.user_widgets import database_select, dashboard_header

from flask import Flask

import warnings
warnings.filterwarnings('ignore')

DEBUG, HOST, PORT = dfl.DEBUG, dfl.HOST, dfl.PORT
print(DEBUG, HOST, PORT)


#  Импортирование элементов дашборда
# select = database_select.select # sql-запрос к базе данных
# column_names = database_select.column_names # наименования полей pandas-датафрейма

select_query = database_select.select_query
select_columns = database_select.select_columns
select_filter = database_select.select_filter


DATA_UPDATE_PERIOD = common_widgets.DATA_UPDATE_PERIOD  # период обновления данных
header = dashboard_header.header    # шапка дашборда
# filters_area = ccf.create_filters_area()    # Формирование области фильтров данных
widget_update, widget_update_data_type, output_list, widget_list, widget_select_index, \
    table_сolumns_displayed = ccf.create_widget_dictionary()[2:8]  #  Импортирование callback-функций

try:
    #  при отсутствии файла с пользователями вход без страницы аутентификации
    with open('users/users_list.json', 'r') as jsonfile:
        USERS_LIST = json.load(jsonfile)  # type = dict
    ENTER_VIA_AUTH_PAGE = True    #  Флаг входа через страницу аутентификации
    USER = str()
except FileNotFoundError:
    USER = 'user1'
    ENTER_VIA_AUTH_PAGE = False

if not os.path.exists('logs'):
    os.mkdir('logs')

#  Глобальные переменные и константы
BNT_SAVE_TABLE_DATA = 0 # хранение кол-ва кликов на кнопке сохранения данных таблицы
ax_msg, ay_msg = [], []  # массивы хранения кол-ва пользователей для виджета scatter

#  Подключение к базе данных
conn = dfl.get_db_connect()

#  Создание dash-приложения
server = Flask(__name__)
app = Dash(server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])
# app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = f'{dfl.COMPANY_NAME} | Dashboard | Витрина Таможенного склада' 


# *************************** LAYOUT *********************************************************
app.layout = html.Div([
                dcc.Location(id='url', refresh=False),
                html.Div(id='page_content')
                ])

# *************************** CALLBACKS ******************************************************
@app.callback(
        Output('page_content', 'children'),
        Input('url', 'pathname')
        )
def display_page(pathname):
    #  Роутинг страниц
    if (not ENTER_VIA_AUTH_PAGE and pathname == '/') or pathname == '/dashboard_page':
        #  СТРАНИЦА ДАШБОРДА
        widgets_area = ccf.create_widgets_area(USER)
        dashboard_page = html.Div([
            #  ОБЛАСТЬ ШАПКИ ДАШБОРДА
            html.Header( header, className='header' ),
            #  ОБЛАСТЬ ФИЛЬТРОВ
            # dbc.Row( filters_area, className='filters_area' ),
            #  ОБЛАСТЬ ВИДЖЕТОВ С ДАННЫМИ (ОСНОВНОЙ КОНТЕНТ ДАШБОРДА)
            dbc.Row([ 
                dbc.Col( widgets_area, style={'backgroundColor': 'GhostWhite', 'padding': '0'}, width=12),
                dcc.Interval( id='interval_component', n_intervals=0)   #  Компонент для периодического обновления данных
                ], style={'margin': '2px'})
            ])

        return dashboard_page
    
    elif ENTER_VIA_AUTH_PAGE and pathname == '/':
        #  СТРАНИЦА ВХОДА
        sign_in_page = html.Div([
            dbc.Label('Логин', className='auth_form_label'), dbc.Input(id='user_input', type='text', className='auth_form_input'),
            dbc.Label('Пароль', className='auth_form_label'), dbc.Input(id='password_input', type='password', className='auth_form_input'),
            html.Button('Вход', id='btn_sign_in', n_clicks=0, className='auth_form_btn'),
            html.Div(id='sign_in_page_output', className='auth_form_output')
        ], className='auth_form')

        return sign_in_page
    

@app.callback(
    Output('sign_in_page_output', 'children'),
    Input('btn_sign_in', 'n_clicks'),
    State('user_input', 'value'), State('password_input', 'value')
    )
def update_output(n_clicks, user_input, password_input):
    #  Валидация логин/пароль
    global USER
    
    if not user_input and not password_input:
        return ''
    if user_input in USERS_LIST and USERS_LIST[user_input] == password_input:
        USER = user_input
        return dcc.Link('Зайти в дашборд', href='/dashboard_page')
    else:
        return 'Некорректный логин или пароль.'


@app.callback(
    output_list,
    Output('interval_component', 'interval'),
    Output('update_date', 'children'),

    Output('table_cnt_records_account_book', 'children'), ########## кол-во строк в таблице
    Output('table_cnt_records_products_on_storage', 'children'), ########## кол-во строк в таблице
    Output('table_cnt_records_report_vehicle', 'children'), ########## кол-во строк в таблице

    Input({'type': 'filter_dropdown', 'index': ALL}, 'value'),  #  список значений всех фильтров
    Input({'type': 'filter_date', 'index': ALL}, 'start_date'), 
    Input({'type': 'filter_date', 'index': ALL}, 'end_date'), 
    # Input('interval_component', 'n_intervals'),
    Input('btn_update_data', 'n_clicks')
)
def update_data(filter_values_list, filter_start_date_list, filter_end_date_list, n_update_btn):
# def update_data(filter_values_list, filter_start_date_list, filter_end_date_list, n, n_update_btn):
    #  Обновляет все виджеты дашбода
    global ax_msg, ay_msg

    n = 0  #  заглушка для interval_component, автоматическое обновление отключено пока, т.к. глючит

    for i in range(len(filter_start_date_list)):
        dates_tuple = (filter_start_date_list[i], filter_end_date_list[i])
        filter_values_list.append(dates_tuple)

    #  Загрузка датафрейма
    #  df = dfl.get_db_data_to_datafame(conn, select, column_names); df['cnt'] = 1

    df = {}
    for s in select_query.keys():
        # df[s] = dfl.get_db_data_to_datafame(conn, select_query[s], select_columns[s])

        select = select_query[s]

        ############ !!! эту часть сделать универсальной или перенести в виджеты !!! #######################
        if select_filter[s]:

            if s in ['received_product_quantity', 'received_dt_quantity', 'received_tnved_quantity', ]:
                filter_str_0, filter_str_1 = '', ''
                if filter_values_list[0][0]:
                    filter_str_0 = select_filter[s][0]
                    filter_date = filter_values_list[0][0].replace('-', '') #########
                    filter_str_0 = filter_str_0.replace('dashboard_filter_0_0', filter_date)
                if filter_values_list[0][1]:
                    filter_str_1 = select_filter[s][1]
                    filter_date = filter_values_list[0][1].replace('-', '') #########
                    filter_str_1 = filter_str_1.replace('dashboard_filter_0_1', filter_date)
                filter_str_whole = filter_str_0 + filter_str_1
                select = select.replace('dashboard_filter_string', filter_str_whole)
                
            elif s in ['account_book']:
                filter_str_0, filter_str_1 = '', ''
                if filter_values_list[1][0]:
                    filter_str_0 = select_filter[s][0]
                    filter_date = filter_values_list[1][0].replace('-', '') #########
                    filter_str_0 = filter_str_0.replace('dashboard_filter_1_0', filter_date)
                if filter_values_list[1][1]:
                    filter_str_1 = select_filter[s][1]
                    filter_date = filter_values_list[1][1].replace('-', '') #########
                    filter_str_1 = filter_str_1.replace('dashboard_filter_1_1', filter_date)
                filter_str_whole = filter_str_0 + filter_str_1
                select = select.replace('dashboard_filter_string', filter_str_whole)           

            elif s in ['report_vehicle']:
                filter_str_0, filter_str_1 = '', ''
                if filter_values_list[2][0]:
                    filter_str_0 = select_filter[s][0]
                    filter_date = filter_values_list[2][0].replace('-', '') #########
                    filter_str_0 = filter_str_0.replace('dashboard_filter_2_0', filter_date)
                if filter_values_list[2][1]:
                    filter_str_1 = select_filter[s][1]
                    filter_date = filter_values_list[2][1].replace('-', '') #########
                    filter_str_1 = filter_str_1.replace('dashboard_filter_2_1', filter_date)
                filter_str_whole = filter_str_0 + filter_str_1
                select = select.replace('dashboard_filter_string', filter_str_whole)                    
            else:
                select = select.replace('dashboard_filter_string', '')
            ###############################################################################

        df[s] = dfl.get_db_data_to_datafame(conn, select)
        df[s]['system_cnt'] = 1

    update_date = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    #  Динамическое формирование набора функций обновлений виджетов
    return_functions, table_cnt_records = [], []
    for w in widget_list:
        widget_key = w.replace('widget_', '')
        if widget_key == 'graph_scatter_cnt_users':
            res = widget_update[widget_key]( df[widget_select_index[widget_key]], filter_values_list, ax_msg, ay_msg, n ) 
            return_functions.append(res)
        else:
            res = widget_update[widget_key]( df[widget_select_index[widget_key]], filter_values_list, n ) 
            return_functions.append(res)

            if 'table_record_details_' in widget_key:
                # расчет кол-ва строк в таблице
                table_cnt_records.append(len(res))

    return return_functions + [ DATA_UPDATE_PERIOD * 1000 ] + [ update_date ] + table_cnt_records



@app.callback(
    Output('settings_modal_window', 'is_open'),
    [Input('btn_settings', 'n_clicks'), Input('btn_settings_close', 'n_clicks')],
    State('settings_modal_window', 'is_open'),
    Input('btn_settings_apply', 'n_clicks'),
    State('input_period', 'value')
)
def toggle_modal(n1, n2, is_open, n, period_value):
    #  Открывает/закрывает модальное окно с настройками
    global DATA_UPDATE_PERIOD

    if n:
        try:
            DATA_UPDATE_PERIOD = int(period_value)
        except:
            print('Недопустимое значение')

    if n1 or n2:
        return not is_open
    
    return is_open


@app.callback(
    Output("offcanvas_filters", "is_open"),
    Input("btn_show_filters", "n_clicks"),
    [State("offcanvas_filters", "is_open")],
)
def toggle_offcanvas_filters(n1, is_open):
    #  Открывает/закрывает область фильтров
    if n1:
        return not is_open
    return is_open


#  Набор функций для каждого соответствующего виджета (таблицы)
#  Здесь прописываем все алиасы таблиц, в которых использована функция create_table
for i in ['_products_on_storage', '_account_book', '_report_vehicle']:
    @app.callback(Output(f'modal_table_record{i}', 'is_open'), Output(f'modal_table_record_content{i}', 'children'),
        Output(f'table_record_details{i}', 'active_cell'), Output(f'btn_modal_table_record_close{i}', 'n_clicks'), 
        Input(f'table_record_details{i}', 'active_cell'), State(f'table_record_details{i}', 'data'), 
        Input(f'btn_modal_table_record_close{i}', 'n_clicks'), State(f'modal_table_record{i}', 'is_open'),
        State(f'table_record_details{i}', 'id')
        )
    def toggle_modal_table_records(active_cell, data, n_close, is_open, table_id):
        #  Открывает/закрывает модальное окно с данными из таблицы
        if active_cell:
            # row_number = int(active_cell['row_id']); content = []
            row_number = active_cell['row_id']; content = []  #########
            for r in data:
                if r['id'] == row_number:
                    record = r; break
            # for k in record.keys():
            for k in table_сolumns_displayed[table_id]:
                key = table_сolumns_displayed[table_id][k]
                value = record[k] if record[k] else 'None'
                row = dbc.Row([dbc.Col(dbc.Label(key), width=4), dbc.Col(dbc.Label(value), width=8),], 
                              style={'marginBottom': '5px'})
                content.append(row)
        if n_close:
            return False, content, None, 0
        return True, content, active_cell, 0

    
    @app.callback(
        Output(f'modal_save_table_data{i}', 'is_open'), 
        Output(f'btn_modal_save_table_data_close{i}', 'n_clicks'),
        Input(f'btn_open_modal_save_table_data{i}', 'n_clicks'), 
        Input(f'btn_modal_save_table_data_close{i}', 'n_clicks'),
    )
    def toggle_modal_save_table_data(n_open, n_close):
        #  Открывает/закрывает модальное окно сохранения данных таблицы
        if not n_open or n_close:
            return False, 0
        return True, 0
    
    @app.callback(
        Output(f"download_dataframe_xlsx{i}", "data"),
        Input(f"btn_modal_save_table_data_save{i}", "n_clicks"),
        State(f'table_record_details{i}', 'data'),
        State(f'input_file_name{i}', 'value'),
        State(f'table_record_details{i}', 'id'),
        prevent_initial_call=True,
    )
    def download_table_data(n_clicks, data, file_name, table_id):
        #  Сохраняет в браузере файл с данными таблицы
        if n_clicks and file_name:
            columns_mapping_dict = table_сolumns_displayed[table_id]
            df_data = pd.DataFrame(data)
            df_data = df_data.rename(columns=columns_mapping_dict)
            file_name += '.xlsx'
            return dcc.send_data_frame(df_data.to_excel, file_name)


app.run_server(debug=DEBUG, host=HOST, port=PORT) 
