import sys
from django.db import models
from django.core.urlresolvers import reverse

class Client(models.Model):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    user_name = models.CharField(max_length=255, blank=False)
    moral_ratio = models.IntegerField(default=0)
    risk_ratio = models.IntegerField(default=0)
#     GENDER_TYPES = (("m","m"),("w","w"))
#     gender		= models.CharField(max_length=200, choices=GENDER_TYPES, default='m')
#
#     class Meta:
#         ordering = ('user_name',)
#
#     def get_absolute_url(self):
#         return reverse('statement_detail', kwargs={'url':self.url})
#
#     def __unicode__(self):
#             return u'%s'  % self.url
#
#
class Bank(models.Model):
    bank_name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    logo_url = models.CharField(max_length=255, blank=False)
#
    def __unicode__(self):
        return self.bank_name
#
#     class Admin:
#         pass
#
class Advisor(models.Model):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    user_name = models.CharField(max_length=255, blank=False)
    bank = models.ForeignKey(Bank)
#
    def __unicode__(self):
        return self.user_name
#
#     class Admin:
#         pass
#
#
class Stock(models.Model):
    ticker = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
#
#     def __unicode__(self):
#         return self.ticker
#
#     class Admin:
#         pass
#
#
class Investment(models.Model):
    client = models.OneToOneField(Client)
    stock = models.OneToOneField(Stock)
#
#
