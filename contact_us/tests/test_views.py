from django.test import TestCase
from django.urls import reverse


class ContactUsViewTest(TestCase):
    def test_contact_form_view(self):
        response = self.client.get(reverse("contact_form"))
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed
