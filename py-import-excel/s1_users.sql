-- (A) USERS TABLE
CREATE TABLE users (
  uid INTEGER,
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  tel TEXT NOT NULL,
  PRIMARY KEY("uid" AUTOINCREMENT)
);