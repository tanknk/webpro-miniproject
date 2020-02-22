from django.urls import path, include
from . import views

urlpatterns = [
    # path('login/', views.login_test, name='login'),
    path('signup/', views.signup, name='signup'),
    path('', include("post.urls"), name='index'),
]