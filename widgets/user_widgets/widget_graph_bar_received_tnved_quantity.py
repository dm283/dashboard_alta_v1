from dash import dcc, html
import plotly.express as px, dash_bootstrap_components as dbc

#  ЗАПОЛНЯЕТСЯ ПРИКЛАДНЫМ ПРОГРАММИСТОМ

id = 'graph_bar_received_tnved_quantity'
widget = dcc.Graph(id=id)
widget_update_data_type = 'figure'
widget_select_index = 'received_tnved_quantity'


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

    # if filter_values_list[0][0] or filter_values_list[0][1]:
    #     print(11111111)
    #     if filter_values_list[0][0]:
    #         df_bar = df_bar[ df_bar['date_in'] >= filter_values_list[0][0] ]
    #     if filter_values_list[0][1]:
    #         df_bar = df_bar[ df_bar['date_in'] < filter_values_list[0][1] ]   
    
    figure = px.bar(df_bar, orientation='v', y='cnt', x='g33', labels={'g33':'Группа ТНВЭД', 'cnt':'Кол-во'},
                    title='Принятые ТНВЭД', height=400)
    
    return figure
