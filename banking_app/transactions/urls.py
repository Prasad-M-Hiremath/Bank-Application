from django.urls import path
from .views import deposit, withdraw, check_balance

urlpatterns = [
    path('deposit/', deposit, name='deposit'),
    path('withdraw/', withdraw, name='withdraw'),
    path('balance/', check_balance, name='balance'),
]
