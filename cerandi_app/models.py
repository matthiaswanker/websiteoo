import sys
from django.db import models
from django.core.urlresolvers import reverse

class Client(models.Model):
    first_name = models.CharField(max_length=255, blank=False)
    watchlist = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    user_name = models.CharField(max_length=255, blank=True)
    moral_ratio = models.IntegerField(default=0)
    risk_ratio = models.IntegerField(default=0)
    plz_location =  models.CharField(max_length=255, blank=True)


    def __unicode__(self):
            return u'%s'  % self.first_name


class Bank(models.Model):
    bank_name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    logo_url = models.CharField(max_length=255, blank=False)

    def __unicode__(self):
        return self.bank_name


class Advisor(models.Model):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    user_name = models.CharField(max_length=255, blank=False)
    bank = models.ForeignKey(Bank)
    plz_location =  models.CharField(max_length=255, blank=True)
    friend_score = models.CharField(max_length=255, blank=True)
    past_performance = models.CharField(max_length=255, blank=True)
#
    def __unicode__(self):
        return self.user_name
#
#     class Admin:
#         pass
#
#
class Stock(models.Model):
    sap_id = models.CharField(max_length=255, blank=True)
    wkn = models.CharField(max_length=255, blank=True)
    ticker = models.CharField(max_length=255, blank=True)
    ticker_name = models.CharField(max_length=255, blank=True)
    sector_id = models.CharField(max_length=255, blank=True)
    sector = models.CharField(max_length=255, blank=True)
    industry = models.CharField(max_length=255, blank=True)
    index_id = models.CharField(max_length=255, blank=True)
    index = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    logo_url = models.CharField(max_length=255, blank=True)
    chart_url = models.CharField(max_length=255, blank=True)
    service_url = models.CharField(max_length=255, blank=True)
    stock_return = models.CharField(max_length=255, blank=True)
    stock_risk = models.CharField(max_length=255, blank=True)
    stock_innovation = models.CharField(max_length=255, blank=True)
    stock_innovation_text = models.CharField(max_length=255, blank=True)
    stock_sustainability = models.CharField(max_length=255, blank=True)
    stock_sustainability_text = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.ticker_name

class Investment(models.Model):
    client = models.ForeignKey(Client)
    stock = models.ForeignKey(Stock)
    weight = models.FloatField(default=0.0)

class Message(models.Model):
    text = models.TextField(blank=True)
    client = models.ForeignKey(Client)
    advisor = models.ForeignKey(Advisor)
    author = models.BooleanField() #false: client, true: advisor
    send_date = models.DateTimeField()

class Match(models.Model):
    client = models.OneToOneField(Client)
    advisor = models.OneToOneField(Advisor)
