from django.urls import path
from .views import api_category, api_event, api_user

urlpatterns = [
	path('api/category', api_category),
	path('api/events', api_event),
	path('api/users', api_user),
]