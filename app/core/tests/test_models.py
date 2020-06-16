from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@marsimon.com', password='testing123'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_success(self):
        """Tests if user creation with email is successful"""
        email = 'test@marsimon.com'
        password = 'testpassword123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Tests if the email for a new user is normalized"""
        email = 'Test@MARSIMON.COM'
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, 'Test@marsimon.com')

    def test_new_user_invalid_email(self):
        """Tests if creating user with no email raises an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Tests creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@marsimon.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
        
    def test_ingredient_str(self):
        """Test the ingredient representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)