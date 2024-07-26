import plotly.express as px, dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, State, dash_table, ALL
from widget_templates.table_template import create_table

#  заполняем эти данные =================================================================================================
#     сolumns_displayed - отображаемые в таблице столбцы / columns_all - все загруженные столбцы (отображаются в окне записи)
#     исходный select при этом может иметь больше столбцов!
id = 'table_record_details_3'
table_alias = '3'
table_name = 'Детализация данных о пользователях онлайн'
widget_select_index = 'web_service_usage'                 # id соответствующего select из database_select.py
сolumns_displayed = ['user_id', 'device', 'country', 'sign_date']
columns_all = ['id', 'web_service', 'user_id', 'device', 'country', 'user_status', 'sign_date', 'signout_date']
pagination = False

def widget_update(df, filter_values_list, n):
    #  Функция обновления данных таблицы
    df_table = df
    
    #  добавляем необходимые фильтры данных
    if filter_values_list[0]:
        df_table = df_table[ df_table['device'].isin([filter_values_list[0]]) ]
    if filter_values_list[1]:
        df_table = df_table[ df_table['country'].isin([filter_values_list[1]]) ]
    if filter_values_list[2]:
        df_table = df_table[ df_table['web_service'].isin([filter_values_list[2]]) ]

    data = df_table[columns_all].to_dict('records')
    return data



#  эти данные и код не меняем ===========================================================================================
widget_update_data_type = 'data'         # тип данных для output - для таблицы всегда data
widget = create_table(
    table_id=id,
    table_alias=table_alias,
    table_name=table_name, 
    pagination=pagination, 
    сolumns_displayed=сolumns_displayed
)












# # сolumns_displayed - отображаемые в таблице столбцы / columns_all - все загруженные столбцы (отображаются в окне записи)
# # исходный select при этом может иметь больше столбцов!

# id = 'table_record_details_3'
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
#                     dbc.ModalBody(id='modal_table_record_content_3'),
#                     dbc.ModalFooter(html.Div([
#                         dbc.Button("Закрыть", id='btn_modal_table_record_close_3', n_clicks=0,
#                             style={'width': '120px'}, color="warning" )
#                         ]))
#                 ],
#                 id='modal_table_record_3',
#                 is_open=False
#             )

# #  Модальное окно сохранения данных таблицы
# modal_save_table_data = dbc.Modal(
#                 [
#                     dbc.ModalHeader(dbc.ModalTitle("Сохранение данных таблицы")),
#                     dbc.ModalBody([
#                         dbc.Row([
#                             dbc.Col(dbc.Label("Наименование файла"), width=7),
#                             dbc.Col(dbc.Input(id='input_file_name_3', type='text'))
#                         ], style={'marginBottom': '5px'}),
#                     ]),
#                     dbc.ModalFooter(html.Div([
#                         dbc.Button("Сохранить", id='btn_modal_save_table_data_save_3', n_clicks=0,
#                             style={'width': '120px', 'marginRight': '10px'}, color="success"), 
#                         dcc.Download(id="download_dataframe_xlsx_3"),
#                         dbc.Button("Закрыть", id='btn_modal_save_table_data_close_3', n_clicks=0,
#                             style={'width': '120px'}, color="warning" )
#                         ]))
#                 ],
#                 id='modal_save_table_data_3',
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
#                 html.Span(html.Img(src='assets/baseline_save_white.png', id='btn_open_modal_save_table_data_3', n_clicks=0,), 
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
#     # data = df_table[[columns_all]].to_dict('records')
    
#     return data
