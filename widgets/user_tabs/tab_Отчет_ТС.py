import os, dash_bootstrap_components as dbc
from dash import html
from content_create_functions import create_widget_dictionary


widget = create_widget_dictionary()[0]

#  ***************************************  ДЕЙСТВИЯ ПРИКЛАДНОГО ПРОГРАММИСТА  ****************************************************
#  Укажите наименование вкладки
# label='Показатели загрузки'

# tab_content = dbc.Row([
#     'Отчет_ТС_(пр.33)'
#     ], style={'margin': '2px 0px 2px 0px'})


#  Импортируйте необходимый модуль с макетом вкладки дашборда (макеты находятся в директории user_templates)
from widgets.user_templates import template_3

#  Поместите в ячейку соответствующий виджет
tab_content = template_3.create_template(
    widget_1=widget['table_record_details_report_vehicle'],
    )
