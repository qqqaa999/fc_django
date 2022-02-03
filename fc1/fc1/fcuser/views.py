from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Fcuser
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

def home(request):
    user_id = request.session.get('user')

    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)

    return render(request, 'home.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        useremail = request.POST.get('useremail', None)
        
        res_data = {}

        if not (username and password and re_password and useremail):
            res_data['error'] = '모든 값을 입력해야합니다.'

        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        
        else:
            fuser = Fcuser.objects.filter(username=username)

            if fuser != None:
                res_data['error'] = '중복된 아이디입니다.'
            
            else:
                fcuser = Fcuser(
                    username=username,
                    password=make_password(password),
                    useremail=useremail,
                )
                fcuser.save()
                
        return render(request, 'register.html', res_data)

def login(request):
    if request.method == 'POST':
        form =  LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form' : form })

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')
    
#login
    # if request.method == 'GET':
    #     return render(request, 'login.html')

    # elif request.method == 'POST':
    #     username = request.POST.get('username', None)
    #     password = request.POST.get('password', None)
    #     res_data = {}

    #     if not (username, password):
    #         res_data['error'] = '모든 값을 입력해야합니다.'
    #     else:
    #         try:
    #             fcuser = Fcuser.objects.get(username=username)
    #             if check_password(password, fcuser.password):
    #                 request.session['user'] = fcuser.id
    #                 return redirect('/')
    #             else: 
    #                 res_data['error'] = '비밀번호가 틀렸습니다.'

    #         except :
    #             res_data['error'] = '없는 아이디입니다.'

        # return render(request, 'login.html', res_data)