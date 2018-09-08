from django.test import TestCase

class TestTreatmentViews(TestCase):

    def test_treatments_view(self):
        page = self.client.get("/home/treatments/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "treatments.html")