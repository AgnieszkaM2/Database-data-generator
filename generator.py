# -*- coding: utf-8 -*-
import cx_Oracle
import random
import datetime
import sys

#lista z cenami

prices=[15.60, 20.00, 25.99, 28.30, 32.20, 35.50, 38.99, 41.00, 46.99, 49.99, 52.30, 56.70, 67.00, 70.20, 74.40, 80.99, 85.90, 90.00, 95.25, 99.99, 100.00, 115.20, 120.00, 125.99, 130.00, 135.50]

#lista z literami

alphabet = []
for letter in range(65,91):
    alphabet.append(chr(letter))
for letter in range(97,123):
    alphabet.append(chr(letter))

#lista z zawodami    

jobs=['sprzedawca','manager','ochrona']
    
#funkcja tworząca losowe słowa

def random_words(min_size,max_size,chars):
    size=0
    for x in range(random.randint(min_size+1, max_size+1)):
                   size=x
    return ''.join(random.sample(chars,k=size))

#funkcja do tworzenia insertów do tabeli Pracownicy i zapisywania ich później do plików

def pracownicy(rowsCount):
    #Tworzenie kursora
    Cursor=con.cursor()
    
    now = datetime.datetime.now()
    dt_string = now.strftime("%d-%m-%Y %H-%M-%S")
    f=open('pracownicy_insert_{0}.txt'.format(dt_string),'a')
    for i in range(rowsCount):
        #Pobieranie wartosci ostatniego Id w tabeli i inkrementowanie go
        SQL1    = "SELECT MAX(Id_pracownika) FROM PRACOWNICY"
        Cursor.execute(SQL1)
        results = Cursor.fetchall()
        maxId=0
        for i in results:
            i=list(i)
            a=i[0]
        if a =='' or a==[] or a== 0  or a== None:
            maxId=1
        else:
            maxId=a
            maxId=maxId+1
        name=random_words(2, 40, alphabet)
        surname=random_words(2, 40, alphabet)
        month=random.randint(1, 12)
        
        day=random.randint(1, 28)
        day=str(day)
        month=str(month)
        
        month=random.randint(1, 12)
        month=random.randint(1, 12)
        year=random.randint(2001, 2021)
        year=str(year)
        year=year[2:4]
        forma='DD-MM-RR'
        date='{0}-{1}-{2}'.format(day,month,year)
        first = random.randint(1,9)
        first = str(first)
        n = 11 
        nrs = [str(random.randrange(10)) for i in range(n-1)]
        for i in range(len(nrs))    :
            first += str(nrs[i])
        pesel=first
        pesel=int(pesel)
        salary=year=random.randint(1000, 4000)
        job=random.choice(jobs)
        #Tworzenie insertu do bazy i wykonywanie go
        
        statement = 'insert into Pracownicy values (:1,:2,:3,to_date(:4,:5),:6,:7,:8)'
        Cursor.execute(statement, (maxId,name,surname,date,forma,pesel,salary,job))
        statement_copy = 'insert into Pracownicy values ({0},{1},{2},to_date({3},{4}),{5},{6},{7})'.format(maxId,name,surname,date,forma,pesel,salary,job)
        con.commit()
        f.write(statement_copy+'\n')
    print('Dodano {0} wierszy do tabeli Pracownicy'.format(rowsCount))
    Cursor.close()
    f.close()

#funkcja do tworzenia insertów do tabeli Grafik i zapisywania ich później do plików

