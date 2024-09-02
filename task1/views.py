from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer, Game


def platform(request):
    return render(request, 'platform.html')


def games(request):
    games = Game.objects.all()
    return render(request, 'games.html', {'games': games})


def cart(request):
    return render(request, 'cart.html')


def sign_up_by_django(request):
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            # Проверяем, совпадают ли пароли и возраст
            if password == repeat_password and age >= 18:
                # Проверяем, существует ли покупатель с таким именем пользователя
                if not Buyer.objects.filter(username=username).exists():
                    # Хешируем пароль перед сохранением
                    hashed_password = make_password(password)
                    # Создаем нового покупателя
                    Buyer.objects.create(username=username, password=hashed_password, age=age)
                    return render(request, 'registration_page.html',
                                  {'message': f'Приветствуем, {username}!', 'form': UserRegister()})
                else:
                    info['error'] = 'Пользователь с таким именем уже существует.'
            else:
                info['error'] = 'Пароли не совпадают или возраст меньше 18.'
    else:
        form = UserRegister()

    return render(request, 'registration_page.html', {'form': form, 'info': info})


def sign_up_by_html(request):
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            # Проверяем, существует ли пользователь с таким именем
            if password == repeat_password and age >= 18:
                if not Buyer.objects.filter(username=username).exists():  # Проверяем на существование
                    # Создаем нового пользователя
                    Buyer.objects.create(username=username, password=password, age=age)  # Добавьте остальные поля
                    return render(request, 'fifth_task/registration_page.html',
                                  {'message': f'Приветствуем, {username}!', 'form': UserRegister()})
                else:
                    info['error'] = 'Пользователь с таким именем уже существует.'
            else:
                info['error'] = 'Пароли не совпадают или возраст меньше 18.'
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form, 'info': info})
