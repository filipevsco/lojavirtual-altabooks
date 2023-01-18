from django.test import TestCase


class TestarPaginas(TestCase):
    def testar_se_pagina_principal_carrega_completamente(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertContains(response, 'Loja Virtual')