import django


from django import forms

from .models import User

class RegisterForm(forms.ModelForm):
    # 회원가입 폼, 장고에서는 HTML 입력요소를 widget이라고 말함
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    re_password = forms.CharField(label='re password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'gender', 'email']

    def clean(self):
        cd = self.cleaned_data
        if cd['password'] != cd['re_password']:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다!')
            
        return cd['re_password']