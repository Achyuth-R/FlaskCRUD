from . import create_app
from . import DbConfig
from . import routes
from . import service

conn = DbConfig.initDb()
app = create_app()
