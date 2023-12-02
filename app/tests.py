from django.test import TestCase, Client
from django.urls import reverse
from .models import PrankCall

class PrankCallTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_prank_call_success(self):
        response = self.client.post(reverse('make_call'), {'phone_number': '1234567890', 'prank_message': 'Hello!'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')
        self.assertTrue(PrankCall.objects.exists())

    def test_prank_call_failure(self):
        response = self.client.post(reverse('make_call'), {'phone_number': '', 'prank_message': ''})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['status'], 'error')
        self.assertFalse(PrankCall.objects.exists())