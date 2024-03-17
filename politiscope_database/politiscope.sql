CREATE TABLE IF NOT EXISTS t_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT COLLATE NOCASE,
    email TEXT UNIQUE COLLATE NOCASE,
    password TEXT
);

-- Delete all records from the table
DELETE FROM t_users;

-- Reset the ID key
DELETE FROM sqlite_sequence WHERE name = 't_users';
