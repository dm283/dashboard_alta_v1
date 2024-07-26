# FILTERS
from functions_library import create_filter, get_db_connect, get_db_data_to_datafame, DB_NAME, DB_SCHEMA

import warnings
warnings.filterwarnings('ignore')

conn = get_db_connect()
data_filter = {}


# filter 0
id = 0
f_type = 'date_picker'
name = 'date_doc [ Книга учета ]'
placeholder = 'DD/MM/YYYY'
value = None
clearable = True
column = ''
query = ''
data_filter[id] = create_filter(f_type, name, placeholder, value, clearable, column, query, conn)


# filter 1
id = 1
f_type = 'date_picker'
name = 'Дата приема [ Книга учета ]'
placeholder = 'DD/MM/YYYY'
value = None
clearable = True
column = ''
query = ''
data_filter[id] = create_filter(f_type, name, placeholder, value, clearable, column, query, conn)


# filter 2
id = 2
f_type = 'date_picker'
name = 'Дата выдачи - Дата приема [ Отчет ТС ]'
placeholder = 'DD/MM/YYYY'
value = None
clearable = True
column = ''
query = ''
data_filter[id] = create_filter(f_type, name, placeholder, value, clearable, column, query, conn)


# # filter 0
# id = 0
# f_type = 'dropdown'
# name = 'Тип устройства'
# placeholder = 'Выберите тип устройства'
# value = None
# clearable = True
# column = 'device'
# query = f"""
#     select distinct device from {DB_NAME}.{DB_SCHEMA}.web_service_usage order by device
#     """
# data_filter[id] = create_filter(f_type, name, placeholder, value, clearable, column, query, conn)

# # filter 1
# id = 1
# f_type = 'dropdown'
# name = 'Страна пользователя'
# placeholder = 'Выберите страну'
# value = None
# clearable = True
# column = 'country'
# query = f"""
#     select distinct country from {DB_NAME}.{DB_SCHEMA}.web_service_usage order by country
#     """
# data_filter[id] = create_filter(f_type, name, placeholder, value, clearable, column, query, conn)

# # filter 2
# id = 2
# f_type = 'dropdown'
# name = 'Веб-сервис'
# placeholder = 'Выберите веб-сервис'
# value = 'aDashboard'
# clearable = False
# column = 'web_service'
# query = f"""
#     select distinct web_service from {DB_NAME}.{DB_SCHEMA}.web_service_usage order by web_service
#     """
# data_filter[id] = create_filter(f_type, name, placeholder, value, clearable, column, query, conn)

# # filter 3
# id = 3
# f_type = 'dropdown'
# name = 'Адрес e-mail'
# placeholder = 'Выберите адрес e-mail'
# value = None
# clearable = True
# column = 'adrto'
# query = f"""
#     select distinct adrto from {DB_NAME}.{DB_SCHEMA}.messages_email order by adrto
#     """
# data_filter[id] = create_filter(f_type, name, placeholder, value, clearable, column, query, conn)
