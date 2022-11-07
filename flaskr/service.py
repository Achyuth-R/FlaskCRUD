from . import DbConfig

dbconn = DbConfig.getConnection()
print(dbconn)

def create(id = "1", name = "achyuth"):
    dbcurr = dbconn.cursor()
    query = 'INSERT INTO TestSchema.TestTable ( id, name) VALUES (%s, %s)'
    dbcurr.execute(query, (id, name))
    dbconn.commit()
    return('Inserted in database values with ID = {} and name = {}'.format(id, name))

def retrieve(id = '1'):
    dbcurr = dbconn.cursor()
    query = 'SELECT * FROM TestSchema.TestTable Where ID = %s'
    dbcurr.execute(query,(id))
    data = dbcurr.fetchone()
    return('Record retrieved from database with ID = {} name = {} '.format(id,data[1]))


def update(id = '1', name = 'anand'):
    dbcurr = dbconn.cursor()
    query = 'UPDATE TestSchema.TestTable SET name =%s WHERE ID = %s'
    dbcurr.execute(query,(name, id))
    return ('Record with ID = {} updated with name = {}'.format(id, name)) 

def delete(id = '1'):
    dbcurr = dbconn.cursor()
    query = 'DELETE FROM TestSchema.TestTable WHERE ID = %s'
    dbcurr.execute(query, (id))
    return('Deleted record with ID = {}'.format(id))