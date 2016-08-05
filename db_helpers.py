from FlaskWebProject import app
from shared_consts import DB_ACCESS_MODULE
import importlib
import FlaskWebProject


def import_db_access_module():
    module_name = app.config[DB_ACCESS_MODULE]
    return importlib.import_module('FlaskWebProject.steershared.' + module_name)
