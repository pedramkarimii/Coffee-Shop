from django.test import TestCase
from contact_us.forms import ContactForm


class ContactFormTest(TestCase):
    def test_contact_form_valid(self):
        form_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "subject": "Test Subject",
            "message": "Test Message",
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())
