from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView
from orders.models import Order, OrderItem


# Create your views here.

class AllOrders(ListView):
    model = Order
    template_name = 'basket/allcarts.html'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-id')


class OrderDetail(UpdateView):
    model = Order
    fields = '__all__'
    template_name = 'basket/cart.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.user != self.request.user:
            raise Http404("You do not have permission to view this order.")
        return obj

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.is_paid:
            return redirect(reverse_lazy('paid', kwargs={'pk': obj.pk}))
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        result = (list(request.POST)[1])
        if 'payNow' in result:
            order = Order.objects.get(id=self.object.id)
            order.is_paid = True
            order.save()
            Order.objects.create(user=self.request.user)
        elif 'clearCart' in result:
            order = Order.objects.get(id=self.object.id)
            for item in order.order_items.all():
                item.delete()
        elif 'deleteItem_' in result:
            item_id = result.split('_')[1]
            item = OrderItem.objects.get(id=item_id)
            item.delete()
        elif 'decreaseQuantity_' in result:
            item_id = result.split('_')[1]
            item = OrderItem.objects.get(id=item_id)
            item.quantity -= 1
            item.save()
        elif 'increaseQuantity_' in result:
            item_id = result.split('_')[1]
            item = OrderItem.objects.get(id=item_id)
            item.quantity += 1
            item.save()

        return self.render_to_response(self.get_context_data())


class PaidOrderDetail(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'basket/paid.html'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if not obj.is_paid:
            return redirect(reverse_lazy('detail', kwargs={'pk': obj.pk}))
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.user != self.request.user:
            raise Http404("You do not have permission to view this order.")
        return obj
