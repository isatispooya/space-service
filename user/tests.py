from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

class CaptchaViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_captcha(self):
        url = reverse('captcha')  # نام مسیر به ویو Captcha
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
