from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    
    send_mail('Merhaba',
    'Merhaba, bu otomatik mesaj',
    'senin@postadresin.com',
    ['coyito@directmail24.net'], # https://temp-mail.org/tr/ den alacağın deneme adres
    fail_silently=False
    )
    return render(request, 'send/index.html')