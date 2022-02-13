
from cmath import e
import json
from logging import exception
from sqlite3 import SQLITE_OK
from unittest import result
from flask import Flask, request ,jsonify
import pymysql
from sqlalchemy import delete
app=Flask(__name__)


@app.route('/admin/del/<student_Id>',methods=["delete"])##删除功能
def delete(student_Id):
    
    try:     
        if student_Id.isdigit():##检测学号是否为数字
            conn=pymysql.connect(host="127.0.0.1", port=3306,user="root",passwd="root",charset="utf8",db="studentall")
            cursor=conn.cursor()
            sql="delete from student_view where studentId=%s;"%(student_Id)
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            return {"code": 200, "data": None, "message": "成功" }
    except Exception as e:
        print(e)
        return {"code":400, "data":None,"message":"请求失败"}

@app.route('/admin/query',methods=["post"])#查询
def query():
    dict=request.get_json()
    id=dict.get("studentId",0)
    print(id)
    if id.isdigit():
        try:    
            conn=pymysql.connect(host="127.0.0.1", port=3306,user="root",passwd="root",charset="utf8",db="studentall")
            cursor=conn.cursor()
            sql="select * from student_view where studentId=%s"%(id)
            cursor.execute(sql)
            result=cursor.fetchone()
            cursor.close()
            conn.close()
            re_dict={"studentId":result[0],"name":result[1],"departments":result[2],"major":result[3],"address":result[4],"phone":result[5]}
            return re_dict
        except Exception as e:
            print(e)
            return {"code":400, "data":None,"message":"请求失败"}

@app.route('/admin/getall',methods=["post"])#获取全部
def all():
    try:
        conn=pymysql.connect(host="127.0.0.1", port=3306,user="root",passwd="root",charset="utf8",db="studentall")
        cursor=conn.cursor()
        cursor.execute("select * from student_view;")
        result=cursor.fetchall()
        cursor.close()
        conn.close()
        re_list=[]
       # print(result)
        for i in result:
            re_dict={"studentId":i[0],"name":i[1],"departments":i[2],"major":i[3],"address":i[4],"phone":i[5]}
            re_list.append(re_dict)
        return json.dumps(re_list,ensure_ascii=False)

    except Exception as e:
        print(e)
        return {"code":400, "data":None,"message":"请求失败"}

@app.route('/admin/modify',methods=["post"])###修改，未完工,整体思路没问题，sql语法不知道哪错了
def modify():
    try:
        dict=request.get_json()
        #print(dict)
        id=dict.get("studentId",0)
        name=dict.get("name",0)
        departments=dict.get("departments",0)
        major=dict.get("major",0)
        print(major)
        address=dict.get("address",0)
        phone=dict.get("phone",0)
        sql="update student_view set studentId='%s',name='%s',departments='%s',major='%s',address='%s',phone='%s' where studentId='%s';"%(id,name,departments,major,address,phone,id)   
        print(sql)
        conn=pymysql.connect(host="127.0.0.1", port=3306,user="root",passwd="root",charset="utf8",db="studentall")
        cursor=conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return  {"code": 200, "data":"upgraded", "message": "成功" }
    except Exception as e:
        print(e)
        return {"code":400, "data":None,"message":"请求失败"}





if __name__=="__main__":
    app.run()