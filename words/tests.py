from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.authtoken.models import Token

from words import apiviews


class TestLanguage(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = apiviews.LanguageList.as_view()
        self.uri = 'languages/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            'test',
            email='test@test.com',
            password='test')

    def test_language_list_status_code(self):
        request = self.factory.get(self.uri,
                                   HTTP_AUTHORIZATION=f'Token {self.token.key}'
                                   )
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
