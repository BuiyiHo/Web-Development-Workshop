DROP TABLE IF EXISTS Toffer;

CREATE TABLE Toffer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    GPA float(10),
    date date(20),
    university varchar(50),
    qs int(10),
    place varchar(50),
    program varchar(50)
);

DROP TABLE IF EXISTS Coffer;

CREATE TABLE Coffer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    GPA float(10),
    date NOT NULL,
    company varchar,
    title varchar
);

DROP TABLE IF EXISTS Roffer;

CREATE TABLE Roffer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    GPA INTEGER NOT NULL,
    date NOT NULL,
    university varchar,
    program varchar,
    supervisor varchar,
    topic varchar,
    qs int(10),
    NOpapers INTEGER,
    NOresearch INTEGER,
    place varchar(30)
);

DROP TABLE IF EXISTS Generate;

CREATE TABLE Generate (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    year int(10)
)