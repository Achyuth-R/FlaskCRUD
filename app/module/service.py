from app.module.models import db, TestTable

def create(id, name):
    try:
        dbObj = TestTable(id=id, name=name)
        db.session.add(dbObj)
        db.session.commit()
        return [True]
    except Exception as e:
        print("Failed to add data.")
        print(e)
        return [False,e]

def retrieveAllRecords():
    try:
        dbObj = TestTable.query.all()
        return [True,dbObj]
        
    except Exception as e:
        print("Failed to get data.")
        print(e)
        return([False, str(e)])
    

def retrieve(id):
    try:
        dbObj = TestTable.query.filter_by(id=id).first()
        return [True,dbObj]
        # return('Record retrieved from database with ID = {} name = {} '.format(dbObj.id, dbObj.name))
    except Exception as e:
        print("Failed to get data.")
        print(e)
        return[False,str(e)]

def update(id, name):
    try:
        dbObj = TestTable.query.filter_by(id=id).first()
        dbObj.name = name
        dbObj.id = id
        db.session.commit()
        return [True,dbObj]
        # return ('Record with ID = {} updated with name = {}'.format(id, name)) 
    except Exception as e:
        print("Failed to update data")
        print(e)
        return([False, str(e)])

def delete(id):
    try:
        dbObj = TestTable.query.filter_by(id=id).first()
        db.session.delete(dbObj)
        db.session.commit()
        return [True]
    except Exception as e:
        print("Failed to delete data")
        print(e)
        return[False, str(e)]