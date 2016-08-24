from FlaskWebProject import app
from FlaskWebProject.steershared.shared_consts import ID, DEBUG, MONGO_DB, DB_ID
from pymongo import MongoClient
from bson.objectid import ObjectId
from copy import deepcopy


_mongo_id_key = '_id'


def get_mongo_id(id_):
    return ObjectId(id_)


def get_db():
    return MongoClient(app.config[MONGO_DB])[app.config[DB_ID]]


def create(collection_id, docs):
    # Machine Learning may call this function directly and pass a dictionary, so make sure that it's wrapped in a list
    if type(docs) is dict:
        docs = [docs]
    try:
        db = get_db()
        results = db[collection_id].insert_many(docs)
        ids = [str(inserted_id) for inserted_id in results.inserted_ids]
        print ids
        return ids
    except Exception as e:
        print type(e)
        print e
        raise e


def extract_docs(cursor):
    docs = []
    for doc in cursor:
        doc[ID] = str(doc[_mongo_id_key])
        del doc[_mongo_id_key]
        docs.append(doc)
    return docs


def read(collection_id, query_dicts=None):
    # Machine Learning may call this function directly and pass a dictionary, so make sure that it's wrapped in a list
    if type(query_dicts) is dict:
        query_dicts = [query_dicts]
    try:
        db = get_db()
        if query_dicts is None:
            cursor = db[collection_id].find()
            return extract_docs(cursor)
        else:
            docs = []
            for query_dict in query_dicts:
                if ID in query_dict.keys():
                    query_dict[_mongo_id_key] = ObjectId(query_dict[ID])
                    del query_dict[ID]
                cursor = db[collection_id].find(query_dict)
                docs.extend(extract_docs(cursor))
            return docs
    except Exception as e:
        print type(e)
        print e
        raise e


def update(collection_id, updated_docs):
    # Machine Learning may call this function directly and pass a dictionary, so make sure that it's wrapped in a list
    if type(updated_docs) is dict:
        updated_docs = [updated_docs]

    updated_docs = deepcopy(updated_docs)

    db = get_db()
    updated_ids = []
    for updated_doc in updated_docs:
        try:
            id_ = updated_doc[ID]
            updated_doc = {'$set': updated_doc}
            result = db[collection_id].update_one({_mongo_id_key: ObjectId(id_)}, updated_doc)
            updated_ids.append(id_)
        except Exception as e:
            print type(e)
            print e
            raise e
    return updated_ids


def replace(collection_id, replace_docs):
    # Machine Learning may call this function directly and pass a dictionary, so make sure that it's wrapped in a list
    if type(replace_docs) is dict:
        replace_docs = [replace_docs]

    replace_docs = deepcopy(replace_docs)

    db = get_db()
    replace_ids = []
    for replace_doc in replace_docs:
        try:
            id_ = replace_doc[ID]
            replace_doc = {'$set': replace_doc}
            result = db[collection_id].replace_one({_mongo_id_key: ObjectId(id_)}, replace_doc)
            replace_ids.append(id_)
        except Exception as e:
            print type(e)
            print e
            raise e
    return replace_ids


def delete(collection_id, ids):
    # Machine Learning may call this function directly and pass a string, so make sure that it's wrapped in a list
    if type(ids) is str:
        ids = [ids]
    db = get_db()
    for id_ in ids:
        try:
            results = db[collection_id].delete_one({_mongo_id_key: ObjectId(id_)})
            print type(results)
            print results
        except Exception as e:
            print type(e)
            print e
            raise e
    return ids
