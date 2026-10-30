from django.test import SimpleTestCase
from django.urls import reverse


class HomeViewTests(SimpleTestCase):
    def test_home_page_returns_welcome_message(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "<h1>Hello, World! Welcome to my Django application!</h1>",
        )


class AboutViewTests(SimpleTestCase):
    def test_about_page_returns_about_heading(self):
        response = self.client.get(reverse("about"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h1>About Page</h1>")
