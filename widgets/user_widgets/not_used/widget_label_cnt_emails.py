from dash import dcc, html


id='label_cnt_emails'
widget = [ html.H1(style={'color': 'DarkBlue'}, id=id), html.H6('Кол-во email сообщений') ]
widget_update_data_type = 'children'
widget_select_index = 'email_messages'


def widget_update(df, filter_values_list, n):
    #
    # devices = ['desktop', 'mobile']
    # countries = ['India', 'Russia', 'England', 'US', 'Japan', 'China', 'Australia', 'Canada']

    # filter_device = devices if filter_values_list[0] == None else [filter_values_list[0]]
    # filter_country = countries if filter_values_list[1] == None else [filter_values_list[1]]
    # filter_web_service = [filter_values_list[2]] 

    return df['uniqueindexfield'].count()
        