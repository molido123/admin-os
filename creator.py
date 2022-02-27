#!/usr/bin/python
from unittest import result
import pymysql

conn=pymysql.connect(host="127.0.0.1", port=3306,user="root",passwd="root",charset="utf8",db="studentall")
cursor=conn.cursor()


##sql2="""INSERT INTO student_view values ('02210621','华根达','计算机魔法学院','计算神秘学','幻想乡','18361457436');"""
sql5="""SELECT password FROM user WHERE name="华根达";"""
create_a_database="""CREATE TABLE student_view (
		studentId char(8) PRIMARY KEY,
		name varchar(20) NOT NULL,
        departments varchar(30) not NULL,
        major varchar(50) not NULL,
        address varchar(50) not NULL,
        phone varchar(15) not NULL UNIQUE
		)ENGINE=innoDB DEFAULT CHARSET=utf8;"""
create_user_database="""
        CREATE TABLE user (
		studentId char(8) PRIMARY KEY,
		name varchar(20) NOT NULL,
        password varchar(20),
        identity varchar(20)
		)ENGINE=innoDB DEFAULT CHARSET=utf8;"""




#cursor.execute(create_a_database)
#cursor.execute(create_user_database)
cursor.execute(sql5)
result=cursor.fetchone()
print(result[0])
##cursor.execute(sql2)
conn.commit
cursor.close
conn.close

