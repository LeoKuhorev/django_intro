from django.test import SimpleTestCase
from django.urls import reverse


class TestAbout(SimpleTestCase):

    def test_about_page_status_check(self):
        url = reverse('about:about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_template(self):
        url = reverse('about:about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'about/about.html')
