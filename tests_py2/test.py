#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('bot.db')
print "Opened database successfully";
c = conn.cursor()
c.execute('''CREATE TABLE TEST
       (NAME	      TEXT  NOT NULL,
        REACT         TEXT  NOT NULL);''')
print "Table created successfully";
conn.commit()
conn.close()
