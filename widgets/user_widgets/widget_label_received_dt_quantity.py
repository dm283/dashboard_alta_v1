from dash import dcc, html
import plotly.express as px, dash_bootstrap_components as dbc


id = 'label_received_dt_quantity'
widget = [ html.H6('Количество принятых ДТ'), html.H1(style={'color': 'DarkBlue'}, id=id), ]
widget_update_data_type = 'children'
widget_select_index = 'received_dt_quantity'


def widget_update(df, filter_values_list, n):
    #  Функция формирования/обновления виджета
    # devices = ['desktop', 'mobile']
    # countries = ['India', 'Russia', 'England', 'US', 'Japan', 'China', 'Australia', 'Canada']
    
    # filter_device = devices if filter_values_list[0] == None else [filter_values_list[0]]
    # filter_country = countries if filter_values_list[1] == None else [filter_values_list[1]]
    # filter_web_service = [filter_values_list[2]] 

    # return len(df[
    #     (df['web_service'].isin(filter_web_service)) & 
    #     (df['device'].isin(filter_device)) & 
    #     (df['country'].isin(filter_country))
    #     ]['country'].unique())

    return df['received_dt_quantity']
