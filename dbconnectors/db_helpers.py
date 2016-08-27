from FlaskWebProject import app
from FlaskWebProject.steershared.shared_consts import ID, DB_ACCESS_MODULE, MODE_HEADER_KEY, DEFAULT_MODE
import importlib
import re


def str_to_float(mode, collection_id, attr):
    db = get_db(mode)
    docs = db.read(collection_id)

    print docs

    for doc in docs:
        doc[attr] = doc[attr].replace(u'£', u'').replace('n/a', '-1').replace(',', '').replace('From ', ''). \
            replace('From: ', '').replace(' / 15 sachets', '').replace('from just ', '').replace('from ', '')
        doc[attr] = doc[attr].strip()

        if not doc[attr]:
            doc[attr] = '-1'

        full_hyphen_pattern = '[0-9]+-[0-9]+'
        half_hyphen_pattern = '[0-9]+-'
        print doc[attr]
        if re.match(full_hyphen_pattern, doc[attr]):
            try:
                half_match = re.match(half_hyphen_pattern, doc[attr])
                doc[attr] = re.sub(full_hyphen_pattern, half_match.group(0), doc[attr]).replace('-', '')
            except Exception as e:
                print e
                print doc[attr]
                raise e
        try:
            doc[attr] = float(doc[attr])
        except Exception as e:
            print e
            print doc
            print doc[attr]
            raise e

    print docs

    db.update(collection_id, docs)


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
    return _dbs[mode]


def add_ids(docs, ids):
    zipped = zip(docs, ids)
    for doc, id_ in zipped:
        doc[ID] = id_


# Private variables
_db_module = import_db_connector_module()
_dbs = {}
