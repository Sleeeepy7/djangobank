from django.contrib.auth.models import AbstractUser
from django.db import models
from phone_field import PhoneField
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.conf import settings


class User(AbstractUser):
    phone = PhoneField(blank=True, help_text='Contact phone number', unique=True)
    balance = models.IntegerField('Баланс пользователя', null=True, default=0)


class Transaction(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    count = models.DecimalField(default=0, max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Отправитель', related_name='sender')
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Получатель', related_name='recipient')



# def money_transfer(request):
#     if request.method == "POST":
#         form = TransactionForm(data=request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.user = request.user # user = admin
#             cur_user = post.user
#             phone = request.POST.get('phone') # достает телефон
#             print(phone)
#             count = request.POST.get('count') # достает кол-во
#             print(count)
#             user = User.objects.get(phone=phone) # user = sleepy
#             print(user)
#             rec_user = user
#             cur_user.balance = cur_user.balance - int(count)
#             print(cur_user.balance)
#             rec_user.balance = rec_user.balance + int(count)
#             print(rec_user.balance)
#             cur_user.save()
#             rec_user.save()
#             return redirect("/")
#
# def money_transfer(request):
#     if request.method == "POST":
#         form = TransactionForm(data=request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.user = request.user # user = admin
#             cur_user = post.user
#             phone = request.POST.get('phone') # достает телефон
#             count = request.POST.get('count') # достает кол-во
#             user = User.objects.get(phone=phone) # user = sleepy
#             rec_user = user
#             if cur_user.balance < int(count):
#                 raise ValueError('У вас недостаточно средств на балансе')
#             else:
#                 cur_user.balance = cur_user.balance - int(count)
#                 rec_user.balance = rec_user.balance + int(count)
#                 cur_user.save()
#                 rec_user.save()
#                 return redirect("/")
#     else:
#         form = TransactionForm()
#         return render(request, "core.html", {"form": form})
