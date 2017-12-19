from django.shortcuts import render, redirect

import json
import MySQLdb

def home(request):
    return render(request, 'home.html')

def load(request):
    db = MySQLdb.connect('localhost', 'root', '1111', 'mydb')
    f = open('db2.json', 'r')
    json_string = f.read()
    parsed_string = json.loads(json_string)

    cur = db.cursor()
    cur.execute("SELECT * FROM mydb.main")
    rows = cur.fetchall()
    for row in rows:
        t = True
        for i in range(0,len(parsed_string["airline"])):
            if parsed_string["airline"][i]["id"] == row[4]:
                t = False
        if t:
            cur.execute("DELETE FROM mydb.main WHERE `id`='%d'" %(row[0]))
            db.commit()
        else:
            t = True
            for i in range(0,len(parsed_string["card"])):
                if parsed_string["card"][i]["id"] == row[5]:
                    t = False
        if t:
            cur.execute("DELETE FROM mydb.main WHERE `id`='%d'" %(row[0]))
            db.commit()
        else:
            t = True
            for i in range(0, len(parsed_string["ticket"])):
                if parsed_string["ticket"][i]["id"] == row[3]:
                    t = False
        if t:
            cur.execute("DELETE FROM mydb.main WHERE `id`='%d'" %(row[0]))
            db.commit()
        else:
            t = True
            for i in range(0, len(parsed_string["client"])):
                if parsed_string["client"][i]["id"] == row[2]:
                    t = False
        if t:
            cur.execute("DELETE FROM mydb.main WHERE `id`='%d'" %(row[0]))
            db.commit()

    cur.execute("SELECT * FROM mydb.airline")
    rows = cur.fetchall()
    for row in rows:
        t = True
        for i in range(0, len(parsed_string["airline"])):
            if parsed_string["airline"][i]["id"] == row[0]:
                t = False
        if t:
            cur.execute("DELETE FROM mydb.airline WHERE `id`='%d'" % (row[0]))
            db.commit()
    for i in range(0,len(parsed_string["airline"])):
        t = False
        for row in rows:
            if parsed_string["airline"][i]["id"] == row[0]:
                t = True
        if t:
            cur.execute("UPDATE mydb.airline SET name='%s',rank='%s',home='%s' WHERE id=%d" % (
                parsed_string["airline"][i]["name"],
                parsed_string["airline"][i]["rank"],
                parsed_string["airline"][i]["home"],
                parsed_string["airline"][i]["id"]
            ))
        else:
            cur.execute("INSERT INTO airline(id, name, rank, home) VALUES(%d,'%s','%s','%s')" %(
            parsed_string["airline"][i]["id"],
            parsed_string["airline"][i]["name"],
            parsed_string["airline"][i]["rank"],
            parsed_string["airline"][i]["home"]
            ))
        db.commit()

    cur.execute("SELECT * FROM mydb.client")
    rows = cur.fetchall()
    for row in rows:
        t = True
        for i in range(0, len(parsed_string["client"])):
            if parsed_string["client"][i]["id"] == row[0]:
                t = False
        if t:
            cur.execute("DELETE FROM mydb.client WHERE `id`='%d'" % (row[0]))
            db.commit()
    for i in range(0,len(parsed_string["client"])):
        t = False
        for row in rows:
            if parsed_string["client"][i]["id"] == row[0]:
                t = True
        if t:
            cur.execute("UPDATE mydb.client SET name='%s', age=%d, home='%s', comment='%s', vip=%d WHERE id=%d" % (
                parsed_string["client"][i]["name"],
                parsed_string["client"][i]["age"],
                parsed_string["client"][i]["home"],
                parsed_string["client"][i]["comment"],
                parsed_string["client"][i]["vip"],
                parsed_string["client"][i]["id"]
            ))
        else:
            cur.execute("INSERT INTO client(id, name, age, home, comment, vip) VALUES(%d,'%s',%d,'%s','%s',%d)" %(
            parsed_string["client"][i]["id"],
            parsed_string["client"][i]["name"],
            parsed_string["client"][i]["age"],
            parsed_string["client"][i]["home"],
            parsed_string["client"][i]["comment"],
            parsed_string["client"][i]["vip"]
            ))
        db.commit()

    cur.execute("SELECT * FROM mydb.card")
    rows = cur.fetchall()
    for row in rows:
        t = True
        for i in range(0, len(parsed_string["card"])):
            if parsed_string["card"][i]["id"] == row[0]:
                t = False
        if t:
            cur.execute("DELETE FROM mydb.card WHERE `id`='%d'" % (row[0]))
            db.commit()
    for i in range(0,len(parsed_string["card"])):
        t = False
        for row in rows:
            if parsed_string["card"][i]["id"] == row[0]:
                t = True
        if t:
            cur.execute("UPDATE mydb.card SET rank='%s', bank_name='%s', card_limit=%d WHERE id=%d" % (
            parsed_string["card"][i]["rank"],
            parsed_string["card"][i]["bank_name"],
            parsed_string["card"][i]["card_limit"],
            parsed_string["card"][i]["id"]
            ))
        else:
            cur.execute("INSERT INTO card(id, rank, bank_name, card_limit) VALUES(%d,'%s','%s',%d)" %(
            parsed_string["card"][i]["id"],
            parsed_string["card"][i]["rank"],
            parsed_string["card"][i]["bank_name"],
            parsed_string["card"][i]["card_limit"]
            ))
        db.commit()

    cur.execute("SELECT * FROM mydb.ticket")
    rows = cur.fetchall()
    for row in rows:
        t = True
        for i in range(0, len(parsed_string["ticket"])):
            if parsed_string["ticket"][i]["id"] == row[0]:
                t = False
        if t:
            cur.execute("DELETE FROM mydb.ticket WHERE `id`='%d'" % (row[0]))
            db.commit()
    for i in range(0,len(parsed_string["ticket"])):
        t = False
        for row in rows:
            if parsed_string["ticket"][i]["id"] == row[0]:
                t = True
        if t:
            cur.execute("UPDATE mydb.ticket SET date='%s', from_city='%s', to_city='%s', cost=%d WHERE id=%d" % (
                parsed_string["ticket"][i]["date"],
                parsed_string["ticket"][i]["from_city"],
                parsed_string["ticket"][i]["to_city"],
                parsed_string["ticket"][i]["cost"],
                parsed_string["ticket"][i]["id"]
            ))
        else:
            cur.execute("INSERT INTO ticket(id, date, from_city, to_city, cost) VALUES(%d,'%s','%s','%s',%d)" %(
            parsed_string["ticket"][i]["id"],
            parsed_string["ticket"][i]["date"],
            parsed_string["ticket"][i]["from_city"],
            parsed_string["ticket"][i]["to_city"],
            parsed_string["ticket"][i]["cost"]
            ))
        db.commit()



    db.close()
    return redirect('/show/')


