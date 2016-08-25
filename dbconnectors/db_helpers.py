from FlaskWebProject import app
from FlaskWebProject.steershared.shared_consts import ID, DB_ACCESS_MODULE
import importlib


def import_db_access_module():
    return importlib.import_module(app.config[DB_ACCESS_MODULE])


def add_ids(docs, ids):
    zipped = zip(docs, ids)
    for doc, id_ in zipped:
        doc[ID] = id_


def rename_attrs(collection_id, attrs):
    db = import_db_access_module()
    docs = db.read(collection_id)
    for doc in docs:
        for old_attr, new_attr in attrs.iteritems():
            doc[new_attr] = doc[old_attr]
            del doc[old_attr]
    db.replace(collection_id, docs)


"""
if __name__ == '__main__':
    db = import_db_access_module()
    coll = 'foo'
    db.delete(coll)
    docs = [{'hello': 0, 'world': 1, 'foo': 5}, {'hello': 2, 'world': 3, 'foo': 6}]
    ids = db.create(coll, docs)
    print 'PRE ADD'
    print docs
    add_ids(docs, ids)
    print 'PRE RENAME'
    print docs
    rename_attrs(coll, {'hello': 'olleh', 'world': 'drlow'})
    docs = db.read(coll)
    print 'POST RENAME'
    print docs
    db.delete(coll)
"""
