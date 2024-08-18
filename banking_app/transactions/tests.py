from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from decimal import Decimal

class TransactionTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass', balance=0)

    def test_deposit(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('deposit'), {'amount': '100.00'})
        self.user.refresh_from_db()
        self.assertEqual(self.user.balance, Decimal('100.00'))

    def test_withdraw_insufficient_funds(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('withdraw'), {'amount': '50.00'})
        self.assertContains(response, "Insufficient balance.")
