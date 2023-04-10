from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status


class CursoTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso = 'CTT1', descricao = 'Curso Teste 1', nivel = 'B'
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso = 'CTT2', descricao = 'Curso Teste 2', nivel = 'A'
        )        
    
    # def test_falhador(self):
    #     self.fail('Teste falhou de propósito, não se preocupe')

    def test_requisicao_get_para_listar_cursos(self):
        '''Teste para verificar a requisição GET para listar os Cursos'''
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_curso(self):
        '''Teste para verificar a requisição POST para criar curso'''
        data = {
            'codigo_curso':'CTT3',
            'descricao':'Curso Teste 3',
            'nivel':'I',
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
    
    def test_requisicao_delete_para_apagar_curso(self):
        """Teste para verificar a requisição delete NÃO permitida"""
        response = self.client.delete('/cursos/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_requisicao_put_para_atualizar_curso(self):
        """Testa para verificar a requisição PUT para atualização de cursos"""
        data = {
            'codigo_curso':'CTT1',
            'descricao':'Curso Teste 1 - Atualizado',
            'nivel':'I',
        }
        response = self.client.put('/cursos/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)