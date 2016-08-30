from FlaskWebProject import app
from FlaskWebProject.steershared.shared_consts import ID, DEFAULT_MODE, MONGO_DB, DB_ID
from pymongo import MongoClient
from bson.objectid import ObjectId
from copy import deepcopy
from functools import wraps


_mongo_id_key = '_id'


def _get_mongo_id(id_):
    return ObjectId(id_)


def _extract_docs(cursor):
    docs = []
    for doc in cursor:
        doc[ID] = str(doc[_mongo_id_key])
        del doc[_mongo_id_key]
        docs.append(doc)
    return docs


def gen_connector(mode):
    return MongoConnector(mode)


def deco_retry(f):
    @wraps(f)
    def f_retry(self, *args, **kwargs):
        mtries = 2
        while mtries > 1:
            try:
                return f(self, *args, **kwargs)
            except Exception as e:
                # Reinstantiate db client
                self.gen_db()
                print type(e)
                print e
            print 'Retrying mongodbconnector'
            mtries -= 1
        return f(self, *args, **kwargs)

    return f_retry  # true decorator


class MongoConnector:
    def __init__(self, mode):
        self._mode = mode
        self._db = None
        self.gen_db()

    def gen_db(self):
        self._db = MongoClient(app.config[MONGO_DB])['{0}_{1}'.format(app.config[DB_ID], self._mode)]

    @deco_retry
    def create(self, collection_id, docs):
        # Machine Learning may call this function directly and pass a dictionary, so make sure that it's wrapped in a
        # list
        if type(docs) is dict:
            docs = [docs]
        try:
            results = self._db[collection_id].insert_many(docs)
            ids = [str(inserted_id) for inserted_id in results.inserted_ids]
            for doc in docs:
                del doc[_mongo_id_key]
            return ids
        except Exception as e:
            print type(e)
            print e
            raise e

    @deco_retry
    def read(self, collection_id, query_dicts=None):
        # Machine Learning may call this function directly and pass a dictionary, so make sure that it's wrapped in a list
        if type(query_dicts) is dict:
            query_dicts = [query_dicts]
        try:
            if query_dicts is None:
                cursor = self._db[collection_id].find()
                return _extract_docs(cursor)
            else:
                docs = []
                for query_dict in query_dicts:
                    if ID in query_dict.keys():
                        query_dict[_mongo_id_key] = ObjectId(query_dict[ID])
                        del query_dict[ID]
                    cursor = self._db[collection_id].find(query_dict)
                    docs.extend(_extract_docs(cursor))
                return docs
        except Exception as e:
            print type(e)
            print e
            raise e

    @deco_retry
    def update(self, collection_id, updated_docs):
        # Machine Learning may call this function directly and pass a dictionary, so make sure that it's wrapped in a list
        if type(updated_docs) is dict:
            updated_docs = [updated_docs]

        updated_docs = deepcopy(updated_docs)

        updated_ids = []
        for updated_doc in updated_docs:
            try:
                id_ = updated_doc[ID]
                updated_doc = {'$set': updated_doc}
                result = self._db[collection_id].update_one({_mongo_id_key: ObjectId(id_)}, updated_doc)
                updated_ids.append(id_)
            except Exception as e:
                print type(e)
                print e
                raise e
        return updated_ids

    @deco_retry
    def replace(self, collection_id, replace_docs):
        # Machine Learning may call this function directly and pass a dictionary, so make sure that it's wrapped in a list
        if type(replace_docs) is dict:
            replace_docs = [replace_docs]

        replace_docs = deepcopy(replace_docs)

        replace_ids = []
        for replace_doc in replace_docs:
            try:
                id_ = replace_doc[ID]
                result = self._db[collection_id].replace_one({_mongo_id_key: ObjectId(id_)}, replace_doc)
                replace_ids.append(id_)
            except Exception as e:
                print type(e)
                print e
                raise e
        return replace_ids

    @deco_retry
    def delete(self, collection_id, ids=None):
        # Machine Learning may call this function directly and pass a string, so make sure that it's wrapped in a list
        if not ids:
            self._db[collection_id].delete_many({})
            return []
        else:
            if type(ids) is str:
                ids = [ids]
            for id_ in ids:
                try:
                    self._db[collection_id].delete_one({_mongo_id_key: ObjectId(id_)})
                except Exception as e:
                    print type(e)
                    print e
                    raise e
            return ids


"""
# This is for backwards compatibility from before connectors were objects
_default_connector = MongoConnector(app.config[DEFAULT_MODE])


def create(collection_id, docs):
    return _default_connector.create(collection_id, docs)


def read(collection_id, docs):
    return _default_connector.read(collection_id, docs)


def update(collection_id, docs):
    return _default_connector.update(collection_id, docs)


def replace(collection_id, docs):
    return _default_connector.replace(collection_id, docs)


def delete(collection_id, docs):
    return _default_connector.delete(collection_id, docs)
"""
