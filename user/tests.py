from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

class UserAccountTests(TestCase):

    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            'first_name', 'last_name', 'username', 'ward_name', 'password'
        )
        self.assertEqual(super_user.first_name, 'first_name')
        self.assertEqual(super_user.last_name, 'last_name')
        self.assertEqual(super_user.ward_name, 'ward_name')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), "username")

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                first_name = 'first_name', last_name= 'last_name', username='username', ward_name='ward_name', password='password', is_superuser=False
            )
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                first_name = 'first_name', last_name= 'last_name', username='username', ward_name='ward_name', password='password', is_staff=False
            )
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                first_name = '', last_name= 'last_name', username='username', ward_name='ward_name', password='password', is_staff=False
            )

    def test_new_user(self):
        db = get_user_model() 
        user = db.objects.create_user(
                'first_name', 'last_name', 'username', 'ward_name', 'password'
            )
        self.assertEqual(user.username, 'username')
        self.assertEqual(user.first_name, 'first_name')
        self.assertEqual(user.last_name, 'last_name')
        self.assertEqual(user.ward_name, 'ward_name')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)

        with self.assertRaises(ValueError):
            db.objects.create_user(
                first_name = '', last_name= 'a', username='a', ward_name='a', password='password'
            )
        with self.assertRaises(ValueError):
            db.objects.create_user(
                first_name = 'a', last_name= '', username='a', ward_name='a', password='password'
            )
        with self.assertRaises(ValueError):
            db.objects.create_user(
                first_name = 'a', last_name= 'a', username='a', ward_name='', password='password'
            )
        with self.assertRaises(ValueError):
            db.objects.create_user(
                first_name = '', last_name= '', username='', ward_name='', password='password'
            )