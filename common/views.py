from django.shortcuts import render, redirect
from .models import Person
from argon2 import PasswordHasher
# from .forms import RegisterForm
# Create your views here.


def user_register(request):
    # register_form = RegisterForm()
    # context = {'forms': register_form}

    # if request.method == 'GET':
    #     return render(request, 'common/user_register.html', context)
    # elif request.method == 'POST':
    #     register_form = RegisterForm(request.POST)
    #     if register_form.is_valid():
    #         user = User(
    #             user_id=register_form.user_id,
    #             password=register_form.password1,
    #             name=register_form.name,
    #             gender=register_form.gender,
    #             age=register_form.name,
    #             phone_number=register_form.phone_number,
    #             email=register_form.email,
    #             address=register_form.address
    #         )
    #         user.save()
    #         return redirect('/')
    #     else:
    #         context['forms'] = register_form
    #     return render(request, 'common/user_register.html', context)
    if request.method == 'GET':
        return render(request, 'common/user_register.html')

    elif request.method == 'POST':
        user_id = request.POST.get('user_id', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        username = request.POST.get('username', '')
        gender = request.POST.get('gender', '')
        email = request.POST.get('email', '')
        age = request.POST.get('age', '')
        phone_number = request.POST.get('phone_number', '')
        address = request.POST.get('address', '')

        if(user_id or password1 or password2 or username or gender or email or phone_number or address) == '':
            return redirect('/common/user_register.html')
        elif password1 != password2:
            return redirect('/common/user_register.html')
        else:
            person = Person(
                user_id=user_id,
                password=password1,
                name=username,
                gender=gender,
                age=age,
                phone_number=phone_number,
                email=email,
                address=address

            )
            person.save()
        return redirect('/')
