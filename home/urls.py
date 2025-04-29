from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='home'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
]
