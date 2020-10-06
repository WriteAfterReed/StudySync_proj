from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('groups.urls', namespace='groups')),
    path('groups/', include('groups.urls', namespace='groups')),

    # The above throws a stupid error if things map to the same place


    # http://localhost:8000/users/list_users 
    path('users/', include('users.urls', namespace='users')),
	path('analysis/', include('analysis.urls', namespace='analysis'))
]
