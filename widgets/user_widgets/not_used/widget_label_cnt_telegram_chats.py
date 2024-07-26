from dash import dcc, html


id='label_cnt_telegram_chats'
widget = [ html.H1(style={'color': 'DarkBlue'}, id=id), html.H6('Кол-во telegram-чатов') ]
widget_update_data_type = 'children'
widget_select_index = 'telegram_chats'


def widget_update(df, filter_values_list, n):
    #
    # devices = ['desktop', 'mobile']
    # countries = ['India', 'Russia', 'England', 'US', 'Japan', 'China', 'Australia', 'Canada']

    # filter_device = devices if filter_values_list[0] == None else [filter_values_list[0]]
    # filter_country = countries if filter_values_list[1] == None else [filter_values_list[1]]
    # filter_web_service = [filter_values_list[2]] 

    return df['id'].count()
        