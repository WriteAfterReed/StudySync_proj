from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('view_user/<int:pk>', views.user_view, name='user_view'),
    path('new_user', views.user_create, name="user_new"),
    path('edit_user/<int:pk>', views.user_update, name='user_edit'),
    path('delete_user/<int:pk>', views.user_delete, name='user_delete'),
    path("user_find_friends", views.user_find_friends, name= "user_find_friends")
]