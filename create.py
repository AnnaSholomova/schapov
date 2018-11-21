create = [
"""CREATE TABLE buses
(
    number text PRIMARY KEY,
    capacity integer,
    model text, 
    year integer,
    checkup integer,
    mileage integer
);""",

"""CREATE TABLE driver
(
    fullname text,
    experience integer,
    categories text,
    birthday text,
    fines text,
    snils integer PRIMARY KEY
);""",

"""CREATE TABLE tickets
(
    price integer,
    bustrips text,
    seats integer,
    passenger text,
    date text
);""",

"""CREATE TABLE bustrips
(
    number integer,
    destination text PRIMARY KEY,
    time text
);""",

"""CREATE TABLE destination
(
    name text PRIMARY KEY
);""",

"""CREATE TABLE passenger
(
    fullname text PRIMARY KEY
);""",
]

