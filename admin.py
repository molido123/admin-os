#!/usr/bin/python
import json
from flask import Flask, request ,jsonify,make_response
import pymysql
from flask_cors import CORS
import jwt212 
app=Flask(__name__)
CORS(app)
jwt_all=jwt212.jwt212

@app.route('/admin/del/<student_Id>',methods=["post"])##删除功能
def delete(student_Id):    
    ################################
    token=request.headers.get('token')#获取请求头中的token
    data=jwt_all.token_query(token)#获取token中的payload
    id=data.get("studentId")
    sql_check="SELECT password FROM user WHERE studentId='%s';"%(id)
   
    conn=pymysql.connect(host="127.0.0.1", port=3306,user="debian-sys-maint",passwd="xfMr9uNCKXGAT9au",charset="utf8",db="studentall")
    cursor=conn.cursor()
    cursor.execute(sql_check)
    password=cursor.fetchone()[0]##获取到密码
    cursor.close()
    conn.close()
     
    
    if jwt_all.token_check(token,password)==True and data.get("identity")=="admin":##确保签名正确且权限为admin
    ###############################################检验token的合法性##########################################################
        try:     
            if student_Id.isdigit():##检测学号是否为数字
                conn=pymysql.connect(host="127.0.0.1", port=3306,user="debian-sys-maint",passwd="xfMr9uNCKXGAT9au",charset="utf8",db="studentall")
                cursor=conn.cursor()
                sql="delete from student_view where studentId=%s;"%(student_Id)
                cursor.execute(sql)
                conn.commit()
                cursor.close()
                conn.close()
                return {"code": 200, "data": None, "message": "成功" },200,[("Access-Control-Allow-Origin","*")]
        except Exception as e:
            print(e)
            return {"code":400, "data":None,"message":"请求失败"},400,[("Access-Control-Allow-Origin","*")]
    ###########################################################################################################
    else:
        return {"code":401,"message":"Not enough clearance"},401,[("Access-Control-Allow-Origin","*")]


@app.route('/admin/query',methods=["post"])#查询
def query():
##########################################################################################    
    token=request.headers.get('token')#获取请求头中的token
    data=jwt_all.token_query(token)#获取token中的payload
    id=data.get("studentId")
    sql_check="SELECT password FROM user WHERE studentId='%s';"%(id)
   
    conn=pymysql.connect(host="127.0.0.1", port=3306,user="debian-sys-maint",passwd="xfMr9uNCKXGAT9au",charset="utf8",db="studentall")
    cursor=conn.cursor()
    cursor.execute(sql_check)
    password=cursor.fetchone()[0]##获取到密码
    cursor.close()
    conn.close()
     
    if jwt_all.token_check(token,password)==True and data.get("identity")=="admin":##确保签名正确且权限为admin
#########################################################################################    
        dict=request.get_json()
        id=dict.get("studentId",0)
        print(id)
        if id.isdigit():
            try:    
                conn=pymysql.connect(host="127.0.0.1", port=3306,user="debian-sys-maint",passwd="xfMr9uNCKXGAT9au",charset="utf8",db="studentall")
                cursor=conn.cursor()
                sql="select * from student_view where studentId=%s"%(id)
                cursor.execute(sql)
                result=cursor.fetchone()
                cursor.close()
                conn.close()
                re_dict={"studentId":result[0],"name":result[1],"departments":result[2],"major":result[3],"address":result[4],"phone":result[5]}
                res=make_response(re_dict)
                res.status = '200' # 设置状态码
                res.headers["Access-Control-Allow-Origin"]="*"
                return res
            except Exception as e:
                print(e)
                return {"code":400, "data":None,"message":"请求失败"},400,[("Access-Control-Allow-Origin","*")]
 ######################################################################################################################   
    else:
        return {"code":401,"message":"Not enough clearance"},401,[("Access-Control-Allow-Origin","*")]


