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
