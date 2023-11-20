from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register,\
                       login_user, logout_user, inc_product_amount, dec_product_amount, remove_product, get_product_json, add_product_ajax, delete_product_ajax, create_product_flutter
from main.models import Product

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('inc_product_amount/<int:id>', inc_product_amount, name='inc_product_amount'),
    path('dec_product_amount/<int:id>', dec_product_amount, name='dec_product_amount'),
    path('remove_product/<int:id>', remove_product, name='remove_product'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-ajax/', add_product_ajax, name='add_product_ajax'),
    path('delete_product_ajax/<int:id>', delete_product_ajax, name='delete_product_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),

]