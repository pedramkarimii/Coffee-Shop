from django.urls import path
from . import views
# from .views import AllOrders

urlpatterns = [
    path('', views.AllOrders.as_view(), name='all_orders'),
    path('detail/<int:pk>', views.OrderDetail.as_view(), name='detail'),
    path('paid/<int:pk>', views.PaidOrderDetail.as_view(), name='paid')
]
