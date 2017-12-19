# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Airline(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    rank = models.CharField(max_length=5, blank=True, null=True)
    home = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'airline'


class Card(models.Model):
    card_limit = models.IntegerField(blank=True, null=True)
    rank = models.CharField(max_length=5, blank=True, null=True)
    bank_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card'


class Client(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    home = models.CharField(max_length=20, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    vip = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Ticket(models.Model):
    date = models.DateField(blank=True, null=True)
    from_city = models.CharField(max_length=20, blank=True, null=True)
    to_city = models.CharField(max_length=20, blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket'

class Main(models.Model):
    paid = models.IntegerField(blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'main'

class Mypoint(models.Model):
    id = models.IntegerField(primary_key=True)
    point = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mypoint'
