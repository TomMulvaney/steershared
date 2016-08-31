from FlaskWebProject import app
from FlaskWebProject.steershared.shared_consts import ID, DB_ACCESS_MODULE, MODE_HEADER_KEY, DEFAULT_MODE, \
    DB_HEADER_KEY, DB_PACKAGE_PATH
import importlib


def rename_attrs(collection_id, attrs, db=None):
    if not db:
        db = get_db()
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
        mode = headers[MODE_HEADER_KEY]
    except (KeyError, TypeError):
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
    mod = importlib.import_module('mongodb_connector')
    print type(mod)
    print mod
