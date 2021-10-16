from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group
from django import forms
from .models import User
from argon2 import PasswordHasher, exceptions
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import check_password


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['password', 'age', 'gender',
                  'phone_number', 'address', ]


class CheckPasswordForm(forms.Form):
    password = forms.CharField()

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = self.user.password

        if password:
            if not check_password(password, confirm_password):
                self.add_error('password', '비밀번호가 일치하지 않습니다')


class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('email', 'name', 'gender', 'age', 'phone_number',
                  'address', 'password1', 'password2')


class LoginForm(forms.Form):
    # class Meta:
    #     model = User

    email = forms.EmailField(
        error_messages={'required': '이메일를 입력해주세요'}
    )
    password = forms.CharField(
        error_messages={'required': '비밀번호를 입력해주세요'}
    )

    def clean(self):
        cleaned_data = super().clean()

        email = cleaned_data.get('email', '')
        password = cleaned_data.get('password', '')

        if email == '':
            return self.add_error('email', '이메일을 입력해 주세요.!!')
        elif password == '':
            print('비밀번호없음')
            return self.add_error('password', '비밀번호를 입력해 주세요.!!')
        else:
            try:
                user = get_object_or_404(User, email=email)
                print('이메일존재')
                if not check_password(password, user.password):
                    self.add_error('password', '패스워드가 틀렸습니다')
                else:
                    self.email = user.email
            except:
                return self.add_error('email', '이메일이 존재하지 않습니다')

                # PasswordHasher().verify(user.password, password)
                # User.check_password(self, user.password)


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    password2 = forms.CharField(label='비밀번호확인', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'name', 'gender',
                  'age', 'phone_number', 'address']

    def clean_password2(self):

        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("비밀번호가 맞지 않습니다")

        return password2

    def save(self, commit=True):
        user = super.save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def clean(self):
        cleaned_data = super().clean()

        email = cleaned_data.get('email', '')
        password1 = cleaned_data.get('password1', '')
        password2 = cleaned_data.get('password2', '')
        name = cleaned_data.get('name', '')
        gender = cleaned_data.get('gender', '')
        age = cleaned_data.get('age', '')
        phone_number = cleaned_data.get('phone_number', '')
        address = cleaned_data.get('address', '')

        if email == '':
            return self.add_error('email', '를 입력해 주세요.!!')
        elif 8 > len(password1):
            return self.add_error('password1', '비밀번호는 8자리 이상을 적어주세요.')
        else:
            self.email = email
            self.password1 = password1
            self.password2 = password2
            self.name = name
            self.gender = gender
            self.age = age
            self.phone_number = phone_number
            self.address = address


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        Model = User
        fields = ('email', 'password', 'name', 'gender', 'age',
                  'phone_number', 'address', 'is_active', 'is_admin')
