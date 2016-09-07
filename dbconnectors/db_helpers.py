from FlaskWebProject import app
from FlaskWebProject.steershared.shared_consts import *
import importlib


def rename_attrs(collection_id, attrs, mode):
    db = get_db(mode)
    docs = db.read(collection_id)
    for doc in docs:
        for old_attr, new_attr in attrs.iteritems():
            doc[new_attr] = doc[old_attr]
            del doc[old_attr]
    db.replace(collection_id, docs)


def add_attrs(collection_id, attrs, mode):
    db = get_db(mode)
    docs = db.read(collection_id)
    for doc in docs:
        for attr, val in attrs.iteritems():
            if attr not in doc.keys():
                doc[attr] = val
    print docs
    db.update(collection_id, docs)


def relink_ids(referencer_coll, link_attr, id_attr, referencee_coll, referencee_attr, mode):
    db = get_db(mode)
    referencers = db.read(referencer_coll, {RETAILER_NAME: 'The Veg Box Cafe'})
    for referencer in referencers:
        try:
            referencees = db.read(referencee_coll, {referencee_attr: referencer[link_attr]})
            for referencee in referencees:
                referencer[id_attr] = referencee[ID]
        except KeyError:
            pass
    print referencers
    db.update(referencer_coll, referencers)


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
    relink_ids(PRODUCTS, RETAILER_NAME, RETAILER_ID, RETAILERS, NAME, DEBUG)
