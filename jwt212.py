#!/usr/bin/python
import time
import json
import base64
import hashlib
import hmac


class jwt212:
    def login_create_token(studentId,password,identity):#登陆时用，分配token。用于检验信息正确之后，此函数无检验功能
        exp = 14400#10天后过期，需再次登录。


        headers = {
        "typ": "token",
        "exp": int(time.time() + exp)  # 过期时间戳
        }

        payload = {
        "studentId":studentId ,
        "identity":identity
        }

        # 生产header
        first = base64.urlsafe_b64encode(json.dumps(headers, separators=(',', ':')).encode('utf-8').replace(b'=', b'')).decode('utf-8').replace('=', '')
        # 生成payload
        second = base64.urlsafe_b64encode(json.dumps(payload, separators=(',', ':')).encode('utf-8').replace(b'=', b'')).decode('utf-8').replace('=', '')
        first_second = f"{first}.{second}"
        # 生成签名
        third = base64.urlsafe_b64encode(hmac.new(password.encode('utf-8'), first_second.encode('utf-8'), hashlib.sha256).digest()).decode('utf-8').replace('=','')

        # 拼接成token
        token = ".".join([first, second, third])
        return token
    

    def token_check(token,password):##一定要提供密码
        headers_check = token.split(".")[0]#头部
        payload_check = token.split(".")[1]#内容
        sign_check = token.split(".")[2]#签名
        # 对数据签名、判断token上对签名是否是合规对
        headers_payload_check = f"{headers_check}.{payload_check}"
        new_sign = base64.urlsafe_b64encode(hmac.new(password.encode('utf-8'), headers_payload_check.encode('utf-8'), hashlib.sha256).digest()).decode('utf-8').replace('=','')
        #下面解码，看时间对不对
            ################################
        if isinstance(headers_check, str):
            headers_check = headers_check.encode('ascii')
        rem = len(headers_check) % 4
        if rem > 0:
            headers_check += b'=' * (4 - rem)
        # 上面这一部分是解密的部分数据补全格式
        header_data = base64.urlsafe_b64decode(headers_check)  # 解码
        data = json.loads(header_data) 
        
        time_past=int(data.get("exp"))#获取过期时间
        time_right_now=int(time.time()) #获取现在时间
        if sign_check==new_sign and time_right_now<=time_past:#检查签名合法和时间
            return True
        else:
            return False
    
    
    
    def token_query(token):
            payload = token.split(".")[1]#内容
            ################################
            if isinstance(payload, str):
                payload = payload.encode('ascii')
            rem = len(payload) % 4
            if rem > 0:
                payload += b'=' * (4 - rem)
            ############################################################
            payload_data = base64.urlsafe_b64decode(payload)  # 解码
            data = json.loads(payload_data)  # 将已编码的JSON字符串解码为Python对象，即将payload转为可以通过get方法获取里面的值
            return data  # 返回payload的数据



 