from dash import dcc, html
import plotly.express as px, dash_bootstrap_components as dbc
from datetime import datetime


id = 'graph_scatter_cnt_users' #'scatter_cnt_users'
widget = dcc.Graph(id=id)
widget_update_data_type = 'figure'
widget_select_index = 'web_service_usage'


def widget_update(df, filter_values_list, ax_msg, ay_msg, n):
    #

    devices = ['desktop', 'mobile']
    countries = ['India', 'Russia', 'England', 'US', 'Japan', 'China', 'Australia', 'Canada']

    filter_device = devices if filter_values_list[0] == None else [filter_values_list[0]]
    filter_country = countries if filter_values_list[1] == None else [filter_values_list[1]]
    filter_web_service = [filter_values_list[2]] 

    cnt_users = df[
        (df['web_service'].isin(filter_web_service)) & 
        (df['device'].isin(filter_device)) & 
        (df['country'].isin(filter_country))
        ]['id'].count()
    if len(ay_msg) == 0 or cnt_users != ay_msg[-1]:
        per_dt = str(datetime.now().strftime("%H:%M:%S"))
        ax_msg.append(per_dt)
        ay_msg.append(cnt_users)
        if len(ax_msg) > 9:
            ax_msg.pop(0)
            ay_msg.pop(0)
    figure = px.scatter(title='Кол-во пользователей онлайн', height=310)
    figure.add_traces(list(px.line(x=ax_msg, y=ay_msg, markers=True).select_traces()))
    return figure
