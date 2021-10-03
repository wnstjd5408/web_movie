from django import forms
from .models import Person
from argon2 import PasswordHasher, exceptions


class LoginForm(forms.Form):
    user_id = forms.CharField(
        max_length=32,
        label="아이디",
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
        error_messages={'required': '아이디를 입력해주세요'}
    )
    user_pw = forms.CharField(
        max_length=128,
        label='비밀번호',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        error_messages={'required': '비밀번호를 입력해주세요'}

    )

    field_order = [

        'user_id',
        'user_pw'
    ]

    def clean(self):
        cleaned_data = super().clean()

        user_id = cleaned_data.get('user_id', '')
        user_pw = cleaned_data.get('user_pw', '')

        if user_id == '':
            return self.add_error('user_id', '아이디를 입력해 주세요.!!')
        elif user_pw == '':
            return self.add_error('user_pw', '비밀번호를 입력해 주세요.!!')
        else:
            try:
                person = Person.objects.get(user_id=user_id)

            except:
                return self.add_error('user_id', '아이디가 존재하지 않습니다')
            try:
                PasswordHasher().verify(person.password, user_pw)

            except exceptions.VerifyMismatchError:
                return self.add_error('user_pw', '비밀번호가 다릅니다')


class RegisterForm(forms.ModelForm):

    field_order = [
        'user_id',
        'password1',
        'password2',
        'name',
        'gender',
        'age',
        'phone_number',
        'email',
        'address',
    ]

    class Meta:
        model = Person

        fields = [
            'user_id',
            'password1',
            'name',
            'gender',
            'age',
            'phone_number',
            'email',
            'address',
        ]

    user_id = forms.CharField(
        label='아이디',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '아이디'
            }
        ),
        error_messages={'required': '아이디를 입력해주세요'}
    )
    password1 = forms.CharField(
        label='비밀번호',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호'
            }
        ),
        error_messages={'required': '비밀번호를 입력해주세요'}
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호 확인'
            }
        ),
        error_messages={'required': '비밀번호가 일치하지 않습니다'}
    )
    name = forms.CharField(
        label='이름',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '이름'
            }
        ),
        error_messages={'required': '이름을 입력해주세요'}
    )
    gender = forms.CharField(
        label='성별',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '성별'
            }
        ),
        error_messages={'required': '성별을 입력해주세요'}
    )
    age = forms.IntegerField(
        label='나이',
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': '나이'
            }
        ),
        error_messages={'required': '나이를 입력해주세요'}
    )
    phone_number = forms.CharField(
        label='핸드폰번호',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '핸드폰번호'
            }
        ),
        error_messages={'required': '번호를 입력해주세요'}
    )
    email = forms.EmailField(
        label='이메일',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '이메일'
            }
        ),
        error_messages={'required': '이메일을 입력해주세요'}
    )
    address = forms.CharField(
        label='주소',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '주소'
            }
        ),
        error_messages={'required': '주소를 입력해주세요'}
    )

    # def save(self, *args,  **kwargs):
    #     person = super().save(commit=False)
    #     password = self.cleaned_data.get('password1')

    #     person.save()

    def clean(self):
        cleaned_data = super().clean()

        user_id = cleaned_data.get('user_id', '')
        password1 = cleaned_data.get('password1', '')
        password2 = cleaned_data.get('password2', '')
        name = cleaned_data.get('name', '')
        gender = cleaned_data.get('gender', '')
        age = cleaned_data.get('age', '')
        phone_number = cleaned_data.get('phone_number', '')
        email = cleaned_data.get('email', '')
        address = cleaned_data.get('address', '')

        if password1 != password2:
            return self.add_error('password2', '비밀번호가 다릅니다')
        elif not(4 <= len(user_id) <= 16):
            return self.add_error('user_id', '아이디는 4~16자리로 입력해 주세요')
        elif 8 > len(password1):
            return self.add_error('password1', '비밀번호는 8자리 이상을 적어주세요.')
        else:
            self.user_id = user_id
            self.password1 = PasswordHasher().hash(password1)
            self.password2 = password2
            self.name = name
            self.gender = gender
            self.age = age
            self.phone_number = phone_number
            self.email = email
            self.address = address
