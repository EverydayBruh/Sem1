from django.urls import path
from .views import api_category, api_event, api_user, api_event_detail

urlpatterns = [
	path('api/category', api_category),
	path('api/events', api_event),
	path('api/events/<int:pk>', api_event_detail),
	path('api/users', api_user),
]