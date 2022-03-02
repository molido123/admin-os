//创建用户名为 test2              密码为test2 的用户
    create user 'root'@'%' identified by 'root';
//授予用户test2 所有权限    
    grant all privileges on *.* to test2@'%' identified by 'test2';
//删除用户
    drop user test@'%';
(mysql语句结尾需加 ";")

![image-20220213231041445](C:\Users\HP\AppData\Roaming\Typora\typora-user-images\image-20220213231041445.png)

user     = debian-sys-maint
password = xfMr9uNCKXGAT9au

conn=pymysql.connect(host="127.0.0.1", port=3306,user="debian-sys-maint",passwd="xfMr9uNCKXGAT9au",charset="utf8",db="studentall")
conn=pymysql.connect(host="127.0.0.1", port=3306,user="root",passwd="root",charset="utf8",db="studentall")