from django.test import TestCase
from snippets.models import Snippet
from snippets.serializers import SnippetSerializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# Create your tests here.
class TestCreate(TestCase):

    Snippet(code='foo="bar"\n').save


class TestUpdate(TestCase):
    pass