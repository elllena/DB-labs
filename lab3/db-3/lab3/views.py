# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.db import connection
import json
import MySQLdb

from lab3.models import *

def home(request):
    cursor = connection.cursor()
    return render(request, 'home.html')

def load(request):
    f = open('db2.json', 'r')
    json_string = f.read()
    parsed_string = json.loads(json_string)

    rows = Airline.objects.all()
    for row in rows:
        t = True
        for i in range(0, len(parsed_string["airline"])):
            if parsed_string["airline"][i]["id"] == row.id:
                t = False
        if t:
            Airline.objects.get(id = row.id).delete()
    rows = Airline.objects.all()
    for i in range(0,len(parsed_string["airline"])):
        t = False
        for row in rows:
            if parsed_string["airline"][i]["id"] == row.id:
                t = True
        if t:
            buff = Airline.objects.get(id = parsed_string["airline"][i]["id"])
            buff.name = parsed_string["airline"][i]["name"]
            buff.rank = parsed_string["airline"][i]["rank"]
            buff.home = parsed_string["airline"][i]["home"]
            buff.save()
        else:
            buff = Airline(
                id = parsed_string["airline"][i]["id"],
                name = parsed_string["airline"][i]["name"],
                rank = parsed_string["airline"][i]["rank"],
                home = parsed_string["airline"][i]["home"]
            )
            buff.save()

    rows = Client.objects.all()
    for row in rows:
        t = True
        for i in range(0, len(parsed_string["client"])):
            if parsed_string["client"][i]["id"] == row.id:
                t = False
        if t:
            Client.objects.get(id=row.id).delete()
    rows = Client.objects.all()
    for i in range(0, len(parsed_string["client"])):
        t = False
        for row in rows:
            if parsed_string["client"][i]["id"] == row.id:
                t = True
        if t:
            buff = Client.objects.get(id=parsed_string["client"][i]["id"])
            buff.name = parsed_string["client"][i]["name"]
            buff.age = parsed_string["client"][i]["age"]
            buff.home = parsed_string["client"][i]["home"]
            buff.comment = parsed_string["client"][i]["comment"]
            buff.vip = parsed_string["client"][i]["vip"]
            buff.save()
        else:
            buff = Client(
                id=parsed_string["client"][i]["id"],
                name = parsed_string["client"][i]["name"],
                age = parsed_string["client"][i]["age"],
                home = parsed_string["client"][i]["home"],
                comment = parsed_string["client"][i]["comment"],
                vip = parsed_string["client"][i]["vip"]
            )
            buff.save()

    rows = Card.objects.all()
    for row in rows:
        t = True
        for i in range(0, len(parsed_string["card"])):
            if parsed_string["card"][i]["id"] == row.id:
                t = False
        if t:
            Card.objects.get(id=row.id).delete()
    rows = Card.objects.all()
    for i in range(0, len(parsed_string["card"])):
        t = False
        for row in rows:
            if parsed_string["card"][i]["id"] == row.id:
                t = True
        if t:
            buff = Card.objects.get(id=parsed_string["card"][i]["id"])
            buff.card = parsed_string["card"][i]["rank"]
            buff.bank_name = parsed_string["card"][i]["bank_name"]
            buff.card_limit = parsed_string["card"][i]["card_limit"]
            buff.save()
        else:
            buff = Card(
                id=parsed_string["card"][i]["id"],
                rank=parsed_string["card"][i]["rank"],
                bank_name=parsed_string["card"][i]["bank_name"],
                card_limit=parsed_string["card"][i]["card_limit"]
            )
            buff.save()

    rows = Ticket.objects.all()
    for row in rows:
        t = True
        for i in range(0, len(parsed_string["ticket"])):
            if parsed_string["ticket"][i]["id"] == row.id:
                t = False
        if t:
            Ticket.objects.get(id=row.id).delete()
    rows = Ticket.objects.all()
    for i in range(0, len(parsed_string["ticket"])):
        t = False
        for row in rows:
            if parsed_string["ticket"][i]["id"] == row.id:
                t = True
        if t:
            buff = Ticket.objects.get(id=parsed_string["ticket"][i]["id"])
            buff.date = parsed_string["ticket"][i]["date"]
            buff.from_city = parsed_string["ticket"][i]["from_city"]
            buff.to_city = parsed_string["ticket"][i]["to_city"]
            buff.cost = parsed_string["ticket"][i]["cost"]
        else:
            buff = Ticket(
                id=parsed_string["ticket"][i]["id"],
                date=parsed_string["ticket"][i]["date"],
                from_city=parsed_string["ticket"][i]["from_city"],
                to_city=parsed_string["ticket"][i]["to_city"],
                cost=parsed_string["ticket"][i]["cost"]
            )
            buff.save()
    return redirect('/show/')


def show_main(request):
    if request.method == "GET":
        mann = Main.objects.all()
        rows = []
        for ma in mann:
            rows.append([ma.id, ma.client.name, ma.card.bank_name, ma.airline.name, ma.ticket.date, ma.ticket.from_city,
                         ma.ticket.to_city, ma.client.vip, ma.paid, ma.client.comment])

    return render(request,'Main_show.html',locals())
def show_date(request):
    if request.method == "POST":
        date1 = request.POST['from']
        date2 = request.POST['to']
        vip = request.POST['vip']

        mann = Main.objects.filter(ticket__date__gte = date1, client__vip = int(vip)).exclude(ticket__date__gte = date2).order_by('id')

        rows = []
        for ma in mann:
            rows.append([ma.id, ma.client.name, ma.card.bank_name, ma.airline.name, ma.ticket.date, ma.ticket.from_city,
                         ma.ticket.to_city, ma.client.vip, ma.paid, ma.client.comment])
    return render(request,'Main_show.html',locals())
