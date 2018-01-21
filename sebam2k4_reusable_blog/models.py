# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.

class Post(models.Model):
  '''
  Post model definithions
  '''

  # author is linked to a registered user, via the User model (table) in the auth app.
  author = models.ForeignKey(settings.AUTH_USER_MODEL)
  title = models.CharField(max_length=200)
  content = models.TextField()
  # identify when post was created
  created_date = models.DateTimeField(auto_now_add=True)
  # set publish date initially to blank and null as drafts are allowed
  published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
  # record how ofter a post is seen
  views = models.IntegerField(default=0)
  # tags field
  tag = models.CharField(max_length=30, blank=True, null=True)
  # add images to a post #stores relative path to image
  image = models.ImageField(upload_to="images", blank=True, null=True)

  def publish(self):
    '''update publish date in db when post is published'''
    self.published_date = timezone.now()
    self.save()

  def __unicode__(self):
    ''' identify blog entries by their title for admin page'''
    return self.title

