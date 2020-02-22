from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post_list/', views.post_list, name='post_list'),
    path('post_list/close_post/', views.add_post, name='add_post'),
    path('post_list/close_post/<int:post_id>/', views.close_post, name='close_post'),
    path('post_list/view_post/<int:post_id>/', views.view_post, name='view_post'),
]