from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout

from .forms import UserRegistrationForm, TransactionForm
from .models import User, Transaction


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Создаем юзера но пока не сохраняем
            new_user = user_form.save(commit=False)
            # ставим пароль
            new_user.set_password(user_form.cleaned_data['password'])
            # сохраняем
            new_user.save()
            return render(request, 'accounts/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'accounts/create_account.html', {'user_form': user_form})


def sign_in(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
    else:
        form = AuthenticationForm()
        return render(request, "accounts/sign_in.html", {"form": form})


def logout_view(request):
    # Выход по нажатию кнопки выход :)
    logout(request)
    return redirect("/")


# def index(request):
#     return render(request, 'core.html',)


def show_history(request):
    history = Transaction.objects.filter(sender=request.user)
    return render(request, "core.html", {'history': history})


def money_transfer(request):
    if request.method == "POST":
        form = TransactionForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # user = admin
            cur_user = post.user
            phone = request.POST.get('phone')  # достает телефон
            count = request.POST.get('count')  # достает кол-во
            user = User.objects.get(phone=phone)  # user = sleepy
            rec_user = user
            if cur_user.balance < int(count):
                raise ValueError('У вас недостаточно средств на балансе')
            else:
                cur_user.balance = cur_user.balance - int(count)
                rec_user.balance = rec_user.balance + int(count)
                trans = Transaction()
                trans.recipient = rec_user
                trans.sender = cur_user
                trans.count = int(count)
                trans.save()
                cur_user.save()
                rec_user.save()

                return redirect("/")
    else:
        form = TransactionForm()

    history = Transaction.objects.filter(sender=request.user)
    context = {'form':form, 'history':history}
    return render(request, "core.html", context)
