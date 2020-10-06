from django.urls import path

from . import views

app_name = 'analysis'

urlpatterns = [
    path('', views.analysis, name='analysis'),
	path('meeting_times', views.meeting_times, name='meeting_times'),
    path('popular_courses', views.popular_courses, name='popular_courses'),
    path('meeting_days', views.meeting_days, name='meeting_days'),
]