def grafik(rowsCount):
    Cursor=con.cursor()
    now = datetime.datetime.now()
    today=datetime.date.today().strftime('%d-%m-%y')
    d=[]
    d=today.split('-')
    dt_string = now.strftime("%d-%m-%Y %H-%M-%S")
    f=open('grafik_insert_{0}.txt'.format(dt_string),'a')
    for i in range(rowsCount):
        SQL1    = "SELECT MAX(Id_grafik) FROM GRAFIK"
        Cursor.execute(SQL1)
        results = Cursor.fetchall()
        maxId=0
        # a=0
        for i in results:
            i=list(i)
            a=i[0]
        if a =='' or a==[] or a== 0 or a== None:
            maxId=1
        else:
            maxId=a
            maxId=maxId+1
        #Pobieranie wartosci Id klucza obcego i tworzenia listy otrzymanych wartosci z bazy
        
        SQL2    = "SELECT Id_pracownika FROM PRACOWNICY"
        Cursor.execute(SQL2)
        results2 = Cursor.fetchall()
        employees=[item for t in results2 for item in t]
        zmiana=['pierwsza','druga']
        zm=random.choice(zmiana)
        d1=int(d[0])
        d2=int(d[1])
        d3=int(d[2])
        month=random.randint(d2, 12)
        if month==2:
            day=random.randint(1, 28)
            day=str(day)
        else:
            day=random.randint(d1, 30)
            day=str(day)
        month=str(month)
        year=d3
        year=str(year)
        forma='DD-MM-RR'
        date='{0}-{1}-{2}'.format(day,month,year)
        employeeId=random.choice(employees)
        statement = 'insert into Grafik values (:1,:2,to_date(:3,:4),:5)'
        Cursor.execute(statement, (maxId,zm,date,forma,employeeId))
        statement_copy = 'insert into Grafik values ({0},{1},to_date({2},{3}),{4})'.format(maxId,zm,date,forma,employeeId)
        con.commit()
        f.write(statement_copy+'\n')
    print('Dodano {0} wierszy do tabeli Grafik'.format(rowsCount))
    Cursor.close()
    f.close()

#funkcja do tworzenia insertów do tabeli Klient i zapisywania ich później do plików

def klient(rowsCount):
    Cursor=con.cursor()
    now = datetime.datetime.now()
    dt_string = now.strftime("%d-%m-%Y %H-%M-%S")
    f=open('klient_insert_{0}.txt'.format(dt_string),'a')
    for i in range(rowsCount):
        SQL1    = "SELECT MAX(Id_klienta) FROM KLIENT"
        Cursor.execute(SQL1)
        results = Cursor.fetchall()
        maxId=0
        for i in results:
            i=list(i)
            a=i[0]
        if a =='' or a==[] or a== 0 or a== None:
            maxId=1
        else:
            maxId=a
            maxId=maxId+1
        name=random_words(2, 40, alphabet)
        surname=random_words(2, 40, alphabet)
        first = random.randint(1,9)
        first = str(first)
        n = 9
        
        nrs = [str(random.randrange(10)) for i in range(n-1)]
        for i in range(len(nrs))    :
            first += str(nrs[i])
        phone=first
        phone=int(phone)
        email='{0}@{1}.com'.format(random_words(2, 10, alphabet),random_words(2, 5, alphabet))
        address='ul.{0} {1}, {2}'.format(random_words(2, 10, alphabet),random.randint(1, 300),random_words(2, 8, alphabet))
        statement = 'insert into Klient values (:1,:2,:3,:4,:5,:6)'
        Cursor.execute(statement, (maxId,name,surname,phone,email,address))
        statement_copy = 'insert into Klient values ({0},{1},{2},{3},{4},{5})'.format(maxId,name,surname,phone,email,address)
        con.commit()
        f.write(statement_copy+'\n')
    print('Dodano {0} wierszy do tabeli Klient'.format(rowsCount))
    Cursor.close()
    f.close()

#funkcja do tworzenia insertów do tabeli Zamowienia i zapisywania ich później do plików

