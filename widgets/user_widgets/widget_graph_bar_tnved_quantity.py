from dash import dcc, html
import plotly.express as px, dash_bootstrap_components as dbc

#  ЗАПОЛНЯЕТСЯ ПРИКЛАДНЫМ ПРОГРАММИСТОМ

id = 'graph_bar_tnved_quantity'
widget = dcc.Graph(id=id)
widget_update_data_type = 'figure'
widget_select_index = 'tnved_quantity'


def widget_update(df, filter_values_list, n):
    #  Функция формирования/обновления виджета
    # devices = ['desktop', 'mobile']
    # countries = ['India', 'Russia', 'England', 'US', 'Japan', 'China', 'Australia', 'Canada']

    # filter_device = devices if filter_values_list[0] == None else [filter_values_list[0]]
    # filter_country = countries if filter_values_list[1] == None else [filter_values_list[1]]
    # filter_web_service = [filter_values_list[2]] 

    # df_bar = df[ 
    #     (df['web_service'].isin(filter_web_service)) & 
    #     (df['device'].isin(filter_device)) & 
    #     (df['country'].isin(filter_country))
    #     ]
    
    df_bar = df
    
    figure = px.bar(df_bar, y='g33', x='cnt', labels={'g33':'Группа ТНВЭД', 'cnt':'Кол-во'},
                    title='ТНВЭД на складе', height=330)
    
    return figure
