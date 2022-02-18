from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.bloodpressure_main, name='bloodpressure_main'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # path('post/new/', views.post_new, name='post_new'),
    # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]