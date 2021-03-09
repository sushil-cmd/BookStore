from django.contrib.auth import  get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):

    def test_create_user(self):

        User = get_user_model()

        user = User.objects.create_user(
            username='test',
            email='test@test.com',
            password='testing321'
        )

        self.assertEqual(user.username, 'test')
        self.assertEquals(user.email, 'test@test.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@test.com',
            password='testing321'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@test.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
