import os, dash_bootstrap_components as dbc
from dash import html


def create_template(
        widget_1, 
        ):
    """
    Создает макет дашборда (сетку)
    """

    template = [

        dbc.Col(
            html.Div(
                widget_1,
                className='widget_cell_grid_div_table'),
            className='widget_cell_grid', style={
                'backgroundColor': 'Gainsboro' #'Gray'
                }, width=12),

        # dbc.Col(
        #     html.Div(
        #         widget_2,
        #         className='widget_cell_grid_div_table'),
        #     className='widget_cell_grid', style={'backgroundColor': 'Gray'}, width=5),

    ]


    return dbc.Row(template, style={'margin': '2px 0px 2px 0px'})
