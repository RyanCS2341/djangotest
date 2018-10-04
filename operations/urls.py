from django.urls import path
from . import views

urlpatterns = [
    path('query/', views.query, name='operations-query'),
    path('addition/', views.addition, name='operations-addition'),
    path('subtraction/', views.subtraction, name='operations-subtraction'),
    path('home/', views.home, name="operations-home"),
    path('index.html/', views.index, name='index')
]
