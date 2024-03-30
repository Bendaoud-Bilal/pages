from django.test import TestCase

# pages/tests.py
from django.test import SimpleTestCase
from django.urls import reverse


# tests for the homepage
class HomepageTests(SimpleTestCase):

    # check return HTTP status codes of 200, the standard response for a successful HTTP request.
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    # tests whether the homepage is accessible (url) via its name, “home”.
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    # tests whether the correct template, “home.html”, is being used to render the homepage.
    def test_template_name_correct(self):  # new
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    #  tests whether the homepage contains the correct content
    # (contains the HTML tag “<h1>Homepage</h1>”)
    def test_template_content(self):  # new
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Homepage</h1>")


# tests for the about page
class AboutpageTests(SimpleTestCase):

    # check return HTTP status codes of 200, the standard response for a successful HTTP request.
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    # tests whether the aboutpage is accessible (url) via its name, “about”.
    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    # tests whether the correct template, “home.html”, is being used to render the aboutpage.
    def test_template_name_correct(self):  # new
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    #  tests whether the aboutpage contains the correct content
    # (contains the HTML tag “<h1>aboutpage</h1>”)
    def test_template_content(self):  #       new
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About page</h1>")
