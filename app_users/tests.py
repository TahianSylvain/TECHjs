from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class UserViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('account:register')
        self.login_url = reverse('account:login')
        self.logout_url = reverse('account:logout')
        self.switch_user_url = reverse('account:switch_user')
        self.test_username = 'testuser'
        self.test_password = 'testpassword'
        self.test_email = 'test@example.com'

    def test_register_view(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_users/sign_up.html')

        data = {
            'username': self.test_username,
            'email': self.test_email,
            'password1': self.test_password,
            'password2': self.test_password,
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_users/sign_up.html')
        self.assertContains(response, 'Account is deactivated!', count=0)
        self.assertContains(response, 'Please, Use correct name or password!', count=0)

        user = User.objects.get(username=self.test_username)
        self.assertEqual(user.username, self.test_username)
        self.assertEqual(user.email, self.test_email)
        self.assertTrue(user.check_password(self.test_password))

    def test_login_view(self):
        User.objects.create_user(username=self.test_username, password=self.test_password)
        data = {
            'username': self.test_username,
            'password': self.test_password,
        }

        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_users/log_in.html')

        response = self.client.post(self.login_url, data)
        self.assertRedirects(response, reverse('main:entry'))

    def test_logout_view(self):
        self.client.login(username=self.test_username, password=self.test_password)
        response = self.client.get(self.logout_url)
        self.assertRedirects(response, reverse('main:entry'))

    def test_switch_user_view(self):
        self.client.login(username=self.test_username, password=self.test_password)
        response = self.client.get(self.switch_user_url)
        self.assertRedirects(response, reverse('account:login'))
