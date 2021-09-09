from django.urls import path
from . import views

urlpatterns = [
    path('', views.capture, name="capture"),
    path('create/', views.create_capture, name='create_capture')
]