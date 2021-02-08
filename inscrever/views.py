from django.shortcuts import render
from sendmail.settings import EMAIL_HOST_USER
from .forms import Inscrever
from django.core.mail import send_mail


def inscrever(request):
    sub = Inscrever()
    if request.method == 'POST':
        sub = Inscrever(request.POST)
        assunto = 'Bem-vindo a RemakeTech'
        mensagem = 'Espero que aprenda com esse tutorial'
        recebedor = str(sub['email'].value())

        send_mail(assunto, mensagem, EMAIL_HOST_USER, [recebedor], fail_silently=False)
        return render(request, 'sucesso.html', {'recebedor': recebedor})
    return render(request, 'index.html', {'form': sub})

