# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import numpy as np

class MarketApp(models.Model):
    name=models.CharField(max_length=200)

    def average_rating(self):
        all_ratings=map(lambda x: x.ratings ,self.review_set.all())
        return np.mean(all_ratings)

    def __unicode__(self):
        return self.name


class Review(models.Model):
    RATING_CHOICES=(
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    marketapp = models.ForeignKey(MarketApp)
    pub_date=models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    ratings=models.IntegerField(choices = RATING_CHOICES)

class Cluster(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)

    def get_members(self):
        return "\n".join([u.username for u in self.users.all()])

# Create your models here.
