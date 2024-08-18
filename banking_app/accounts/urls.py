from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, accounts_home

urlpatterns = [
    path('', accounts_home, name='accounts_home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
