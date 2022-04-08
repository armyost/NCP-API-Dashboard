
import json

def create_endpoints(app, services):
    api_service  = services.api_service

    @app.route("/ping", methods=['GET'])
    def ping():
        return "pong"

    @app.route("/apicall_test1", methods=['GET'])
    def apicall_test1():

        uri="/server/v2/getServerInstanceList?responseFormatType=json"

        ## 서명값 추출
        signature = api_service.make_signature(uri)

        ## NCP에 API 호출
        response=api_service.send_api(signature, uri)

        ## Response 받은 String을 Json으로 변환 후 Parsing
        json_response=response.json()
        jsonArray = json_response['getServerInstanceListResponse']['serverInstanceList']
        
        ## 서버 정보를 JSON Array에 맞추어서 반복적으로 저장
        for serverInstanceNo in jsonArray:
            api_service.insert_data_serverInstance(serverInstanceNo)
        return '', 200


## 필요에따라 EndPoint를 추가만 하면 다른 지표를 수집할 수 있습니다. 다만, 이곳과 더불어 Dao도 손을대야 합니다.