def zamowienia(rowsCount):
    Cursor=con.cursor()
    now = datetime.datetime.now()
    today=datetime.date.today().strftime('%d-%m-%y')
    dt=[]
    dt=today.split('-')
    dt_string = now.strftime("%d-%m-%Y %H-%M-%S")
    f=open('zamowienia_insert_{0}.txt'.format(dt_string),'a')
    for i in range(rowsCount):
        SQL1    = "SELECT MAX(Id_zamowienia) FROM ZAMOWIENIA"
        Cursor.execute(SQL1)
        results = Cursor.fetchall()
        maxId=0
        for i in results:
            i=list(i)
            a=i[0]
        if a =='' or a==[] or a== 0 or a== None:
            maxId=1
        else:
            maxId=a
            maxId=maxId+1
        SQL2    = "SELECT Id_pracownika FROM PRACOWNICY"
        Cursor.execute(SQL2)
        results2 = Cursor.fetchall()
        employees=[item for t in results2 for item in t]
        SQL3    = "SELECT Id_klienta FROM KLIENT"
        Cursor.execute(SQL3)
        results3 = Cursor.fetchall()
        clients=[item for t in results3 for item in t]
        SQL4    = "SELECT MAX(Data) FROM ZAMOWIENIA"
        Cursor.execute(SQL4)
        results4 = Cursor.fetchall()
        for i in results4:
            i=list(i)
            lastDate=str(i[0])
        if lastDate=='' or lastDate==None or lastDate=='None':
            day=int(dt[0])
            month=int(dt[1])
            year=int(dt[2])
        else:
            d=[]
            pom=lastDate[1:10]
            d=pom.split('-')
            y=d[0]
            y=y[1:3]
            day=int(d[2])
            month=int(d[1])
            year=int(y)
            if day==28 and month!=12:
                day=1
                month=month+1
            elif day==26 or day==27:
                day=28
            elif month==2 and day==28:
                month=3
                day=random.randint(1,3)
            elif month==12 and day==28:
                month=1
                day=random.randint(1,3)
                year=year+1
            elif month==12 and day==30:
                month=1
                day=random.randint(1,3)
                year=year+1
            else:
                day=random.randint(day, day+1)
        day=str(day)
        month=str(month)
        year=str(year)
        forma='DD-MM-RR'
        date='{0}-{1}-{2}'.format(day,month,year)
        price=random.choice(prices)
        status=['w drodze','do odbioru','odebrane']
        stat=random.choice(status)
        employeeId=random.choice(employees)
        clientId=random.choice(clients)
        statement = 'insert into Zamowienia values (:1,to_date(:2,:3),:4,:5,:6,:7)'
        Cursor.execute(statement, (maxId,date,forma,price,stat,clientId,employeeId))
        statement_copy = 'insert into Zamowienia values ({0},to_date({1},{2}),{3},{4},{5},{6})'.format(maxId,date,forma,price,stat,clientId,employeeId)
        con.commit()
        f.write(statement_copy+'\n')
    print('Dodano {0} wierszy do tabeli Zamowienia'.format(rowsCount))
    Cursor.close()
    f.close()

#funkcja do tworzenia insertów do tabeli Platnosci i zapisywania ich później do plików

