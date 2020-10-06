from django.urls import path

from groups import views

app_name = 'groups'



urlpatterns = [
    path('', views.group_list, name='group_list'),
    path('view/<int:pk>', views.group_view, name='group_view'),
    path('new', views.group_create, name="group_new"),
    path('edit/<int:pk>', views.group_update, name='group_edit'),
    path('delete/<int:pk>', views.group_delete, name='group_delete'),
    path('group_search_course', views.group_search_course, name='group_search_course'),
    path('search_availability', views.search_availability, name = 'search_availability'),
    path('group_search_course_language', views.group_search_course_language, name = 'group_search_course_language')
]