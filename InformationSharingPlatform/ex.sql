DROP TABLE IF EXISTS experience;

CREATE TABLE experience (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content NOT NULL,
    company varchar(100),
    stu_id int(50),
    job varchar(100)
);