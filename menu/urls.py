from django.urls import path
from .views import *


urlpatterns = [
    path('categories/',CategoryView.as_view(),name='categories' ),
    path('products/<int:id>',ProductView.as_view(),name='products' ),
    path('transaction/<int:id>',TransactionView.as_view(),name='transaction' ),


]
