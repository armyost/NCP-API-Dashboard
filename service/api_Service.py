import json
import re
import hashlib
import hmac
import base64
import requests
import time

from flask import jsonify

## NCP의 대부분 API가 사용할 수 있도록 재사용성을 고려하였습니다.

class apiService:
    
    def __init__(self, api_dao, access_key, secret_key):       
        self.api_dao = api_dao
        self.secret_key = secret_key
        self.access_key = access_key
        
        global timestamp
        global method

        timestamp_integer = int(time.time() * 1000)
        timestamp = str(timestamp_integer)
        method="GET"

    ## HMAC으로 다이제스트한 SigningKey 도출
    def	make_signature(self, uri):
        secret_key = self.secret_key
        secret_key = bytes(secret_key, 'UTF-8')
        
        message = method + " " + uri + "\n" + timestamp + "\n" + self.access_key
        message = bytes(message, 'UTF-8')
        signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())
        signature=signingKey
        
        signature_only=re.search('b\'(.+?)\'', str(signature)).group(1)
        return signature_only
        
    ## API 호출 Service
    def send_api(self, signature_param, uri): 
        API_HOST = "https://ncloud.apigw.ntruss.com" 
					
        url = API_HOST + uri							
        headers = {
            'Content-Type': 'application/json',
            'charset': 'UTF-8',
            'Accept': '*/*',
            'x-ncp-apigw-timestamp': timestamp,
            'x-ncp-iam-access-key': self.access_key,
            'x-ncp-apigw-signature-v2': signature_param
            } 
        body = { 
            "key": "value"
        } 
        try: 
            if method == 'GET': 
                response = requests.get(url, headers=headers) 
            elif method == 'POST': 
                response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t")) 
            print("response status %r" % response.status_code) 
            print("response text %r" % response.text) 
        except Exception as ex: 
            print(ex)
        return response

    def insert_data_serverInstance(self, row):
        self.api_dao.insert_data_serverInstance(row)