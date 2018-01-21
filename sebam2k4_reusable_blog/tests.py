# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import Post
# Create your tests here.

# For testing model or function accessing db inherit from django.test.TestCase
# Otherwise inherit from unittest.TestCase

class PostTests(TestCase):
  '''
  Define the tests
  that will run against Post mdoel
  '''

  def test_str(self):
    '''
    Intantiate Post class and initialize its title
    and check if it equals to specified title with .assertEqual
    '''
    test_title = Post(title='My Latest Blog Post')
    self.assertEqual(str(test_title), 'My Latest Blog Post')
