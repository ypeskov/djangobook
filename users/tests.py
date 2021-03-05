from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='will',
            email='will@example.com',
            password='qwerty'
        )
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superadmin(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@example.com',
            password='qwerty'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@example.com')
        self.assertTrue(admin_user.is_superuser)
