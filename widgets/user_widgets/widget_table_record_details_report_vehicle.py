import plotly.express as px, dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, State, dash_table, ALL
from widget_templates.table_template import create_table

#  заполняем эти данные =================================================================================================
#     сolumns_displayed - отображаемые в таблице столбцы / columns_all - все загруженные столбцы (отображаются в окне записи)
#     исходный select при этом может иметь больше столбцов!
id = 'table_record_details_report_vehicle'  
table_alias = 'report_vehicle'
table_name = 'Отчет по ТС'
widget_select_index = 'report_vehicle'                 # id соответствующего select из database_select.py
# columns_all = ['id', 'id_0', 'key_id', 'g32', 'gtdnum', 'date_in', 'g31', 'g31_3',
#        'g31_3a', 'g33_in', 'g35', 'gtdregime_in', 'date_chk', 'place',
#        'exp_date', 'g41a_dt', 'code', 'date_out', 'doc_num_out',
#        'gtdregime_out', 'g35_out', 'g31_3_out', 'g31_3a_out', 'g31_out',
#        'g32_out', 'g33_out', 'g31_3ost', 'g35ost', 'g35ost_', 'g31_3ost_',]
сolumns_displayed = {
    'id':'№ п/п', 'gtdnum':'Номер ДТ', 'g32':'№ тов.', 'g33_in':'Код ТНВЭД', 'g31':'Наименование товара', 'g35':'Вес брутто',
    'g31_3':'Кол.доп.ед', 'g31_3a':'Ед.изм.', 'date_in':'Дата приема', 'place':'Скл.номер', 'date_chk':'Дата ок.хр.', 
       'exp_date':'Срок годности', 'gtdregime_out':'Режим выдачи', 'doc_num_out':'№ ДТ выдачи', 'g33_out':'Код ТНВЭД выдачи',
    'g35_out':'Выдача брутто', 'g31_3_out':'Выд.доп.ед', 'date_out':'Дата выдачи', 
    'g35ost_':'Остаток брутто', 'g31_3ost_':'Остаток Доп.ед',
}
columns_all = list(сolumns_displayed.keys())

pagination = True

def widget_update(df, filter_values_list, n):
    #  Функция обновления данных таблицы
    df_table = df

    # костыль т.к. в селекте непонятно где поле id
    # df_table = df_table.rename(columns={"id": "id_0", "nn": "id"})

    #  добавляем необходимые фильтры данных
    # if filter_values_list[0]:
    #     df_table = df_table[ df_table['device'].isin([filter_values_list[0]]) ]
    # if filter_values_list[1]:
    #     df_table = df_table[ df_table['country'].isin([filter_values_list[1]]) ]
    # if filter_values_list[2]:
    #     df_table = df_table[ df_table['web_service'].isin([filter_values_list[2]]) ]
    
    data = df_table[columns_all].to_dict('records')
    return data



#  эти данные и код не меняем ===========================================================================================
widget_update_data_type = 'data'         # тип данных для output - для таблицы всегда data
widget = create_table(
    table_id=id,
    table_alias=table_alias,
    table_name=table_name, 
    pagination=pagination, 
    сolumns_displayed=сolumns_displayed,
    header_margin_left=700
)




# # сolumns_displayed - отображаемые в таблице столбцы / columns_all - все загруженные столбцы (отображаются в окне записи)
# # исходный select при этом может иметь больше столбцов!

# id = 'table_record_details'
# table_name = 'Детализация данных о пользователях онлайн'
# widget_update_data_type = 'data'               # тип данных для output - для таблицы всегда data
# widget_select_index = 'web_service_usage'      # id соответствующего select из database_select.py
# сolumns_displayed = ['user_id', 'device', 'country', 'sign_date']
# columns_all = ['id', 'web_service', 'user_id', 'device', 'country', 'user_status', 'sign_date', 'signout_date']
# pagination = False

