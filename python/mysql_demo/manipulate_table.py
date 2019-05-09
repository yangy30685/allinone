#!/usr/bin/python
# -*- coding:utf-8 -*-

import mysql.connector as mc

cnn = mc.connect(user='root',passwd='123456', database='test')
cursor = cnn.cursor()
cursor.execute('drop table if exists employee')

cursor.execute('drop table if exists student')
# create a table by sql
sql_0 = '''create table employee 
        (id int not null auto_increment,
        first_name  char(20) not null,
        last_name  char(20),
        age int,  
        gender char(6),
        income float,
        primary key(id)
        )'''
cursor.execute(sql_0)

# show table
sql_1 = 'describe employee'
cursor.execute(sql_1)
info_1 = cursor.fetchall()
print('info_1 : ', type(info_1))

for i in range(1, 10):
  
    # insert a value
    sql_2 = '''insert into employee 
            (id, first_name, last_name, age, gender, income)
            values ({}, 'mac_air','apple', {}, 'male', {})'''.format(i, 10+i, 10*i**2)
    try:
        cursor.execute(sql_2)
        cnn.commit()
    except:
        # Rollback in case there is any error
        cnn.rollback()

# show data
sql_3 = 'select * from employee'
cursor.execute(sql_3)
info_3 = cursor.fetchall()
print('info_3 : ', type(info_3))

# show data on condition
sql_4 = '''select * from employee 
        where id >{}'''.format(4)
try:
    cursor.execute(sql_4)
    info_4 = cursor.fetchall()
    print('info_4 : ', type(info_4))
    for row in info_4:
        print('id={},first_name={},last_name={},age={},gender={},income={}'.format(row[0],row[1],row[2],row[3],row[4],row[5]))
except:
    print("Error!!!")


# close connect
cnn.close()
