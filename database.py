from sqlite3 import connect, OperationalError
from create import create

class Database:

    def __init__(self):
        self.conn = connect("dbase.db")
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute("SELECT * FROM buses")
        except OperationalError:
            for sql in create:
                self.cursor.execute(sql)
                
    def __del__(self):
        self.conn.close()

    def get_bus_fields(self):##
        return ("number", "capacity", "model", "year", "checkup", "mileage")
    
    def get_bus_rus_fields(self):##
        return ("Номер", "Мест", "Модель", "Год", "ТО", "Пробег")      

    def get_driver_fields(self):##
        return ("fullname", "experience", "categories", "birthday", "fines", "snils")
    
    def get_driver_rus_fields(self):##
        return ("ФИО", "Опыт", "Категория", "Дата рожд.", "Штрафы", "СНИЛС")

    def get_bustrip_fields(self):##
        return ("number", "destination", "time")
    
    def get_bustrip_rus_fields(self):##
        return ("№ рейса", "Остановки", "Время")

    def get_destination_fields(self):##
        return ("name",)
    
    def get_destination_rus_fields(self):##
        return ("Название",)

    def get_passenger_fields(self):##
        return ("fullname",)
    
    def get_passenger_rus_fields(self):##
        return ("ФИО",)

    def get_ticket_fields(self):##
        return ("price", "bustrip", "seats", "passenger", "date")
    
    def get_ticket_rus_fields(self):##
        return ("Цена", "Рейс", "Место", "Пассажир", "Дата")

    def get_buses(self):##
        yield "%-5s|%-4s|%-10s|%4s|%4s|%6s" % ("Номер", "Мест", "Модель", "Год", "ТО", "Пробег")
        self.cursor.execute("SELECT * FROM buses")
        for number, capacity, model, year, checkup, mileage in self.cursor.fetchall():
            yield "%-5s|%4s|%-10s|%4s|%4s|%6s" % (number, capacity, model, year, checkup, mileage)

    def get_driver(self):##
        yield "%-15s|%-4s|%-9s|%7s|%4s|%6s" % ("ФИО", "Опыт", "Категория", "Дата рожд.", "Штрафы", "СНИЛС")
        self.cursor.execute("SELECT * FROM driver")
        for fullname, experience, categories, birthday, fines, snils in self.cursor.fetchall():
            yield "%-15s|%4s|%-9s|%7s|%4s|%6s" % (fullname, experience, categories, birthday, fines, snils)
            
    def get_bustrip(self):##
        yield "%-7s|%-25s|%-5s" % ("№ рейса", "Остановки", "Время")
        self.cursor.execute("SELECT * FROM bustrips")
        for number, destination, time in self.cursor.fetchall():
            yield "%-7s|%25s|%-5s" % (number, destination, time)

    def get_destination(self):##
        yield "%-10s" % ("Название")
        self.cursor.execute("SELECT * FROM destination")
        for name in self.cursor.fetchall():
            yield "%-0s" % (name)

    def get_passenger(self):##
        yield "%-30s" % ("ФИО")
        self.cursor.execute("SELECT * FROM passenger")
        for fullname in self.cursor.fetchall():
            yield "%-30s" % (fullname)

    def get_tickets(self):##
        yield "%-4s|%-9s|%7s|%4s|%6s" % ("Цена", "Рейс", "Место", "Пассажир", "Дата")
        self.cursor.execute("SELECT * FROM tickets")
        for price, bustrip, seats, passenger, date in self.cursor.fetchall():
            yield "%-4s|%-9s|%7s|%4s|%6s" % (price, bustrip, seats, passenger, date)
    
    def insert_bus(self, number, capacity, model, year, checkup, mileage):
        self.cursor.execute("""INSERT INTO buses VALUES
               ('%s', '%s', '%s', '%s', '%s', '%s')""" % (number, capacity, model, year, checkup, mileage))
        self.conn.commit()

    def insert_driver(self, fullname, experience, categories, birthday, fines, snils):
        self.cursor.execute("""INSERT INTO driver VALUES
                ('%s', '%s', '%s', '%s', '%s', '%s')""" % (fullname, experience, categories, birthday, fines, snils))
        self.conn.commit()

    def insert_ticket(self, price, bustrip, seats, passenger, date):
        self.cursor.execute("""INSERT INTO tickets VALUES
                ('%s', '%s', '%s', '%s', '%s')""" % (price, bustrip, seats, passenger, date))
        self.conn.commit()

    def insert_bustrips(self, number, destination, time):
        self.cursor.execute("""INSERT INTO bustrips VALUES
                ('%s', '%s', '%s')""" % (number, destination, time))
        self.conn.commit()

    def insert_destination(self, name):
        self.cursor.execute("""INSERT INTO destination VALUES
                ('%s')""" % (name))
        self.conn.commit()

    def insert_passenger(self, fullname):
        self.cursor.execute("""INSERT INTO passenger VALUES
                ('%s')""" % (fullname))
        self.conn.commit()

    def delete_bus(self, number):####
        self.cursor.execute("""DELETE FROM buses WHERE number = '%s'""" % (number))
        self.conn.commit()

    def delete_driver(self, snils):####
        self.cursor.execute("""DELETE FROM driver WHERE snils = '%s'""" % (snilsv))
        self.conn.commit()

    def delete_bustrip(self, number):####
        self.cursor.execute("""DELETE FROM bustrips WHERE number = '%s'""" % (number))
        self.conn.commit()

    def delete_destination(self, name):####
        self.cursor.execute("""DELETE FROM destination WHERE name = '%s'""" % (name))
        self.conn.commit()

    def delete_passenger(self, fullname):####
        self.cursor.execute("""DELETE FROM passenger WHERE fullname = '%s'""" % (fullname))
        self.conn.commit()

    def delete_ticket(self, date, passenger, bustrip):####
        self.cursor.execute("""DELETE FROM tickets
                               WHERE date = '%s' and
                                     passenger = '%s' and
                                     bustrips = '%s'""" % (date, passenger, bustrip))
        self.conn.commit()

if __name__ == "__main__":
    database = Database()
    
##
##bus0 = {
##    'number':'e234ke123',
##    'capacity' : '32',
##    'model' : 'zzz',
##    'year' : '2000',
##    'checkup' : '2018',
##    'mileage' : '200 000'
##}
##
##bus1 = {
##    'number':'a125bc',
##    'capacity' : '32',
##    'model' : 'zzz',
##    'year' : '2000',
##    'checkup' : '2018',
##    'mileage' : '200 000'
##}
##
##driver = {
##    'fullname' : 'sam frt',
##    'experience' : '25',
##    'categories' : 'a,b,c,d',
##    'birthday' : '49',
##    'fines' : 'no',
##    'snils' : '0'
##    }
##
##tickets = {
##    'price' : '400',
##    'bustrips' : 'cc - nn',
##    'seats' : '18',
##    'passenger' : 'fill btr',
##    'data' : '20/12/18'
##    }
##
##bustrips = {
##    'number' : '265',
##    'destination' : 'bbb',
##    'time' : '20/10'
##    }
##
##destination = {
##    'name' : 'bbb'
##    }
##
##passenger = {
##    'fullname' : 'dilan rth'
##
##}
