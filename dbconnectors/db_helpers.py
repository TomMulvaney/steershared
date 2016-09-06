from FlaskWebProject import app
from FlaskWebProject.steershared.shared_consts import *
import importlib


def rename_attrs(collection_id, attrs, db=None):
    if not db:
        db = get_db(app.config[DB_ACCESS_MODULE])
    docs = db.read(collection_id)
    for doc in docs:
        for old_attr, new_attr in attrs.iteritems():
            doc[new_attr] = doc[old_attr]
            del doc[old_attr]
    db.replace(collection_id, docs)


def import_db_connector_module(module_name=app.config[DB_ACCESS_MODULE]):
    return importlib.import_module(module_name)


def get_db(headers):
    try:
        mode = str(headers[MODE_HEADER_KEY])
    except (KeyError, TypeError):
        if type(headers) is unicode:
            headers = str(headers)
        # Check if it's a str because we used to have a mode (str) argument instead of headers
        mode = headers if type(headers) is str else app.config[DEFAULT_MODE]

    try:
        db_module_name = headers[DB_HEADER_KEY]
    except (KeyError, TypeError):
        db_module_name = app.config[DB_ACCESS_MODULE]

    db_module = importlib.import_module('{0}.{1}'.format(app.config[DB_PACKAGE_PATH], db_module_name))

    key = '{0}_{1}'.format(db_module_name, mode)
    if key not in _dbs.keys():
        _dbs[key] = db_module.gen_connector(mode)
    return _dbs[key]


def add_ids(docs, ids):
    zipped = zip(docs, ids)
    for doc, id_ in zipped:
        doc[ID] = id_


# Private variables
_dbs = {}

if __name__ == '__main__':
    db_config = {DB_ACCESS_MODULE: 'mongodb_connector', MODE_HEADER_KEY: DEBUG}
    db_ = get_db(EVAL)
    mode_ = {'IAB_CATEGORY_CODE': IAB_CATEGORY_CODE}
    print type(mode_)
    rename_attrs(PRODUCTS, mode_, db_)
