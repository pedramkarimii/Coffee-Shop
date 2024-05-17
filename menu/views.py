from django.views.generic import ListView, View,DetailView
from django.shortcuts import render ,HttpResponse,redirect
from .models import *
from orders.models import *
from django.db.models import Q

class CategoryView(ListView):
    model = Category
    template_name = 'menu/categories.html'
    context_object_name = 'categories_list'

    def get_queryset(self):
        if self.request.GET.get("q")!=None:
            query = self.request.GET.get('q')
            return (Category.objects.filter(
                Q(name__icontains=query)
            ))

        else:
            return Category.objects.all()


class ProductView(View):
    def get(self, request, id):
        category = Category.objects.get(id=id)
        products = Product.objects.filter(categories=category)

        return render(request, 'menu/products.html', {'products_list': products})


class TransactionView(View):

    def get(self,request,id):

        # if not Order.objects.filter(user=request.user, ).exists():
        #     create_order= Order.objects.create(user=request.user,  )
        #     create_order.save()

        get_product=Product.objects.get(id=id)
        get_user = User.objects.get(username=request.user)
        get_order = Order.objects.get(user=get_user)



        if not OrderItem.objects.filter(product=get_product, order=get_order).exists():

            create_object=OrderItem.objects.create(product=get_product,order=get_order,)
            create_object.save()
            return HttpResponse('add to cart')
        else:
            return HttpResponse('already exists')


# class AdminCustom(View):
#     def get(self,request):
#         all_products = Product.objects.all()
#         return render(request,"admin/base.html",context={'all_products':all_products})



# class SearchView(ListView):
#     model = Product
#     template_name = 'menu'
#     context_object_name = ''
#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         return Product.objects.filter(
#             Q(name__icontains=query) | Q(description__icontains=query)
#         )
