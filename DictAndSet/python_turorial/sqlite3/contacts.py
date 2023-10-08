import sqlite3

db = sqlite3.connect("contacts.sqlite")

db.execute("CREATE TABLE contatcs (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contatcs (name, phone, email) VALUES ('Tim', 654321, 'tim@email.com')")
