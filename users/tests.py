from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken

class UserTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(userName='testuser', password='testpassword')
        refresh = RefreshToken.for_user(self.user)
        self.refresh_token = str(refresh)
        self.access_token = str(refresh.access_token)

    def test_register_user(self):
        url = reverse('register')
        data = {
            'userName': 'testuser2',
            'password': 'testpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(userName='testuser2').userName, 'testuser2')

    def test_obtain_token(self):
        url = reverse('token_obtain_pair')
        data = {
            'userName': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_refresh_token(self):
        url = reverse('token_refresh')
        data = {
            'refresh': self.refresh_token
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_list_users(self):
        url = reverse('user-list')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Ajuste para verificar o número de usuários listados

    def test_get_user_detail(self):
        url = reverse('user-detail', args=[self.user.id])
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['userName'], 'testuser')

    def test_update_user(self):
        url = reverse('user-detail', args=[self.user.id])
        data = {
            'userName': 'updateduser',
            'password': 'newpassword'
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.userName, 'updateduser')

    def test_delete_user(self):
        url = reverse('user-detail', args=[self.user.id])
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)