def platnosci(rowsCount):
    Cursor=con.cursor()
    now = datetime.datetime.now()
    today=datetime.datetime.today()
    today=today.strftime("%m-%d-%y")
    dt_string = now.strftime("%d-%m-%Y %H-%M-%S")
    f=open('platnosci_insert_{0}.txt'.format(dt_string),'a')
    for i in range(rowsCount):
        SQL1    = "SELECT MAX(Id_platnosci) FROM PLATNOSCI"
        Cursor.execute(SQL1)
        results = Cursor.fetchall()
        maxId=0
        for i in results:
            i=list(i)
            a=i[0]
        if a =='' or a==[] or a== 0 or a== None:
            maxId=1
        else:
            maxId=a
            maxId=maxId+1
        SQL2    = "SELECT Id_zamowienia FROM ZAMOWIENIA"
        Cursor.execute(SQL2)
        results2 = Cursor.fetchall()
        orders=[item for t in results2 for item in t]
        orderId=random.choice(orders)
        SQL3    = "SELECT Data FROM ZAMOWIENIA WHERE Id_zamowienia = {0}".format(orderId)
        Cursor.execute(SQL3)
        results3 = Cursor.fetchall()
        
        for i in results3:
            i=list(i)
            orderDate=str(i[0])
        d=[]
        pom=orderDate[1:10]
        d=pom.split('-')
        y=d[0]
        y=y[1:3]
        day=int(d[2])
        month=int(d[1])
        year=int(y)
        day=str(day)
        month=str(month)
        year=str(year)
        forma='DD-MM-RR'
        date='{0}-{1}-{2}'.format(day,month,year)
        forms=['gotówka','karta']
        form=random.choice(forms)
        statement = 'insert into Platnosci values (:1,:2,to_date(:3,:4),:5)'
        Cursor.execute(statement, (maxId,form,date,forma,orderId))
        statement_copy = 'insert into Platnosci values ({0},{1},to_date({2},{3}),{4})'.format(maxId,form,date,forma,orderId)
        con.commit()
        f.write(statement_copy+'\n')
    print('Dodano {0} wierszy do tabeli Platnosci'.format(rowsCount))
    Cursor.close()
    f.close()

#funkcja do tworzenia insertów do tabeli Autor i zapisywania ich później do plików

def autor(rowsCount):
    Cursor=con.cursor()
    now = datetime.datetime.now()
    dt_string = now.strftime("%d-%m-%Y %H-%M-%S")
    f=open('autor_insert_{0}.txt'.format(dt_string),'a')
    for i in range(rowsCount):
        SQL1    = "SELECT MAX(Id_autor) FROM AUTOR"
        Cursor.execute(SQL1)
        results = Cursor.fetchall()
        maxId=0
        for i in results:
            i=list(i)
            a=i[0]
        if a =='' or a==[] or a== 0 or a== None:
            maxId=1
        else:
            maxId=a
            maxId=maxId+1
        name=random_words(2, 40, alphabet)
        surname=random_words(2, 40, alphabet)
        statement = 'insert into Autor values (:1,:2,:3)'
        Cursor.execute(statement, (maxId,name,surname))
        statement_copy = 'insert into Autor values ({0},{1},{2})'.format(maxId,name,surname)
        con.commit()
        f.write(statement_copy+'\n')
    print('Dodano {0} wierszy do tabeli Autor'.format(rowsCount))
    Cursor.close()
    f.close()

#funkcja do tworzenia insertów do tabeli Wydawnictwo i zapisywania ich później do plików

def wydawnictwo(rowsCount):
    Cursor=con.cursor()
    now = datetime.datetime.now()
    dt_string = now.strftime("%d-%m-%Y %H-%M-%S")
    f=open('wydawnictwo_insert_{0}.txt'.format(dt_string),'a')
    for i in range(rowsCount):
        SQL1    = "SELECT MAX(Id_wydawnictwo) FROM WYDAWNICTWO"
        Cursor.execute(SQL1)
        results = Cursor.fetchall()
        maxId=0
        for i in results:
            i=list(i)
            a=i[0]
        if a =='' or a==[] or a== 0 or a== None:
            maxId=1
        else:
            maxId=a
            maxId=maxId+1
        name=random_words(2, 50, alphabet)
        statement = 'insert into Wydawnictwo values (:1,:2)'
        Cursor.execute(statement, (maxId,name))
        statement_copy = 'insert into Wydawnictwo values ({0},{1})'.format(maxId,name)
        con.commit()
        f.write(statement_copy+'\n')
    print('Dodano {0} wierszy do tabeli Wydawnictwo'.format(rowsCount))
    Cursor.close()
    f.close()

#funkcja do tworzenia insertów do tabeli Ksiazka i zapisywania ich później do plików