def show_text(request):
    if request.method == "POST":
        text1 = request.POST['text1']
        text2 = request.POST['text2']

        mann = Main.objects.filter(client__comment__contains=text2).exclude(client__comment__contains = text1).order_by('id')

        rows = []
        for ma in mann:
            rows.append([ma.id, ma.client.name, ma.card.bank_name, ma.airline.name, ma.ticket.date, ma.ticket.from_city,
                         ma.ticket.to_city, ma.client.vip, ma.paid, ma.client.comment])
    return render(request,'Main_show.html',locals())
def search(request):
    return render(request,'search.html',locals())
def show(request):
    if request.method == "GET":
        tick = Ticket.objects.all()
        tickets = []
        for a in tick:
            tickets.append([a.id,a.date,a.from_city,a.to_city,a.cost])

        cli = Client.objects.all()
        clients = []
        for a in cli:
            clients.append([a.id,a.name,a.age,a.home,a.comment,a.vip])

        car = Card.objects.all()
        cards = []
        for a in car:
            cards.append([a.id,a.card_limit,a.rank,a.bank_name])

        air = Airline.objects.all()
        airlines = []
        for a in air:
            airlines.append([a.id,a.name,a.rank,a.home])
    return render(request,'2show.html',locals())
def add(request):
    db = MySQLdb.connect(host="localhost", user="root", passwd="1111", db="mydb")
    cur = db.cursor()
    if request.method == "POST":
        row = Main(client = Client.objects.get(id = int(request.POST['client_id'])),
        card = Card.objects.get(id = int(request.POST['card_id'])),
        airline = Airline.objects.get(id = int(request.POST['airline_id'])),
        ticket = Ticket.objects.get(id = int(request.POST['ticket_id'])),
        paid = int(request.POST['paid']))
        row.save()
        return redirect('/main/')
    scli = 1
    scar = 1
    sair = 1
    stic = 1

    tick = Ticket.objects.all()
    tickets = []
    for a in tick:
        tickets.append([a.id, a.date, a.from_city, a.to_city, a.cost])

    cli = Client.objects.all()
    clients = []
    for a in cli:
        clients.append([a.id, a.name, a.vip])

    car = Card.objects.all()
    cards = []
    for a in car:
        cards.append([a.id, a.bank_name, a.card_limit])

    air = Airline.objects.all()
    airlines = []
    for a in air:
        airlines.append([a.id, a.name])
    space = ' / '
    return render(request,'add.html',locals())

def delete(request):
    mid = int(request.POST['row_id'])
    p = Main.objects.get(id = mid)
    p.delete()
    return redirect('/main/')

def edit(request):
    if request.POST['row_im'] == "0":
        id = request.POST['row_id']
        row = Main.objects.get(id = int(id))
        row.client = Client.objects.get(id = int(request.POST['client_id']))
        row.card = Card.objects.get(id = int(request.POST['card_id']))
        row.airline = Airline.objects.get(id = int(request.POST['airline_id']))
        row.ticket = Ticket.objects.get(id = int(request.POST['ticket_id']))
        row.paid = int(request.POST['paid'])
        row.save()
        return redirect('/main/')

    id = request.POST['row_id']
    row = Main.objects.get(id = int(id))
    row_id = row.id
    scli = row.client.id
    scar = row.card.id
    sair = row.airline.id
    stic = row.ticket.id
    pay = row.paid

    tick = Ticket.objects.all()
    tickets = []
    for a in tick:
        tickets.append([a.id, a.date, a.from_city, a.to_city, a.cost])

    cli = Client.objects.all()
    clients = []
    for a in cli:
        clients.append([a.id, a.name, a.vip])

    car = Card.objects.all()
    cards = []
    for a in car:
        cards.append([a.id, a.bank_name, a.card_limit])

    air = Airline.objects.all()
    airlines = []
    for a in air:
        airlines.append([a.id, a.name])
    space = ' / '
    return render(request,'edit.html',locals())

def plus(request):
    if request.method == "GET":
        buff = Mypoint.objects.get(id = 1)
        schedule=buff.point
        buff = Mypoint.objects.get(id = 0)
        triger=buff.point
        return render(request,'plus.html',locals())

    db = MySQLdb.connect(host="localhost", user="root", passwd="1111", db="mydb")
    cur = db.cursor()

    schedule = request.POST['schedule']
    if schedule == '0':
        buff = Mypoint.objects.get(id = 1)
        buff.point = 0
        buff.save()
        week = request.POST['week']
#        sql = "DROP EVENT IF EXISTS my_event;"
#        cur.execute(sql)
#        db.commit()
#        db.close()
    else:
        buff = Mypoint.objects.get(id = 1)
        buff.point = 1
        buff.save()
#        week = request.POST['week']
#        sql = "DELIMITER $$ ; DROP EVENT IF EXISTS my_event$$ CREATE EVENT `my_event` " \
#          "ON SCHEDULE EVERY %d WEEK STARTS CURRENT_TIMESTAMP ON COMPLETION NOT PRESERVE ENABLE COMMENT ''  " \
#          "DO call my_proc(); $$ DELIMITER ; $$ " % (int(week))

         #or ALTER EVENT 'my_event' ON SCHEDULE EVERY %d WEEK;

#        cur.execute(sql)
#        db.commit()
#        db.close()

    buff = Mypoint.objects.get(id=1)
    schedule = buff.point
    buff = Mypoint.objects.get(id=0)
    triger = buff.point
    return render(request,'plus.html',locals())