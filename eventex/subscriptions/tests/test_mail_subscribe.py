from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Sidney Andrade', cpf='12345678901', email='sidney.jwnior@gmail.com', phone='47-99115-8947')
        self.resp = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'sidney.jwnior@gmail.com'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['sidney.jwnior@gmail.com', 'sidney.jwnior@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Sidney Andrade',
            '12345678901',
            'sidney.jwnior@gmail.com',
            '47-99115-8947'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