def ksiazka(rowsCount):
    Cursor=con.cursor()
    now = datetime.datetime.now()
    dt_string = now.strftime("%d-%m-%Y %H-%M-%S")
    f=open('ksiazka_insert_{0}.txt'.format(dt_string),'a')
    for i in range(rowsCount):
        SQL1    = "SELECT MAX(Id_ksiazka) FROM KSIAZKA"
        Cursor.execute(SQL1)
        results = Cursor.fetchall()
        maxId=0
        for i in results:
            i=list(i)
            a=i[0]
        if a =='' or a==[] or a== 0 or a== None:
            maxId=1
        else:
            maxId=a
            maxId=maxId+1
        SQL2    = "SELECT Id_autor FROM AUTOR"
        Cursor.execute(SQL2)
        results2 = Cursor.fetchall()
        autors=[item for t in results2 for item in t]
        autorId=random.choice(autors)
        SQL3    = "SELECT Id_wydawnictwo FROM WYDAWNICTWO"
        Cursor.execute(SQL3)
        results3 = Cursor.fetchall()
        wydawnictwa=[item for t in results3 for item in t]
        wydId=random.choice(wydawnictwa)
        title=random_words(2, 40, alphabet)
        desc=''
        for i in range(18):
            des=random_words(8, 10, alphabet)
            desc=desc + ' ' + des
        year=random.randint(1930,2021)
        price=random.choice(prices)
        statement = 'insert into Ksiazka values (:1,:2,:3,:4,:5,:6,:7)'
        Cursor.execute(statement, (maxId,title,year,price,desc,autorId,wydId))
        statement_copy = 'insert into Ksiazka values ({0},{1},{2},{3},{4},{5},{6})'.format(maxId,title,year,price,desc,autorId,wydId)
        con.commit()
        f.write(statement_copy+'\n')
    print('Dodano {0} wierszy do tabeli Ksiazka'.format(rowsCount))
    Cursor.close()
    f.close()
    
#funkcja do tworzenia insertów do tabeli Zamowienia_info i zapisywania ich później do plików

def zamowienia_info(rowsCount):
    Cursor=con.cursor()
    now = datetime.datetime.now()
    dt_string = now.strftime("%d-%m-%Y %H-%M-%S")
    f=open('info_insert_{0}.txt'.format(dt_string),'a')
    for i in range(rowsCount):
        SQL1    = "SELECT MAX(Id_info) FROM ZAMOWIENIA_INFO"
        Cursor.execute(SQL1)
        results = Cursor.fetchall()
        maxId=0
        for i in results:
            i=list(i)
            a=i[0]
        if a =='' or a==[] or a== 0 or a== None:
            maxId=1
        else:
            maxId=a
            maxId=maxId+1
        SQL2    = "SELECT Id_ksiazka FROM KSIAZKA"
        Cursor.execute(SQL2)
        results2 = Cursor.fetchall()
        books=[item for t in results2 for item in t]
        bookId=random.choice(books)
        SQL3    = "SELECT Id_zamowienia FROM ZAMOWIENIA"
        Cursor.execute(SQL3)
        results3 = Cursor.fetchall()
        orders=[item for t in results3 for item in t]
        orderId=random.choice(orders)
        number=random.randint(1, 150)
        statement = 'insert into Zamowienia_info values (:1,:2,:3,:4)'
        Cursor.execute(statement, (maxId,number,bookId,orderId))
        statement_copy = 'insert into Zamowienia_info values ({0},{1},{2},{3})'.format(maxId,number,bookId,orderId)
        con.commit()
        f.write(statement_copy+'\n')
    print('Dodano {0} wierszy do tabeli Zamowienia_info'.format(rowsCount))
    Cursor.close()
    f.close()

#funkcja do tworzenia insertów do tabeli Egzemplarze i zapisywania ich później do plików

