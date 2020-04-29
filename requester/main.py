from flask import Flask

from .config import configuration
from .api.setup import setup_api
from .database.setup import setup_database


app = Flask(__name__)

app.config.update(configuration)
setup_api(app)
setup_database(app)