def show_main(request):
    if request.method == "GET":
        db = MySQLdb.connect(host="localhost" , user="root" , passwd="1111" , db="mydb")
        cur = db.cursor()

        sql = "SELECT ma.id,cl.name,ca.bank_name,ai.name,ti.date,ti.from_city,ti.to_city,cl.vip,ma.paid,cl.comment FROM mydb.main ma LEFT JOIN mydb.card ca ON ma.card_id=ca.id "
        sql = sql + "LEFT JOIN mydb.airline ai ON ma.airline_id=ai.id "
        sql = sql + "LEFT JOIN mydb.client cl ON ma.client_id=cl.id "
        sql = sql + "LEFT JOIN mydb.ticket ti ON ma.ticket_id=ti.id ORDER BY id;"
        cur.execute(sql)
        rows = cur.fetchall()
        db.close()
    return render(request,'Main_show.html',locals())
def show_date(request):
    if request.method == "POST":
        db = MySQLdb.connect(host="localhost" , user="root" , passwd="1111" , db="mydb")
        cur = db.cursor()
        date1 = request.POST['from']
        date2 = request.POST['to']
        vip = request.POST['vip']
        sql = "SELECT ma.id,cl.name,ca.bank_name,ai.name,ti.date,ti.from_city,ti.to_city,cl.vip,ma.paid,cl.comment FROM mydb.main ma LEFT JOIN mydb.card ca ON ma.card_id=ca.id "
        sql = sql + "LEFT JOIN mydb.airline ai ON ma.airline_id=ai.id "
        sql = sql + "LEFT JOIN mydb.client cl ON ma.client_id=cl.id "
        sql = sql + "LEFT JOIN mydb.ticket ti ON ma.ticket_id=ti.id WHERE vip = %d AND DATE(date) BETWEEN '%s' AND '%s' ORDER BY id;"%(int(vip), date1,date2)
        cur.execute(sql)
        rows = cur.fetchall()
        db.close()
    return render(request,'Main_show.html',locals())
