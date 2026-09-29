from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase


class AuthenticationTests(APITestCase):
    def test_registration_hashes_password_and_returns_usable_token(self):
        response = self.client.post('/api/auth/register/', {
            'username': 'portfolio_student',
            'password': 'local-test-password-284!',
        }, format='json')
        self.assertEqual(response.status_code, 201, response.data)
        user = get_user_model().objects.get(username='portfolio_student')
        self.assertTrue(user.check_password('local-test-password-284!'))
        self.assertEqual(user.role, 'student')
        self.assertNotIn('password', response.data['user'])
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.data['access'])
        profile = self.client.get('/api/auth/me/')
        self.assertEqual(profile.status_code, 200)
        self.assertEqual(profile.data['username'], user.username)

    def test_profile_requires_authentication(self):
        response = self.client.get('/api/auth/me/')
        self.assertIn(response.status_code, (401, 403))

    def test_invalid_login_does_not_issue_tokens(self):
        get_user_model().objects.create_user(username='student', password='valid-test-password-284!')
        response = self.client.post('/api/auth/token/', {
            'username': 'student', 'password': 'wrong-password',
        }, format='json')
        self.assertEqual(response.status_code, 401)
        self.assertNotIn('access', response.data)

    def test_anonymous_user_cannot_create_subject(self):
        response = self.client.post('/api/subjects/', {'name': 'Example'}, format='json')
        self.assertIn(response.status_code, (401, 403))
