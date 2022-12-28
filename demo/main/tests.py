from django.test import TestCase
from demo.settings import env

class SimpleTest(TestCase):
    def test_secret_1(self):
        """
        Tests enviroments variables stored in .env
        """

        text = env('ULTRA_SECRET_TOKEN')
        expected = 'Im just a simple token'

        self.assertEqual(text, expected)

    def test_secret_2(self):
        """
        Tests enviroments variables stored in .env
        """

        text = env('supersecurestring')
        expected = 'Ihavemanynumber8475039428745092387502938750293875029387529375923875092387592384750'

        self.assertEqual(text, expected)