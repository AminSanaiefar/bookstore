from django.test import TestCase
from django.urls import reverse


class HomePageTest(TestCase):
    def test_home_page_by_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_by_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # test if in showed template Home Page Is showing --->
    def test_home_page_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Home Page')

    # test if the correct template is using for home page
    def test_home_page_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
