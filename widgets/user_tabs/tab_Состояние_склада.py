import os, dash_bootstrap_components as dbc
from dash import html
from content_create_functions import create_widget_dictionary


widget = create_widget_dictionary()[0]

#  ***************************************  ДЕЙСТВИЯ ПРИКЛАДНОГО ПРОГРАММИСТА  ****************************************************
#  Укажите наименование вкладки
# label='Основные показатели'

# tab_content = dbc.Row([
#     'Состояние_склада'
#     ], style={'margin': '2px 0px 2px 0px'})


#  Импортируйте необходимый модуль с макетом вкладки дашборда (макеты находятся в директории user_templates)
from widgets.user_templates import template_1

#  Поместите в ячейку соответствующий виджет
tab_content = template_1.create_template(
    widget_1_1_1=widget['label_product_quantity'],
    widget_1_1_2=widget['label_dt_quantity'],
    widget_1_2_1=widget['graph_bar_tnved_quantity'],
    widget_2_1=widget['table_record_details_products_on_storage'],
    )
