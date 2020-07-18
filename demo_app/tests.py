from django.test import SimpleTestCase
from django.urls import reverse


class Testhome(SimpleTestCase):

    def test_home_page_status_check(self):
        url = reverse('demo:welcome')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_template(self):
        url = reverse('demo:welcome')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'demo_app/welcome.html')
