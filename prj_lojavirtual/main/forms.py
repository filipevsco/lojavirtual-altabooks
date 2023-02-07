from django import forms
from django.core.mail import send_mail
from lojavirtual import settings


class FormFaleConosco(forms.Form):
    nome = forms.CharField(required=True)
    email_origem = forms.EmailField(required=True, label= 'Entre com seu e-mail:')
    mensagem = forms.CharField(required=True, widget=forms.Textarea)

    def enviar_mensagem_por_email(self):
        send_mail(
            'FALE CONOSCO: Mensagem recebida.',
            self.data['mensagem'],
            self.data['email_origem'],
            [settings.EMAIL_FALE_CONOSCO],
            fail_silently=False
            )