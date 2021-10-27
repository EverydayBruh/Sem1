from django.urls import path
from .views import api_category

urlpatterns = [
	path('api/', api_category),
]