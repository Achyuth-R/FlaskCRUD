from . import create_app
from . import DbConfig
from . import routes
from . import service

app = create_app()
DbConfig.initDb()