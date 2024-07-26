import plotly.express as px, dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, State, dash_table, ALL


id = 'table_messages_email'

#  Виджет "Таблица"
widget = [ 
            html.H6([     
                html.Span('E-mail сообщения', ),  #style={'marginLeft': '110px'}
                ], style={'color': 'white', 'backgroundColor': 'None', 'marginBottom': '5px', 'textAlign': 'center'}), 
            dash_table.DataTable(
                columns=[{"name": i, "id": i} for i in ['id', 'adrto', 'subj', 'textemail', 'attachmentfiles', 'datep', 'dates']],
                style_cell = {'font_size': '10px', 'textAlign': 'center'},
                #page_action='none',
                style_table={'height': '361px', 'overflowY': 'auto'},
                style_header={'backgroundColor': 'Black', 'color': 'white'},
                style_data={'backgroundColor': 'DarkSlateGray', 'color': 'white'},
                id=id,
                #filter_action='native',
                page_action="native",
                page_current= 0,
                page_size= 11,
                ),
        ]

widget_update_data_type = 'data'
widget_select_index = 'messages_email'


def widget_update(df, filter_values_list, n):
    #  Функция обновления данных таблицы
    
    # devices = ['desktop', 'mobile']
    # countries = ['India', 'Russia', 'England', 'US', 'Japan', 'China', 'Australia', 'Canada']

    # filter_device = devices if filter_values_list[0] == None else [filter_values_list[0]]
    # filter_country = countries if filter_values_list[1] == None else [filter_values_list[1]]
    # filter_web_service = [filter_values_list[2]] 

    df_table = df
    data = df_table[['id', 'adrto', 'subj', 'textemail', 'attachmentfiles', 'datep', 'dates']].to_dict('records')
    
    return data
