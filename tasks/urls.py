from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:pk>/', views.detail, name="detail"),
    path('create/', views.create_task, name="create_task"),
    path('update/<int:pk>/', views.update_task, name="update_task")
]
