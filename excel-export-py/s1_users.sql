-- (A) USERS TABLE
CREATE TABLE users (
  uid INTEGER,
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  tel TEXT NOT NULL,
  PRIMARY KEY("uid" AUTOINCREMENT)
);

-- (B) DUMMY DATA
INSERT INTO "users" VALUES
(1,'Jo Doe','jo@doe.com','465785'),
(2,'Joa Doe','joa@doe.com','123456'),
(3,'Job Doe','job@doe.com','234567'),
(4,'Joe Doe','joe@doe.com','345678'),
(5,'Jog Doe','jog@doe.com','578456'),
(6,'Joh Doe','joh@doe.com','378945'),
(7,'Joi Doe','joi@doe.com','456789'),
(8,'Jon Doe','jon@doe.com','987654'),
(9,'Jor Doe','jor@doe.com','754642'),
(10,'Joy Doe','joy@doe.com','124578');
