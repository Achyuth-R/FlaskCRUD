import configparser

def Config(filename='app/database.ini',section='database'):
    parse = configparser.ConfigParser()
    parse.read(filename)
    db=0
    if parse.has_section(section):
        param = parse.items(section)
        # for params in param:
        #     db=params[1]
        DatabaseName=param[0][1]
        DatabaseEngine=param[1][1]
        DatabaseUser=param[2][1]
        DatabasePassword=param[3][1]
        DatabaseLocation=param[4][1]
        db = "{0}://{1}:{2}@{3}/{4}".format(DatabaseEngine,DatabaseUser,DatabasePassword,DatabaseLocation,DatabaseName)
        print(f"Connecting to URL {0}",db)
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db