from django.urls import path
from .views import show_home, menu_list_json, menu_list_xml, menu_detail_json, menu_detail_xml, add_menu_item, delete_item
from .views import register, login_user, logout_user, edit_menu, delete_item, add_menu_item_ajax, create_menu_flutter
from django.conf import settings
from django.conf.urls.static import static

app_name = 'home'

urlpatterns = [
    path('', show_home, name='show_home'),
    path('api/menu/json/', menu_list_json, name='menu_list_json'),
    path('api/menu/xml/', menu_list_xml, name='menu_list_xml'),
    path('api/menu/json/<int:pk>/', menu_detail_json, name='menu_detail_json'),
    path('api/menu/xml/<int:pk>/', menu_detail_xml, name='menu_detail_xml'),
    path('add-menu/', add_menu_item, name='add_menu_item'),
    path('delete/<int:pk>/', delete_item, name='delete_item'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-menu/<int:pk>', edit_menu, name='edit_menu'),
    path('add-menu-ajax/', add_menu_item_ajax, name='add_menu_item_ajax'),
    path('create-flutter/', create_menu_flutter, name='create_mood_flutter'),
]