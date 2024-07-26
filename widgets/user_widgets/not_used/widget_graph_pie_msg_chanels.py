from dash import dcc, html
import plotly.express as px, dash_bootstrap_components as dbc


id = 'graph_pie_msg_chanels'
widget = dcc.Graph(id=id)
widget_update_data_type = 'figure'
widget_select_index = 'count_messages'


def widget_update(df, filter_values_list, n):
    #
    # devices = ['desktop', 'mobile']
    # countries = ['India', 'Russia', 'England', 'US', 'Japan', 'China', 'Australia', 'Canada']

    # filter_device = devices if filter_values_list[0] == None else [filter_values_list[0]]
    # filter_country = countries if filter_values_list[1] == None else [filter_values_list[1]]
    # filter_web_service = [filter_values_list[2]] 

    df_pie = df
    figure = px.pie(df_pie, values='msg_cnt', names='channel', title='Каналы рассылки', height=433)

    return figure
