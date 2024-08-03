# urls.py
from django.urls import path
from .views import TransactionListView, TransactionCreateView

urlpatterns = [
    path('', TransactionListView.as_view(), name='transaction_list'),
    path('add/', TransactionCreateView.as_view(), name='add_transaction'),
]