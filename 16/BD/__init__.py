import sqlite3 as sq
with sq.connect('АПТЕКА.db') as con:
 cur = con.cursor()
 cur.execute("""CREATE TABLE IF NOT EXISTS Лекарственные_средства (
 code INTEGER PRIMARY KEY AUTOINCREMENT,
 name_of_the_medicine TEXT NOT NULL,
 application TEXT NOT NULL,
 quantity INTEGER,
 price INTEGER,
 country_of_origin TEXT NOT NULL)""")
