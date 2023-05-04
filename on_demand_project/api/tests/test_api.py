from rest_framework.test import APITestCase
from rest_framework import status


class AuthAPITestCase(APITestCase):

    def setUp(self):
        self.user = self.client.post('/auth/users/', data={'username': 'superman', 'password': 'galya123'})
        response = self.client.post('/auth/jwt/create/', data={'username': 'superman', 'password': 'galya123'})
        self.access_token = response.data['access']
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.access_token)

    def test_get_users_me(self):
        response = self.client.get('/auth/users/me/')

        self.assertEqual({'email': '', 'id': 2, 'username': 'superman'}, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_patch_user_data(self):
        response = self.client.put('/auth/users/me/', data={'email': 'fig@someur.com'})
        self.assertEqual({'email': 'fig@someur.com', 'id': 3, 'username': 'superman'}, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_put_user_data(self):
        response = self.client.put('/auth/users/me/', data={'email': 'someurl@fig.com'})
        self.assertEqual({'email': 'someurl@fig.com', 'id': 4, 'username': 'superman'}, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_delete_user(self):
        response = self.client.delete('/auth/users/me/', data={'current_password': 'galya123'})
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)


