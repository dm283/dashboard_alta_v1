import plotly.express as px, dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, State, dash_table, ALL


id = 'table_telegram_chats_types'

#  Виджет "Таблица"
widget = [ 
            html.H6([     
                html.Span('Telegram-чаты', ),  #style={'marginLeft': '110px'}
                ], style={'color': 'white', 'backgroundColor': 'None', 'marginBottom': '5px', 'textAlign': 'center'}), 
            dash_table.DataTable(
                columns=[{"name": i, "id": i} for i in ['entity_type', 'chat_cnt']],
                style_cell = {'font_size': '10px', 'textAlign': 'center'},
                page_action='none',
                #style_table={'height': '657px', 'overflowY': 'auto'},
                style_header={'backgroundColor': 'Black', 'color': 'white'},
                style_data={'backgroundColor': 'DarkSlateGray', 'color': 'white'},
                id=id
                ),
        ]

widget_update_data_type = 'data'
widget_select_index = 'count_telegram_chats_types'


def widget_update(df, filter_values_list, n):
    #  Функция обновления данных таблицы
    
    # devices = ['desktop', 'mobile']
    # countries = ['India', 'Russia', 'England', 'US', 'Japan', 'China', 'Australia', 'Canada']

    # filter_device = devices if filter_values_list[0] == None else [filter_values_list[0]]
    # filter_country = countries if filter_values_list[1] == None else [filter_values_list[1]]
    # filter_web_service = [filter_values_list[2]] 

    df_table = df
    data = df_table[['entity_type', 'chat_cnt']].to_dict('records')
    
    return data
