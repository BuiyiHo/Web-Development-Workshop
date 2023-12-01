DROP TABLE IF EXISTS userinfo;

CREATE TABLE userinfo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username varchar(100),
    password varchar(20),
    status varchar(20)
);


