from django.urls import path
from .views import CustomerRemainDetailView,CustomerRemainListCreateView,CustomerListCreateView,CustomerDetailView,BrokerageTransactionsDetailView,BrokerageTransactionsListCreateView

urlpatterns = [
    path('customer/', CustomerListCreateView.as_view(), name='customer'),
    path('customer/<int:pk>/',CustomerDetailView.as_view(), name='customer'),
    path('customerremain/',CustomerRemainListCreateView.as_view(), name='customerremain'),
    path('customerremain/<int:pk>/',CustomerRemainDetailView.as_view(), name='customerremain'),
    path('brokeragetransactions/',BrokerageTransactionsListCreateView.as_view(), name='brokeragetransactions'),
    path('brokeragetransactions/<int:pk>/',BrokerageTransactionsDetailView.as_view(), name='brokeragetransactions'),

]

