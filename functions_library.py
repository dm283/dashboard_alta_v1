# БИБЛИОТЕКА СИСТЕМНЫХ ФУНКЦИЙ ДЛЯ DASHBOARD_PROJECT
import sys, os, configparser, psycopg2, pyodbc, pandas as pd, time
from pathlib import Path
from dash import dcc, html
from datetime import date, datetime

config = configparser.ConfigParser()
config_file = os.path.join(Path(__file__).resolve().parent, 'config.ini')   
if os.path.exists(config_file):
  config.read(config_file, encoding='utf-8')
else:
  print("error! config file doesn't exist"); sys.exit()

DEBUG = config.getboolean('main', 'debug')
HOST = config['main']['host']
PORT = config['main']['port']

DB_CONNECTION_STRING = config['db']['db_connection_string']
DB_TYPE = config['db']['db_type']
DB_NAME = config['db']['db_name']
DB_SCHEMA = config['db']['db_schema']

COMPANY_NAME = config['content']['company_name']


def get_db_connect():
  #  Подключение к базе данных, варианты для postres и ms-sql
  print(f'connecting to database server [{DB_CONNECTION_STRING}] ... ', end='')

  try:
    if DB_TYPE == '-p':  # postgre database
      if 'DSN=' in DB_CONNECTION_STRING:
        CONN = pyodbc.connect(DB_CONNECTION_STRING)
      else:
        CONN = psycopg2.connect(DB_CONNECTION_STRING)  
    elif DB_TYPE == '-m':  # ms-sql database
      CONN = pyodbc.connect(DB_CONNECTION_STRING)     
    
    status = 'ok'; result = CONN

  except(Exception) as err:
    status = 'error'; result = err

  print(status)
  return status, result


def get_db_data_to_datafame(select):
    #  Загрузка из базы данных в pandas-датафрейм
    # df = pd.read_sql(select, conn)
    # return df
    err = 1

    while err:

      try:
        conn_status, conn_result = get_db_connect()
        if conn_status == 'error':
          raise Exception(conn_result)
        elif conn_status == 'ok':
          conn = conn_result

        print(f'reading from database [{DB_NAME}] ... ', end='')
        df = pd.read_sql(select, conn)

        err = 0
        print('ok')
        conn.close()

      except Exception as ex:
        print('error', ex)

        with open('logs/log.txt', 'a') as f:
          log_record = f'{datetime.now()} -- error -- {ex}\n\n'
          f.write(log_record)

        time.sleep(5)
        err = 1

    return df


def create_filter(f_type, name, placeholder, value, clearable, column, query):
    #  Создает объект фильтр
    if f_type == 'date_picker':
      data_filter = [html.Div(name, className='filter_label'),
        dcc.DatePickerRange( clearable=clearable, className='filter_date_picker', display_format=placeholder,
                            start_date_placeholder_text=placeholder, end_date_placeholder_text=placeholder,
                            # initial_visible_month=date(2017, 8, 5),
                            id={'type': 'filter_date', 'index': f'filter_{column}'}, ),
      ]
    else:
      filter_values_list = get_db_data_to_datafame(query)[column].to_list()
      data_filter = [html.Div(name, className='filter_label'),
                      dcc.Dropdown(options=filter_values_list, value=value, placeholder=placeholder, clearable=clearable,
                          className='filter_dropdown', 
                          id={'type': 'filter_dropdown', 'index': f'filter_{column}'}, )]
    return data_filter


# def get_db_connect():
#     """
#     Подключение к базе данных
#     """
#     conn = None
#     try:
#         print('connecting to data base ... ', end='')
#         conn = psycopg2.connect(
#             host='localhost',
#             port='5432',
#             database='dev_pg_1',
#             user='postgres',
#             password='s2d3f4!@'
#         )
#     except (Exception, psycopg2.DatabaseError) as err:
#         print(err)
#         sys.exit(1)
#     print('OK')
#     return conn


# def get_db_data_to_datafame(conn, select, column_names):
#     """
#     Загрузка из базы данных в pandas-датафрейм
#     """
#     cursor = conn.cursor()
#     try:
#         cursor.execute(select)
#     except (Exception, psycopg2.DatabaseError) as err:
#         print('Error:', err)
#         cursor.close()
#         return 1
#     tuples_list = cursor.fetchall()
#     cursor.close()
#     df = pd.DataFrame(tuples_list, columns=column_names)
#     return df
