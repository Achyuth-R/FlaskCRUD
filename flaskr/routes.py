from flask import request
from . import get_app
from . import service

app = get_app()


@app.get("/")
def hello():
    return('hello')

#127.0.0.1:5000/create
@app.get("/create")
def createRecord():
    data = request.get_json()
    id = data["id"]
    name = data["name"]
    return service.create(id, name)

#127.0.0.1:5000/retrieve
@app.get("/retrieve")
def retrieveRecord():
    data = request.get_json()
    id = data["id"]
    return service.retrieve(id)

#127.0.0.1:5000/update
@app.get("/update")
def updateRecord():
    data = request.get_json()
    id = data["id"]
    name = data["name"]
    return service.update(id,name)
    
#127.0.0.1:5000/delete
@app.get("/delete")
def deleteRecord():
    data = request.get_json()
    id = data["id"]
    return service.delete(id)