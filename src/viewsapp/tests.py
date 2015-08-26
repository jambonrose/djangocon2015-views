from model_mommy import mommy
from test_plus import TestCase

from .models import ExampleModel


class ViewTests(TestCase):

    def test_model_detail(self):
        example_obj = mommy.make(ExampleModel)
        response = self.get_check_200(
            'model_detail',
            slug=example_obj.slug)
        self.assertContext('object', example_obj)
        self.assertTemplateUsed(response, 'viewsapp/detail.html')

    def test_model_detail_post(self):
        example_obj = mommy.make(ExampleModel)
        response = self.post(
            'model_detail',
            slug=example_obj.slug,
            data={})
        self.assertEqual(response.status_code, 405)

    def test_model_create_get(self):
        self.get_check_200('model_create')
        self.assertInContext('form')

    def test_model_create_put(self):
        response = self.client.put(
            self.reverse('model_create'),
            follow=True,
            data={
                'name': 'django',
                'slug': 'django',
            })
        self.assertEqual(response.status_code, 405)

    def test_model_create_post(self):
        self.post(
            'model_create',
            follow=True,
            data={
                'name': 'djangocon',
                'slug': 'djangocon',
            })
        self.assertRedirects(
            self.last_response,
            self.reverse(
                'model_detail',
                slug='djangocon'))
