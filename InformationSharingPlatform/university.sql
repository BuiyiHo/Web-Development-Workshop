DROP TABLE IF EXISTS universitylist;

CREATE TABLE universitylist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name varchar(100),
    qs int(10),
    program varchar(20),
    place varchar(100)
);