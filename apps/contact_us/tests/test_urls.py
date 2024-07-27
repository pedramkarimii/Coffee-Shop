from django.test import TestCase


class ContactUsURLTest(TestCase):
    def test_contact_us_urls(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        response = self.client.get("/thank-you/")
        self.assertEqual(response.status_code, 302)  # Ensure redirection
