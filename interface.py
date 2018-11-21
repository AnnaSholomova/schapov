from tkinter import *

from database import Database

class Interface:
    vars = {}
    
    def __make_frames(self):
        self.bus_frame = Frame(self.__root,bg='#fff4be',bd=5)
        self.driver_frame = Frame(self.__root,bg='#bfd2cd',bd=5)
        self.ticket_frame = Frame(self.__root,bg='#ffec8b',bd=5)
        self.bustrip_frame = Frame(self.__root,bg='#faebd7',bd=5)
        self.destination_frame = Frame(self.__root,bg='#cdc0b0',bd=5)
        self.passenger_frame = Frame(self.__root,bg='#fff981',bd=5)

    def __set_trip_dest_value(self, event):
        try:
            i = self.destination_list.curselection()[0]
            if i > 0:
                self.vars["destination"].set(
                    self.destination_list.get(ACTIVE).strip()
                )
        except IndexError:
            pass

    def __set_ticket_pass_value(self, event):
        try:
            i = self.passenger_list.curselection()[0]
            if i > 0:
                self.vars["passenger"].set(
                    self.passenger_list.get(ACTIVE).strip()
                )
        except IndexError:
            pass

    def __set_ticket_trip_value(self, event):
        try:
            i = self.bustrip_list.curselection()[0]
            if i > 0:
                self.vars["bustrip"].set(
                    self.bustrip_list.get(ACTIVE).split('|')[0].strip()
                )
        except IndexError:
            pass

    def __make_lists(self):
        self.bus_list         = Listbox(self.bus_frame,        height=8,width=45, font='consolas')
        self.driver_list      = Listbox(self.driver_frame,     height=8,width=45, font='consolas')
        self.ticket_list      = Listbox(self.ticket_frame,     height=8,width=45, font='consolas')
        self.bustrip_list     = Listbox(self.bustrip_frame,    height=8,width=45, font='consolas')
        self.destination_list = Listbox(self.destination_frame,height=8,width=45, font='consolas')
        self.passenger_list   = Listbox(self.passenger_frame,  height=8,width=45, font='consolas')
        self.destination_list.bind("<Button-1>", self.__set_trip_dest_value)
        self.passenger_list.bind(  "<Button-1>", self.__set_ticket_pass_value)
        self.bustrip_list.bind(    "<Button-1>", self.__set_ticket_trip_value)
        #self.bus_list.bind(        "<Button-1>", self.__set_trip_dest_value)


    def __place_frames(self):
        row, col = 0, 0
        for frame, title, listbox, foo in [
                (self.bus_frame,"Автобусы", self.bus_list, self.insert_bus),
                (self.driver_frame,"Водители", self.driver_list, self.insert_driver ),
                (self.bustrip_frame, "Рейсы", self.bustrip_list, self.insert_bustrip),
                (self.destination_frame, "Остановки", self.destination_list, self.insert_destination ),
                (self.passenger_frame, "Пассажиры", self.passenger_list, self.insert_passenger),
                (self.ticket_frame, "Билеты", self.ticket_list, self.insert_ticket),
                ]:
            Label(frame, text = title).pack()
            listbox.pack()
            frame.grid(row = row, column = col)
            col += 1
            if col == 3:
                col = 0
                row += 1
                
    def __fill_lists(self):
        for listbox, list_generator in [
            (self.bus_list, self.db.get_buses),
            (self.driver_list, self.db.get_driver),
            (self.bustrip_list, self.db.get_bustrip),
            (self.destination_list, self.db.get_destination),
            (self.passenger_list, self.db.get_passenger),
            (self.ticket_list, self.db.get_tickets),
            ]:
            listbox.delete(0, END)
            for e in list_generator():
                listbox.insert(END, e)

    def __build_custom_frame(self, frame, get_fields, get_rus_fields, insert_foo, delete_foo):
        f = Frame(frame, name='subframe')
        i = 0
        for n in get_fields():
            m = get_rus_fields()[i]
            Label(f, text=m).grid(column = 0, row = i)
            self.vars.update({n:StringVar()})
            Entry(f, textvariable = self.vars[n], name=n).grid(column = 1, row = i)
            i += 1
        Button(f, text = "Добавить", command = insert_foo).grid(column = 0, row = i + 1)
        Button(f, text = "Удалить",  command = delete_foo).grid(column = 1, row = i + 1)
        f.pack()
        
    def __make_entries(self):
        for frame, get_names, get_rus_names, insert_foo, delete_foo in [
            (self.bus_frame, 
             self.db.get_bus_fields,
             self.db.get_bus_rus_fields,
             self.insert_bus,
             self.delete_bus),####
            (self.driver_frame,
             self.db.get_driver_fields,
             self.db.get_driver_rus_fields,
             self.insert_driver,
             self.delete_driver),####
            (self.bustrip_frame,
             self.db.get_bustrip_fields,
             self.db.get_bustrip_rus_fields,
             self.insert_bustrip,
             self.delete_bustrip),
            (self.destination_frame,
             self.db.get_destination_fields,
             self.db.get_destination_rus_fields,
             self.insert_destination,
             self.delete_destination),####
            (self.passenger_frame,
             self.db.get_passenger_fields,
             self.db.get_passenger_rus_fields,
             self.insert_passenger,
             self.delete_passenger),####
            (self.ticket_frame,
             self.db.get_ticket_fields,
             self.db.get_ticket_rus_fields,
             self.insert_ticket,
             self.delete_ticket),####
        ]:
            self.__build_custom_frame(frame, get_names, get_rus_names, insert_foo, delete_foo)

    def __init__(self):
        self.db = Database()
        
        self.__root = Tk()
        self.__make_frames()
        self.__make_lists()
        self.__place_frames()
        self.__make_entries()
        self.__fill_lists()

    def mainloop(self):
        self.__root.mainloop()

    def __get_fields(self, frame, get_db_fields):
        f = frame.children['subframe']
        return [ f.children[name].get() for name in get_db_fields() ]
    
    def insert_bus(self):
        listbox = self.bus_frame.children['!listbox']
        number, capacity, model, year, checkup, mileage = self.__get_fields(self.bus_frame, self.db.get_bus_fields)
        self.db.insert_bus(
            number = number,
            capacity = capacity,
            model = model,
            year = year,
            checkup = checkup,
            mileage = mileage
        )
        
        self.__fill_lists()

    def insert_driver(self):##
        listbox = self.driver_frame.children['!listbox']
        fullname, experience, categories, birthday, fines, snils = self.__get_fields(self.driver_frame,  self.db.get_driver_fields)
        self.db.insert_driver(
            fullname = fullname,
            experience = experience,
            categories = categories,
            birthday = birthday,
            fines = fines,
            snils = snils
        )
        
        self.__fill_lists()

    def insert_bustrip(self):##
        listbox = self.bustrip_frame.children['!listbox']
        number, destination, time = self.__get_fields(self.bustrip_frame,  self.db.get_bustrip_fields)
        self.db.insert_bustrips(
            number = number,
            destination = destination,
            time = time
        )
        
        self.__fill_lists()    

    def insert_destination(self):##
        listbox = self.destination_frame.children['!listbox']
        name = self.__get_fields(self.destination_frame,  self.db.get_destination_fields)[0]
        self.db.insert_destination(
            name = name
        )
        
        self.__fill_lists()

    def insert_passenger(self):##
        listbox = self.passenger_frame.children['!listbox']
        fullname = self.__get_fields(self.passenger_frame,  self.db.get_passenger_fields)[0]
        self.db.insert_passenger(
            fullname = fullname
        )
        
        self.__fill_lists()

    def insert_ticket(self):##
        listbox = self.ticket_frame.children['!listbox']
        price, bustrip, seats, passenger, date = self.__get_fields(self.ticket_frame,  self.db.get_ticket_fields)
        self.db.insert_ticket(
            price = price,
            bustrip = bustrip,
            seats = seats,
            passenger = passenger,
            date = date
        )
        
        self.__fill_lists()

    def delete_bus(self):####
        listbox = self.bus_frame.children['!listbox']
        self.db.delete_bus(number = self.bus_list.get(ACTIVE).split('|')[0].strip())
        
        self.__fill_lists()

    def delete_driver(self):####
        listbox = self.driver_frame.children['!listbox']
        self.db.delete_driver(snils = self.driver_list.get(ACTIVE).split('|')[0].strip())
        
        self.__fill_lists()

    def delete_bustrip(self):####
        listbox = self.bustrip_frame.children['!listbox']
        self.db.delete_bustrip(number = self.bustrip_list.get(ACTIVE).split('|')[0].strip())
        
        self.__fill_lists()

    def delete_destination(self):####
        listbox = self.destination_frame.children['!listbox']
        self.db.delete_destination(name = self.destination_list.get(ACTIVE).split('|')[0].strip())
        
        self.__fill_lists()

    def delete_passenger(self):####
        listbox = self.passenger_frame.children['!listbox']
        self.db.delete_passenger(fullname = self.passenger_list.get(ACTIVE).split('|')[0].strip())
        
        self.__fill_lists()

    def delete_ticket(self):####
        listbox = self.ticket_frame.children['!listbox']
        self.db.delete_ticket(
            bustrip   = self.ticket_list.get(ACTIVE).split('|')[1].strip(),
            passenger = self.ticket_list.get(ACTIVE).split('|')[3].strip(),
            date      = self.ticket_list.get(ACTIVE).split('|')[4].strip(),
        )
        
        self.__fill_lists()

if __name__ == "__main__":
    interface = Interface()
    interface.mainloop()