@app.route('/admin/getall',methods=["post"])#获取全部
def all():
#########################################################################################    
    token=request.headers.get('token')#获取请求头中的token
    data=jwt_all.token_query(token)#获取token中的payload
    
    id=data.get("studentId")
    
    sql_check="SELECT password FROM user WHERE studentId='%s';"%(id)
   
    conn=pymysql.connect(host="127.0.0.1", port=3306,user="debian-sys-maint",passwd="xfMr9uNCKXGAT9au",charset="utf8",db="studentall")
    cursor=conn.cursor()
    cursor.execute(sql_check)
    password=cursor.fetchone()[0]##获取到密码
    cursor.close()
    conn.close()
     
    if jwt_all.token_check(token,password)==True and data.get("identity")=="admin":##确保签名正确且权限为admin    
############################################################################################        
        try:
            conn=pymysql.connect(host="127.0.0.1", port=3306,user="debian-sys-maint",passwd="xfMr9uNCKXGAT9au",charset="utf8",db="studentall")
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
            return json.dumps(re_list,ensure_ascii=False),200,[("Access-Control-Allow-Origin","*")]

        except Exception as e:
            print(e)
            return {"code":400, "data":None,"message":"请求失败"},400,[("Access-Control-Allow-Origin","*")]
##################################################################################################################
    else:
        return {"code":401,"message":"Not enough clearance"},401,[("Access-Control-Allow-Origin","*")]



@app.route('/admin/modify',methods=["post"])###修改
def modify():
#############################################################################
    token=request.headers.get('token')#获取请求头中的token
    data=jwt_all.token_query(token)#获取token中的payload
    
    id=data.get("studentId")
    
    sql_check="SELECT password FROM user WHERE studentId='%s';"%(id)
   
    conn=pymysql.connect(host="127.0.0.1", port=3306,user="debian-sys-maint",passwd="xfMr9uNCKXGAT9au",charset="utf8",db="studentall")
    cursor=conn.cursor()
    cursor.execute(sql_check)
    password=cursor.fetchone()[0]##获取到密码
    cursor.close()
    conn.close()
     
    if jwt_all.token_check(token,password)==True and data.get("identity")=="admin":##确保签名正确且权限为admin  

#########################################################################
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
            conn=pymysql.connect(host="127.0.0.1", port=3306,user="debian-sys-maint",passwd="xfMr9uNCKXGAT9au",charset="utf8",db="studentall")
            cursor=conn.cursor()
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            state={"code": 200, "data":"upgraded", "message": "成功" }
            res=make_response(state)
            res.status="200"
            res.headers["Access-Control-Allow-Origin"]="*"
            return  res
        except Exception as e:
            print(e)
            return {"code":400, "data":None,"message":"请求失败"},400,[("Access-Control-Allow-Origin","*")]
#################################################################################################################
    else:
        return {"code":401,"message":"Not enough clearance"},401,[("Access-Control-Allow-Origin","*")]

