from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework import APIClient

CREATE_USER_URL = reverse('user:create')

def create_user(**params):
    return get_user_model().objects.create_user(**params)

class UserCreateApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        data =  {
            'email': 'user@example.com',
            'password': 'testpassword',
            'name': 'Tester',
        }
        res = self.client.post(CREATE_USER_URL, data=data)
        assert res.status_code == 201
        user = get_user_model().objects.get(email=data['email'])
        self.assertTrue(user.check_passwort(data['password']))
        assert 'passowrd' not in res.content

    def test_user_with_email_exist_error(self):
        """Test that user_with_email_exist_error"""
        data = {
            "email": 'user@example.com',
            "password": 'testpassword2',
            "name": 'Tester2',
        }

        create_user(**data)
        res = self.client.post(CREATE_USER_URL, data=data)
        assert res.status_code == 400
        assert 'email' in res.json()['detail']

    def test_password_too_short(self):
        "Test if the password is too short"
        data = {
            "email": 'user@example.com',
            "password": 'pw',
            "name": 'Tester3',
        }
        res = self.client.post(CREATE_USER_URL, data=data)
        assert res.status_code == 400
        user_exist = get_user_model().objects.filter(
            email=data['email']
        ).exist()
        self.assertFalse(user_exist)
