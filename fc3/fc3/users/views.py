from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False) #commit=False을 했기 때문에 DB에 영향을 주지 않고 메모리 상에서 저장이됨
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            return render(request, 'registration/login.html', {'user_form':user})
    else:
        user_form = RegisterForm()
    
    return render(request, 'registration/register.html', {'user_form':user_form})