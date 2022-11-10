from flask import request, jsonify
from app import app
from app.module import service

@app.get("/")
def hello():
    return('hello')

#127.0.0.1:5000/api/records
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
        
        
    elif(request.method == 'POST'):
        data = request.get_json()
        id = data["id"]
        name = data["name"]
        resp = service.create(id, name)        
        if(resp[0]):
            return jsonify({'status':'created',
                            'data':data}),201
        else:
            return jsonify({'status':'error',
                            'Error_Msg' : resp[1]}),500

#127.0.0.1:5000/api/records/<id>
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