@app.route('/user/register',methods=['post'])
def register():
    try:
        dict=request.get_json()
        print(dict)
        id=dict.get("studentId")#得到请求中的学号
        password_register=dict.get("password")#得到请求中的密码
        sql_exe="update user set password='%s' where studentId='%s';"%(password_register,id)#增加密码语句
        sql_id="SELECT name FROM user WHERE studentId='%s';"%(id)#从库里查名
        sql_identity="SELECT identity FROM user WHERE studentId='%s';"%(id)
        
        conn=pymysql.connect(host="127.0.0.1", port=3306,user="debian-sys-maint",passwd="xfMr9uNCKXGAT9au",charset="utf8",db="studentall")
        cursor=conn.cursor()
        sql_check="SELECT password FROM user WHERE studentId='%s';"%(id)#检测密码是否存在
        cursor.execute(sql_check)
        password=cursor.fetchone()[0]##获取到密码,检查是否已经注册
        cursor.close()
        conn.close()
       
        conn=pymysql.connect(host="127.0.0.1", port=3306,user="debian-sys-maint",passwd="xfMr9uNCKXGAT9au",charset="utf8",db="studentall")
        cursor=conn.cursor()
        cursor.execute(sql_id)
        name=cursor.fetchone()[0]#查询是否有此人
        cursor.close()
        conn.close()
        print(name)
        if name==None:#学号不存在
            state={"code":1004,"message":"用户不存在，请检查学号"}
            print(state)
            res=make_response(state)
            res.headers["Access-Control-Allow-Origin"]="*"
            return res
        elif name!=None and password==None:##校验没问题,予以注册成功
            conn=pymysql.connect(host="127.0.0.1", port=3306,user="debian-sys-maint",passwd="xfMr9uNCKXGAT9au",charset="utf8",db="studentall")
            cursor=conn.cursor()
            cursor.execute(sql_exe)
            conn.commit()    
            cursor.close()
            conn.close()
#######下面要取得他的身份
            conn=pymysql.connect(host="127.0.0.1", port=3306,user="debian-sys-maint",passwd="xfMr9uNCKXGAT9au",charset="utf8",db="studentall")
            cursor=conn.cursor()
            cursor.execute(sql_identity)
            identity=cursor.fetchone()
            cursor.close()
            conn.close()
########################            
            token=jwt_all.login_create_token(id,password_register,identity)##制造token
            state={"code": 200, "data": {"token":token},"message": "成功" }
            res=make_response(state)
            res.status="200"
            res.headers["Access-Control-Allow-Origin"]="*"
            return res

        else:
            state={"code":1001,"message":"此学号已经注册了"}
            res=make_response(state)
            res.headers["Access-Control-Allow-Origin"]="*"
            return res

    except Exception as e:
            print(e)
            return {"code":400, "data":None,"message":"请求失败"},400,[("Access-Control-Allow-Origin","*")]



@app.route("/login",methods=["post"])
def login():
    dict=request.get_json()
    id=dict.get("studentId")#得到请求中的学号
    password=dict.get("password")#得到请求中的密码
 ##获取到密码,检查密码是否正确  
    conn=pymysql.connect(host="127.0.0.1", port=3306,user="debian-sys-maint",passwd="xfMr9uNCKXGAT9au",charset="utf8",db="studentall")
    cursor=conn.cursor()
    sql_check="SELECT password FROM user WHERE studentId='%s';"%(id)#检测密码是否存在
    cursor.execute(sql_check)
    password_sql=cursor.fetchone()##获取到密码,检查密码是否正确
    cursor.close()
    conn.close()
    if password_sql==None:
        return {"code":1005, "data":None,"message":"密码错误或用户不存在"},1005,[("Access-Control-Allow-Origin","*")]
    elif password_sql!=None:
        password_sql=password_sql[0]
        if password_sql==password:##密码正确且用户存在
        #####获取身份 
            conn=pymysql.connect(host="127.0.0.1", port=3306,user="debian-sys-maint",passwd="xfMr9uNCKXGAT9au",charset="utf8",db="studentall")
            cursor=conn.cursor()
            sql_identity="SELECT identity FROM user WHERE studentId='%s';"%(id)
            cursor.execute(sql_identity)
            identity=cursor.fetchone()
            cursor.close()
            conn.close()
            if identity==None:
                 pass
            elif identity!=None:
                identity=identity[0]
            token=jwt_all.login_create_token(id,password,identity)##制造token
            state={"code": 200, "data": {"token":token},"message": "成功" }
            res=make_response(state)
            res.status="200"
            res.headers["Access-Control-Allow-Origin"]="*"
            return res
        else:
            return {"code":1005, "data":None,"message":"密码错误或用户不存在"},1005,[("Access-Control-Allow-Origin","*")]



  
if __name__=="__main__":
    app.run(host="0.0.0.0")