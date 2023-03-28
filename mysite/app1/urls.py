from django.urls import path
from .views import my_view

urlpatterns = [
    path('', my_view, name='home'),
    path('record/<int:id>/', my_view, name='record_detail'),
]