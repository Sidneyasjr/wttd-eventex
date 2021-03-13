from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Sidney Andrade',
            cpf='12345678901',
            email='sidney.jwnior@gmail.com',
            phone='47-99115-8947'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must jave an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Sidney Andrade', str(self.obj))

    def test_paid_default_to_false(self):
        """By default paid must be False."""
        self.assertEqual(False, self.obj.paid)
