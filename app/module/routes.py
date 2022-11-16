from flask import request, jsonify
import json
from app import app
from app.module import service
from app.module import Config

#127.0.0.1:8000/api
@app.get("/")
@app.get("/api")
def hello():
    APIDesc = Config.APIDescConfig()
    return APIDesc,200,{'Content-Type': 'application/JSON'}

#127.0.0.1:8000/api/records
@app.route('/api/records', methods=['GET','PUT'])
def handleRecordsFun():
    if(request.method == 'GET'):
        result = service.retrieveAllRecords()
        if(result[0]):
            resAsJson = [
                    {
                        "id": record.id,
                        "name": record.name
                            } for record in result[1]]
            
            return jsonify({'status':'retreived',
                            'data':resAsJson}), 200
        else:
            return jsonify({'status':'error',
                            'Error_Msg':result[1]}),500
        
        
    elif(request.method == 'PUT'):
        data = request.get_json()
        id = data["id"]
        name = data["name"]
        resp = service.create(id, name)        
        if(resp[0]):
            return jsonify({'status':'created','data':data}),201
        else:
            return jsonify({'status':'error','Error_Msg' : resp[1]}),500


#127.0.0.1:8000/api/records/bulk_create
@app.route('/api/records/bulk_create', methods = ["PUT"])
def handleBulkRecord():
    ReqBody = request.get_json()
    ReqData = ReqBody["data"]
    RespArray=[]
    if(len(ReqData)<=5):
        for record in ReqData:
            id = record["id"]
            name = record["name"]
            ServiceResp = service.create(id, name)
            if(ServiceResp[0]):
                RespArray.append({'status':'created','data':record})
            else:
                RespArray.append({'status':'error','Error_Msg' : ServiceResp[1]})
        JsonDataResp = {"data":RespArray}
        return json.dumps(JsonDataResp),200,{'Content-Type': 'application/JSON'}
    else:
        ErrResp = {"error":"Bulk create should have less than 5 entries"}
        return json.dumps(ErrResp, indent=1),400,{'Content-Type': 'application/JSON'}


#127.0.0.1:8000/api/records/<id>
@app.route('/api/records/<id>', methods = ["GET","POST","DELETE"])
def handleIndividualRecordFun(id):

    if(request.method == 'GET'):
        resp = service.retrieve(id)
        if(resp[0]):
            data = convert_to_Json(resp[1])
            return jsonify({'data':data}), 200
        else:
            return jsonify({'status':'error',
                            'error_msg':resp[1]}), 500

    if(request.method == 'POST'):
        data = request.get_json()
        resp = service.update(id, data['name'])
        JsonResp = {'id':id,
                    'name':data}
        if(resp[0]):
            return jsonify({'status':'udpated',
                            'data': JsonResp}), 200
        else:
            return jsonify({'status':'error',
                            'error_msg':resp[1]}), 500
    if(request.method == 'DELETE'):
        resp = service.delete(id)
        if(resp[0]):
            return jsonify({'status':'deleted'}), 200
        else:
            return jsonify({'status':'error',
                            'error_msg':resp[1]}), 500

def convert_to_Json(data):
    resp = {'id' : data.id,
            'name' : data.name}
    return resp