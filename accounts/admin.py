from django.contrib import admin

from accounts.models import User, Transaction

admin.site.register(User)
admin.site.register(Transaction)
