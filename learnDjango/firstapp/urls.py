from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='test'),
    path('test2', views.test_two, name='test2'),
    path('create', views.create, name='create'),
]