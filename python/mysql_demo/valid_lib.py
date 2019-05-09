#!/usr/bin/python
# -*- coding:utf-8 -*-
import MySQLdb

# open
db = MySQLdb.connect("localhost", "root", "123456", "test", charset='utf8' )
# cursor()
cursor = db.cursor()
# execute execute sql 
cursor.execute('select database()')
# fetchone() fetch a data
data = cursor.fetchone()
print("Database current : %s " % data)

cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print("Database version : %s " % data)

db.close()
