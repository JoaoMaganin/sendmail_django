from django.shortcuts import render
from sendmail.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail


def inscrever(request):
    sub = forms.Inscrever()
    if request.method == 'POST':
        sub = forms.Inscrever(request.POST)
        assunto = 'Bem vindo ao RemakeTech'
        mensagem = 'Espero que esteja aproveitando esse tutorial'
        recebedor = str(sub['email'].value())

        send_mail(assunto, mensagem, EMAIL_HOST_USER, [recebedor], fail_silently=False)
        return render(request, 'sucesso.html', {'recebedor': recebedor})
    return render(request, 'index.html', {'form': sub})