def egzemplarze(rowsCount):
    Cursor=con.cursor()
    today=datetime.date.today().strftime('%d-%m-%y')
    d=[]
    d=today.split('-')
    now = datetime.datetime.now()
    dt_string = now.strftime("%d-%m-%Y %H-%M-%S")
    f=open('egzemplarze_insert_{0}.txt'.format(dt_string),'a')
    for i in range(rowsCount):
        SQL1    = "SELECT MAX(Id_egzemplarze) FROM EGZEMPLARZE"
        Cursor.execute(SQL1)
        results = Cursor.fetchall()
        maxId=0
        for i in results:
            i=list(i)
            a=i[0]
        if a =='' or a==[] or a== 0 or a== None:
            maxId=1
        else:
            maxId=a
            maxId=maxId+1
        SQL2    = "SELECT Id_ksiazka FROM KSIAZKA"
        Cursor.execute(SQL2)
        results2 = Cursor.fetchall()
        books=[item for t in results2 for item in t]
        bookId=random.choice(books)
        number=random.randint(1, 30)
        SQL3    = "SELECT Cena FROM KSIAZKA WHERE Id_ksiazka = {0}".format(bookId)
        Cursor.execute(SQL3)
        results3 = Cursor.fetchall()
        p=0
        for i in results3:
            i=list(i)
            p=i[0]
        price=number*p
        d1=int(d[0])
        d2=int(d[1])
        # d3=int(d[2])
        month=random.randint(d2, 12)
        if month==2:
            day=random.randint(1, 28)
            day=str(day)
        else:
            day=random.randint(d1, 30)
            day=str(day)
        month=str(month)
        year=random.randint(10, 21)
        year=str(year)
        forma='DD-MM-RR'
        date='{0}-{1}-{2}'.format(day,month,year)
        statement = 'insert into Egzemplarze values (:1,:2,to_date(:3,:4),:5,:6)'
        Cursor.execute(statement, (maxId,number,date,forma,price,bookId))
        statement_copy = 'insert into Egzemplarze values ({0},{1},to_date({2},{3}),{4},{5})'.format(maxId,number,date,forma,price,bookId)
        con.commit()
        f.write(statement_copy+'\n')
    print('Dodano {0} wierszy do tabeli Egzemplarze'.format(rowsCount))
    Cursor.close()
    f.close()

#funkcja do tworzenia insertów do tabeli Stan i zapisywania ich później do plików

def stan(rowsCount):
    Cursor=con.cursor()
    now = datetime.datetime.now()
    dt_string = now.strftime("%d-%m-%Y %H-%M-%S")
    f=open('stan_insert_{0}.txt'.format(dt_string),'a')
    for i in range(rowsCount):
        SQL1    = "SELECT MAX(Id_stan) FROM STAN"
        Cursor.execute(SQL1)
        results = Cursor.fetchall()
        maxId=0
        # a=0
        for i in results:
            i=list(i)
            a=i[0]
        if a =='' or a==[] or a== 0 or a== None:
            maxId=1
        else:
            maxId=a
            maxId=maxId+1
        SQL2    = "SELECT Id_ksiazka FROM KSIAZKA"
        Cursor.execute(SQL2)
        results2 = Cursor.fetchall()
        books=[item for t in results2 for item in t]
        bookId=random.choice(books)
        number1=random.randint(1, 300)
        number2=random.randint(1, 300)
        statement = 'insert into Stan values (:1,:2,:3,:4)'
        Cursor.execute(statement, (maxId,number1,number2,bookId))
        statement_copy = 'insert into Stan values ({0},{1},{2},{3})'.format(maxId,number1,number2,bookId)
        con.commit()
        f.write(statement_copy+'\n')
    print('Dodano {0} wierszy do tabeli Stan'.format(rowsCount))
    Cursor.close()
    f.close()

#String do połączenia się z przykładowym użytkownikiem lokalnej bazy danych

try:
    con = cx_Oracle.connect('USER/user123@localhost:1521/XEPDB1')

      
except cx_Oracle.DatabaseError as e:
    print("Wystąpił problem połączenia z bazą", e)
    