# #  Модальное окно с расширенными данными о записи
# modal_table_record = dbc.Modal(
#                 [
#                     dbc.ModalHeader(dbc.ModalTitle(table_name, style={'fontSize': '20px'})),
#                     dbc.ModalBody(id='modal_table_record_content'),
#                     dbc.ModalFooter(html.Div([
#                         dbc.Button("Закрыть", id='btn_modal_table_record_close', n_clicks=0,
#                             style={'width': '120px'}, color="warning" )
#                         ]))
#                 ],
#                 id='modal_table_record',
#                 is_open=False
#             )

# #  Модальное окно сохранения данных таблицы
# modal_save_table_data = dbc.Modal(
#                 [
#                     dbc.ModalHeader(dbc.ModalTitle("Сохранение данных таблицы")),
#                     dbc.ModalBody([
#                         dbc.Row([
#                             dbc.Col(dbc.Label("Наименование файла"), width=7),
#                             dbc.Col(dbc.Input(id='input_file_name', type='text'))
#                         ], style={'marginBottom': '5px'}),
#                     ]),
#                     dbc.ModalFooter(html.Div([
#                         dbc.Button("Сохранить", id='btn_modal_save_table_data_save', n_clicks=0,
#                             style={'width': '120px', 'marginRight': '10px'}, color="success"), 
#                         dcc.Download(id="download_dataframe_xlsx"), 
#                         dbc.Button("Закрыть", id='btn_modal_save_table_data_close', n_clicks=0,
#                             style={'width': '120px'}, color="warning" )
#                         ]))
#                 ],
#                 id='modal_save_table_data',
#                 is_open=False
#             )


# if pagination:
#     table_height = '676px'
#     table_page_action = 'native'
# else:
#     table_height = '720px'
#     table_page_action = 'none'


# #  Виджет "Таблица"
# widget = [ modal_table_record,
#            modal_save_table_data,
#             html.H6([     
#                 html.Span(html.Img(src='assets/baseline_save_white.png', id='btn_open_modal_save_table_data', n_clicks=0,), 
#                           className='icon_save_table_data'),
#                 html.Span(table_name, style={'marginLeft': '110px'}),
#                 ], style={'color': 'white', 'backgroundColor': 'None', 'marginBottom': '2px', 'textAlign': 'left'}), 
#             dash_table.DataTable(
#                 id=id,
#                 columns=[{"name": i, "id": i} for i in сolumns_displayed],
#                 style_cell = {'font_size': '10px', 'textAlign': 'center'},
#                 style_table={'height': table_height, 'overflowY': 'auto'},
#                 style_header={'backgroundColor': 'Black', 'color': 'white'},
#                 style_data={'backgroundColor': 'DarkSlateGray', 'color': 'white'},
#                 page_action=table_page_action, page_current=0, page_size=21,
#                 ),
#         ]


# def widget_update(df, filter_values_list, n):
#     #  Функция обновления данных таблицы

#     df_table = df

#     #  добавляем необходимые фильтры данных
#     if filter_values_list[0]:
#         df_table = df_table[ df_table['device'].isin([filter_values_list[0]]) ]
#     if filter_values_list[1]:
#         df_table = df_table[ df_table['country'].isin([filter_values_list[1]]) ]
#     if filter_values_list[2]:
#         df_table = df_table[ df_table['web_service'].isin([filter_values_list[2]]) ]

#     data = df_table[columns_all].to_dict('records')


#     # devices = ['desktop', 'mobile']
#     # countries = ['India', 'Russia', 'England', 'US', 'Japan', 'China', 'Australia', 'Canada']

#     # filter_device = devices if filter_values_list[0] == None else [filter_values_list[0]]
#     # filter_country = countries if filter_values_list[1] == None else [filter_values_list[1]]
#     # filter_web_service = [filter_values_list[2]] 

#     # df_table = df[
#     #     (df['web_service'].isin(filter_web_service)) &
#     #     (df['device'].isin(filter_device)) & 
#     #     (df['country'].isin(filter_country))
#     #     ]
#     # data = df_table[columns_all].to_dict('records')
    
#     return data
