from django.shortcuts import render,redirect, reverse, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, FormView
from .models import Product, Order, Transaction
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .forms import TransactionForm
from django import forms
from django.forms import ModelForm, Textarea
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

def homeView(request):
    objs_list = Product.objects.all()
    transaction = Transaction.objects.filter(firstname = request.user)
    context = {
        'objs_list':objs_list ,
        'trans' : transaction
    }
    return render(request, "home.html", context)

class productView(View):
    def get(self, request):
        return render(request, 'product.html')

def contact(request):
    transaction = Transaction.objects.filter(firstname = request.user)
    return render(request, "contact.html", {'trans':transaction})

def product(request, product_id):
    try:
        product = Product.objects.get(pk = product_id)
        li = Product.objects.all()
        related_product = []
        transaction = Transaction.objects.filter(firstname = request.user)
        for i in range(0,4):
            if(li[i] != product):
                related_product.append(li[i])
        context = {
            'product' : product,
            'related' : related_product,
            'trans' : transaction
        }
    except Product.DoesNotExist:
        return render(request, 'product.html', context)
    return render(request, 'product.html', context)

def add2Cart(request, product_id):
    product = Product.objects.get(pk = product_id)
    transaction_qs = Transaction.objects.filter(firstname = request.user)
    if(transaction_qs.exists()):
        transaction = transaction_qs[0]
        order = Order.objects.create(product = product,transaction = transaction, priceOrder = product.price)
    else:    
        transaction = Transaction.objects.create(firstname = request.user)
        order = Order.objects.create(product = product,transaction = transaction, priceOrder = product.price)
    return redirect("cart")

def cart(request):
    try:
        transaction_qs = Transaction.objects.filter(firstname = request.user)
        transaction = transaction_qs[0]
        orders = Order.objects.filter(transaction = transaction)
        tong = 0
        for i in orders:
            tong += i.amount * i.product.price
        context = {
            'objl': orders,
            'sum': tong,
            'trans' : transaction
        }
        return render(request, 'cart.html',context)
    except :
        return render(request, 'cart.html')

def removeCart(request):
    transaction_qs = Transaction.objects.filter(firstname = request.user)
    transaction = transaction_qs[0]
    orders = Order.objects.filter(transaction = transaction)
    orders.all().delete()
    return redirect('cart')

class checkoutView(UpdateView):
    template_name = 'checkout.html'
    form_class = TransactionForm
    success_url = reverse_lazy('ok')
    def form_valid(self, form):
        from pprint import pprint; pprint(form.cleaned_data)
        return super().form_valid(form)
    def get_object(self):
        transaction_qs = Transaction.objects.filter(firstname = self.request.user)
        transaction = transaction_qs[0]
        return transaction
             
def checkout_ok(request):
    return render(request, 'checkout_ok.html')
