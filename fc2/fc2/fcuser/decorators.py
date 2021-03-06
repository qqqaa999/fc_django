from django.shortcuts import redirect
from .models import Fcuser

def login_required(func):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login')
        return func(request, *args, **kwargs)
    return wrap

def admin_required(func):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login')

        user = Fcuser.objects.get(email=user)
        if user.level != 'admin':
            return redirect('/')
        return func(request, *args, **kwargs)
    return wrap