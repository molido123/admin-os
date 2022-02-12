import pymysql

conn=pymysql.connect(host="127.0.0.1", port=3306,user="root",passwd="root",charset="utf8",db="studentall")
cursor=conn.cursor()


##sql2="""INSERT INTO student_view values ('02210621','huagenda','计算机学院','计算机科学','反斗花园','18361457436');"""

create_a_database="""CREATE TABLE student_view (
		studentId char(8) PRIMARY KEY ,
		name varchar(20) NOT NULL,
        departments varchar(20) not NULL,
        major varchar(20) not NULL,
        address varchar(20) not NULL,
        phone varchar(15) not NULL UNIQUE
        
		)ENGINE=innoDB DEFAULT CHARSET=utf8;"""






cursor.execute(create_a_database)
##cursor.execute(sql2)
conn.commit
cursor.close
conn.close