def show_text(request):
    if request.method == "POST":
        db = MySQLdb.connect(host="localhost" , user="root" , passwd="1111" , db="mydb")
        cur = db.cursor()
        text1 = request.POST['text1']
        text2 = request.POST['text2']
        text = "'-"+text1+' "'+text2+'"'+"'"
        sql = "SELECT ma.id,cl.name,ca.bank_name,ai.name,ti.date,ti.from_city,ti.to_city,cl.vip,ma.paid,cl.comment FROM mydb.main ma LEFT JOIN mydb.card ca ON ma.card_id=ca.id "
        sql = sql + "LEFT JOIN mydb.airline ai ON ma.airline_id=ai.id "
        sql = sql + "LEFT JOIN mydb.client cl ON ma.client_id=cl.id "
        sql = sql + "LEFT JOIN mydb.ticket ti ON ma.ticket_id=ti.id WHERE MATCH(comment) AGAINST (%s IN BOOLEAN MODE) ORDER BY id;"%(text)
        cur.execute(sql)
        rows = cur.fetchall()
        db.close()
    return render(request,'Main_show.html',locals())
def search(request):
    if request.method == "GET":
        print 'get'
        return render(request,'search.html',locals())
    print request.POST['from']
    return render(request,'search.html',locals())
def show(request):
    if request.method == "GET":
        db = MySQLdb.connect(host="localhost" , user="root" , passwd="1111" , db="mydb")
        cur = db.cursor()

        sql = "SELECT * FROM mydb.ticket"
        cur.execute(sql)
        tickets = cur.fetchall()
        sql = "SELECT * FROM mydb.client"
        cur.execute(sql)
        clients = cur.fetchall()
        sql = "SELECT * FROM mydb.card"
        cur.execute(sql)
        cards = cur.fetchall()
        sql = "SELECT * FROM mydb.airline"
        cur.execute(sql)
        airlines = cur.fetchall()
        db.close()
    return render(request,'2show.html',locals())
def add(request):
    db = MySQLdb.connect(host="localhost", user="root", passwd="1111", db="mydb")
    cur = db.cursor()
    if request.method == "POST":
        client = request.POST['client_id']
        card = request.POST['card_id']
        airline = request.POST['airline_id']
        ticket = request.POST['ticket_id']
        paid = request.POST['paid']
        sql = "INSERT INTO main(paid, client_id, ticket_id, airline_id, card_id) VALUES(%d,%d,%d,%d,%d)" % (
        int(paid), int(client), int(ticket), int(airline), int(card))
        cur.execute(sql)
        db.commit()
        db.close()
        return redirect('/main/')
    scli = 1
    scar = 1
    sair = 1
    stic = 1
    sql = "SELECT id,name,vip from mydb.client"
    cur.execute(sql)
    clients = cur.fetchall()
    sql = "SELECT id,bank_name from mydb.card"
    cur.execute(sql)
    cards = cur.fetchall()
    sql = "SELECT id,name from mydb.airline"
    cur.execute(sql)
    airlines = cur.fetchall()
    sql = "SELECT id,date,from_city,to_city from mydb.ticket"
    cur.execute(sql)
    tickets = cur.fetchall()
    space = ' / '
    db.close()
    return render(request,'add.html',locals())

def delete(request):
    db = MySQLdb.connect('localhost', 'root', '1111', 'mydb')
    cur = db.cursor()
    id = request.POST['row_id']
    cur.execute("DELETE FROM mydb.main WHERE `id`='%d'" %(int(id)))
    db.commit()
    db.close()
    return redirect('/main/')

def edit(request):
    db = MySQLdb.connect(host="localhost", user="root", passwd="1111", db="mydb")
    cur = db.cursor()
    if request.POST['row_im'] == "0":
        id = request.POST['row_id']
        client = request.POST['client_id']
        card = request.POST['card_id']
        airline = request.POST['airline_id']
        ticket = request.POST['ticket_id']
        paid = request.POST['paid']
        sql ="UPDATE mydb.main SET paid=%d,client_id=%d,ticket_id=%d,airline_id=%d,card_id=%d WHERE id=%d"% (
        int(paid), int(client), int(ticket), int(airline), int(card), int(id))
        cur.execute(sql)
        db.commit()
        db.close()
        return redirect('/main/')

    id = request.POST['row_id']
    sql = "SELECT id, client_id, ticket_id, airline_id, card_id from mydb.main WHERE id=" + id
    cur.execute(sql)
    row = cur.fetchone()
    row_id = row[0]
    scli = row[1]
    scar = row[2]
    sair = row[3]
    stic = row[4]
    sql = "SELECT id,name,vip from mydb.client"
    cur.execute(sql)
    clients = cur.fetchall()
    sql = "SELECT id,bank_name from mydb.card"
    cur.execute(sql)
    cards = cur.fetchall()
    sql = "SELECT id,name from mydb.airline"
    cur.execute(sql)
    airlines = cur.fetchall()
    sql = "SELECT id,date,from_city,to_city from mydb.ticket"
    cur.execute(sql)
    tickets = cur.fetchall()
    space = ' / '
    db.close()
    return render(request,'edit.html',locals())