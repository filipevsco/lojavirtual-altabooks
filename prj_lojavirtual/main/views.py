from django.views.generic.edit import FormView
from main import forms


class ViewFaleConosco(FormView):
    template_name = "fale_conosco.html"
    form_class = forms.FormFaleConosco
    success_url = "/"
