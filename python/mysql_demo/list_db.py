#!/usr/bin/python
# -*- coding:utf-8 -*-

import mysql.connector as mc

# print(mysql.__file__)
# print

# connect 
cnn = mc.connect(user='root', passwd='123456',database='test')
# get cursor
cursor = cnn.cursor()

# if exist then delete
sql_1 = 'show databases'
cursor.execute(sql_1)
info_1 = cursor.fetchall()
print('databases are:{}'.format(info_1))

sql_2 = 'select database()'
cursor.execute(sql_2)
info_2 = cursor.fetchall()
print('current database : {}'.format(info_2))

sql_3 = 'show tables'
cursor.execute(sql_3)
info_3 = cursor.fetchall()
print('tables : {}'.format(info_3))

# close connect
cnn.close()
