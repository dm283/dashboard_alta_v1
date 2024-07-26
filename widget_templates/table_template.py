#  Функция с шаблоном основной таблицы
#  *** Этот код и данные не меняем ! ***

import plotly.express as px, dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, State, dash_table, ALL

def create_table(table_id, table_alias, table_name, pagination, сolumns_displayed, header_margin_left):
    #  Создает виджет таблицы и модальных окон просмотра записи и сохранения данных

    #  Модальное окно с расширенными данными о записи
    modal_table_record = dbc.Modal(
                    [
                        dbc.ModalHeader(dbc.ModalTitle(table_name, style={'fontSize': '20px', 'color': 'darkblue'})),
                        dbc.ModalBody(id='modal_table_record_content_'+table_alias, style={'fontSize': '13px',}),
                        dbc.ModalFooter(html.Div([
                            dbc.Button("Закрыть", id='btn_modal_table_record_close_'+table_alias, n_clicks=0,
                                style={'width': '120px'}, color="warning" )
                            ]))
                    ],
                    id='modal_table_record_'+table_alias,
                    is_open=False,
                )

    #  Модальное окно сохранения данных таблицы
    modal_save_table_data = dbc.Modal(
                    [
                        dbc.ModalHeader(dbc.ModalTitle("Сохранение данных таблицы")),
                        dbc.ModalBody([
                            dbc.Row([
                                dbc.Col(dbc.Label("Наименование файла"), width=7),
                                dbc.Col(dbc.Input(id='input_file_name_'+table_alias, type='text'))
                            ], style={'marginBottom': '5px'}),
                        ]),
                        dbc.ModalFooter(html.Div([
                            dbc.Button("Сохранить", id='btn_modal_save_table_data_save_'+table_alias, n_clicks=0,
                                style={'width': '120px', 'marginRight': '10px'}, color="success"), 
                            dcc.Download(id='download_dataframe_xlsx_'+table_alias),
                            dbc.Button("Закрыть", id='btn_modal_save_table_data_close_'+table_alias, n_clicks=0,
                                style={'width': '120px'}, color="warning" )
                            ]))
                    ],
                    id='modal_save_table_data_'+table_alias,
                    is_open=False
                )

    if pagination:
        table_height = '676px'
        table_page_action = 'native'
    else:
        table_height = '720px'
        table_page_action = 'none'

    #  Виджет "Таблица"
    widget = [ modal_table_record,
            modal_save_table_data,
                html.H6([     
                    html.Span(html.Img(src='assets/baseline_save_white.png', id='btn_open_modal_save_table_data_'+table_alias, n_clicks=0,), 
                            className='icon_save_table_data'),
                    html.Span(table_name, style={'marginLeft': f'{header_margin_left}px',
                                                 'color': 'DarkBlue', 'fontWeight': 'normal', 'fontSize': '18px',
                                                 }),
                    html.Span([
                        html.Span('Всего записей: ', style={'color': 'DarkBlue', 'fontSize': '13px',}),
                        html.Span(id='table_cnt_records_'+table_alias, style={'color': 'DarkBlue', 'fontSize': '13px',}),
                    ], style={'float': 'right',} ),
                ], style={'backgroundColor': 'None', 'marginBottom': '2px', 'textAlign': 'left'}), 
                dash_table.DataTable(
                    id=table_id,
                    columns=[{"name": сolumns_displayed[i], "id": i} for i in сolumns_displayed],
                    style_cell = {'font_size': '10px', 'textAlign': 'left', 'maxWidth': '170px', 
                                  'overflow': 'hidden', 'textOverflow': 'ellipsis',
                                  },
                    style_table={'height': table_height, 'overflowY': 'auto'},
                    # style_header={'backgroundColor': 'Black', 'color': 'white'},
                    # style_data={'backgroundColor': 'DarkSlateGray', 'color': 'white'},
                    style_header={'backgroundColor': 'white', 'color': 'DarkBlue', 'fontWeight': 'bold', 'fontSize': '12px', 
                                  'textAlign': 'center', },
                    style_data={'backgroundColor': 'white', },
                    style_data_conditional=[
                        {
                        'if': {'row_index': 'odd'},
                        'backgroundColor': 'WhiteSmoke',
                        },
                    ],
                    page_action=table_page_action, page_current=0, page_size=20,
                    sort_action='native',
                    filter_action='native',
                    ),
            ]
    
    return widget
