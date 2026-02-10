from django.test import TestCase

from contents.models import Post


class TestPost(TestCase):
    def test_sample(self):
        self.assertEqual(1, 1, "SIMPLE TEST")

    def setUp(self):
        Post.objects.create(title="111")
        Post.objects.create(title="222")

    def test_posts_count(self):
        # self._create_post()
        self.assertEqual(Post.objects.all().count(), 2)

    def test_posts_count_2(self):
        # self._create_post()
        Post.objects.create(title="333")
        self.assertEqual(Post.objects.count(), 3)
