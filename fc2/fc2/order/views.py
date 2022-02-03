from re import template
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .models import Order
# Create your views here.

class OrderCreate(FormView):
    form_class = RegisterForm
    success_url = '/product/'
    
    def form_invalid(self, form):                                      
        return redirect('/product/' + str(form.product))

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw

class OrderList(ListView):
    template_name = 'order.html'
    context_object_name = 'order_list'

    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter(fcuser__email=self.request.session.get('user'))
        return queryset