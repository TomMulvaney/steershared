from FlaskWebProject import app
from FlaskWebProject.steershared.shared_consts import ID, DB_ACCESS_MODULE, MODE_HEADER_KEY, DEFAULT_MODE
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


def import_db_connector_module():
    return importlib.import_module(app.config[DB_ACCESS_MODULE])


def get_db(mode):
    try:
        if type(mode) is not str:
            mode = mode[MODE_HEADER_KEY]
    except KeyError:
        mode = app.config[DEFAULT_MODE]
    except TypeError:
        mode = app.config[DEFAULT_MODE]
    if mode not in _dbs.keys():
        _dbs[mode] = _db_module.gen_connector(mode)
    print 'Getting {0} db'.format(mode)
    return _dbs[mode]


def add_ids(docs, ids):
    zipped = zip(docs, ids)
    for doc, id_ in zipped:
        doc[ID] = id_


# Private variables
_db_module = import_db_connector_module()
_dbs = {}
