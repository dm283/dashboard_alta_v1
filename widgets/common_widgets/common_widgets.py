#  Общие виджеты для всех типовых дашбордов

import plotly.express as px, dash_bootstrap_components as dbc
from dash import dcc, html, dash_table
from widgets.user_widgets import data_filters

DATA_UPDATE_PERIOD = 3600

#  Кнопка НАСТРОЙКИ с модальным окном
btn_settings = [
            html.Img(src='assets/baseline_more_vert_white.png', id='btn_settings', n_clicks=0),
            dbc.Modal(
                [
                    dbc.ModalHeader(dbc.ModalTitle("Настройки дашборда")),
                    dbc.ModalBody([
                        dbc.Row([
                            dbc.Col(dbc.Label("Период обновления данных (сек)"), width=7),
                            dbc.Col(dbc.Input(id='input_period', value=DATA_UPDATE_PERIOD, type='text'))
                        ], style={'marginBottom': '5px'}),
                        dbc.Row([
                            dbc.Col(dbc.Label('Цветовая тема'), width=7),
                            dbc.Col(dbc.Select(id='select_theme', options=['Светлая', 'Тёмная'], value='Светлая'))
                        ], style={'marginBottom': '5px'})
                    ]),
                    dbc.ModalFooter(html.Div([
                        dbc.Button("Применить", id='btn_settings_apply', n_clicks=0,
                            style={'width': '120px', 'marginRight': '10px'}, color="success"), 
                        dbc.Button("Закрыть", id='btn_settings_close', n_clicks=0,
                            style={'width': '120px'}, color="warning" )
                        ]))
                ],
                id='settings_modal_window',
                is_open=False
            ),
        ]


btn_update_data = html.Img(src='assets/baseline_refresh_white.png', id='btn_update_data', n_clicks=0)

btn_user_actions = dcc.Link(html.Img(src='assets/baseline_logout_white.png', id='btn_user_actions', n_clicks=0), 
                            href='/')

# Формирование области фильтров
data_filter = data_filters.data_filter  # фильтры данных

filters_area = []
for k in range(len(data_filter)):
    filters_area.append(
        dbc.Row( data_filter[k],
                className='widget_cell_grid', 
                style={'padding': '0px 5px 10px 5px', 'border': 'None'},
                )
        )

btn_show_filters = [
    html.Img(src='assets/baseline_filter_alt_white.png', id='btn_show_filters', n_clicks=0),
    dbc.Offcanvas(
            filters_area,
            id="offcanvas_filters",
            title="Фильтры данных",
            placement='end',
            is_open=False,
            className='filters_area',
        ),
    ]