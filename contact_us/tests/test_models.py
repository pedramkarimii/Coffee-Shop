from django.test import TestCase
from contact_us.models import ContactMessage


class ContactMessageModelTest(TestCase):
    def test_contact_message_creation(self):
        contact_message = ContactMessage.objects.create(
            name="John Doe",
            email="john@example.com",
            subject="Test Subject",
            message="Test Message",
        )
        self.assertEqual(contact_message.name, "John Doe")
        self.assertEqual(contact_message.email, "john@example.com")
        self.assertEqual(contact_message.subject, "Test Subject")
        self.assertEqual(contact_message.message, "Test Message")
