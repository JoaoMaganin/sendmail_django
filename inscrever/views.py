from django.shortcuts import render
from sendmail.settings import EMAIL_HOST_USER  # Host que envia o email
from .forms import Inscrever  # formulário importado
from django.core.mail import send_mail  # send_mail = função responsável por enviar emails


def inscrever(request):
    sub = Inscrever()  # Variável que recebe o formulário
    if request.method == 'POST':  # Se for método https for post, enviará o email
        sub = Inscrever(request.POST)
        assunto = 'Bem-vindo a RemakeTech'
        mensagem = 'Espero que aprenda com esse tutorial'
        recebedor = str(sub['email'].value())  # Pega o email inserido la em forms.py

        send_mail(assunto, mensagem, EMAIL_HOST_USER, [recebedor], fail_silently=False)  # Envia o email com as
        # informações acima
        return render(request, 'sucesso.html', {'recebedor': recebedor})  # renderiza o template sucesso.html e o
        # recebedor junto
    return render(request, 'index.html', {'form': sub})  # Caso haja erro, recarrega a página index.html