#Główna funkcja zawierająca możliwe do wyboru opcje programu

def main():
    print()

    print('Generowanie danych do bazy')
    print()
    print('  1- Wszystkie tabele   2-tabela Pracownicy   3-tabela Grafik   4-tabela Klient')
    print()
    print('  5-tabela Zamowienia   6-tabela Platnosci    7-tabela Autor    8-tabela Wydawnictwo')
    print()
    print('  9-tabela Ksiazka    10-tabela Zamowienia_info   11-tabela Egzemplarze   12-tabela Stan')
    print()
    
    selection=int(input('Wybierz jedną z powyższych opcji:  '))
    
    if selection==0 or selection>12:
        print('Błędna wybór opcji, spróbuj jeszcze raz.')
        selection=int(input('Wybierz jedną z powyższych opcji:  '))
    print()
    rowsCount=int(input('Okresl liczbę wierszy do wygenerowania:  '))
    print()
    if rowsCount==0:
        print('Błędna wartosć, spróbuj jeszcze raz.')
        rowsCount=int(input('Okresl liczbę wierszy do wygenerowania:  '))
    if selection==1:
        try:
            pracownicy(rowsCount)
            print()
            grafik(rowsCount)
            print()
            klient(rowsCount)
            print()
            zamowienia(rowsCount)
            print()
            platnosci(rowsCount)
            print()
            autor(rowsCount)
            print()
            wydawnictwo(rowsCount)
            print()
            ksiazka(rowsCount)
            print()
            zamowienia_info(rowsCount)
            print()
            egzemplarze(rowsCount)
            print()
            stan(rowsCount)
            print()
        except cx_Oracle.Error as error:
            print('Wystąpił błąd:')
            print(error)
    elif selection==2:
        try:
            pracownicy(rowsCount)
        except cx_Oracle.Error as error:
            print('Wystąpił błąd:')
            print(error)
    elif selection==3:
        try:
            grafik(rowsCount)
        except cx_Oracle.Error as error:
            print('Wystąpił błąd:')
            print(error)
    elif selection==4:
        try:
            klient(rowsCount)
        except cx_Oracle.Error as error:
            print('Wystąpił błąd:')
            print(error)
    elif selection==5:
        try:
            zamowienia(rowsCount)
        except cx_Oracle.Error as error:
            print('Wystąpił błąd:')
            print(error)
    elif selection==6:
        try:
            platnosci(rowsCount)
        except cx_Oracle.Error as error:
            print('Wystąpił błąd:')
            print(error)
    elif selection==7:
        try:
            autor(rowsCount)
        except cx_Oracle.Error as error:
            print('Wystąpił błąd:')
            print(error)
    elif selection==8:
        try:
            wydawnictwo(rowsCount)
        except cx_Oracle.Error as error:
            print('Wystąpił błąd:')
            print(error)
    elif selection==9:
        try:
            ksiazka(rowsCount)
        except cx_Oracle.Error as error:
            print('Wystąpił błąd:')
            print(error)
    elif selection==10:
        try:
            zamowienia_info(rowsCount)
        except cx_Oracle.Error as error:
            print('Wystąpił błąd:')
            print(error)
    elif selection==11:
        try:
            egzemplarze(rowsCount)
        except cx_Oracle.Error as error:
            print('Wystąpił błąd:')
            print(error)
    elif selection==12:
        try:
            stan(rowsCount)
        except cx_Oracle.Error as error:
            print('Wystąpił błąd:')
            print(error)
    print()

main()
k=input('Czy chcesz wygenerować kolejne dane?  (y/n) ')
while k=='y':
    main()
    k=input('Czy chcesz wygenerować kolejne dane?  (y/n) ')

if k=='n':
    con.close()
    sys.exit()
else:
    print('Błędna odpowiedź, spróbuj jeszcze raz.')
    k=input('Czy chcesz wygenerować kolejne dane?  (y/n) ')
    





