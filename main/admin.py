from django.contrib import admin
from .models import Account

class AccountsAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'date_of_login']

admin.site.register(Account, AccountsAdmin)