from FlaskWebProject import app
from FlaskWebProject.data.data_consts import ID, DEBUG
from shared_consts import MONGO_DB, DB_ID
from pymongo import MongoClient
from bson.objectid import ObjectId


_mongo_id = '_id'


def get_db(mode):
    return MongoClient(app.config[MONGO_DB])[app.config[DB_ID]]
    #return MongoClient(app.config[MONGO_DB])['{0}_{1}'.format(app.config[DB_ID], mode)]


def create(collection_id, docs, mode=DEBUG):
    # Machine Learning may call this function directly and pass a dictionary, so make sure that it's wrapped in a list
    if type(docs) is dict:
        docs = [docs]
    try:
        db = get_db(mode)
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
        doc[ID] = str(doc[_mongo_id])
        del doc[_mongo_id]
        docs.append(doc)
    return docs


def read(collection_id, query_dicts=None, mode=DEBUG):
    # Machine Learning may call this function directly and pass a dictionary, so make sure that it's wrapped in a list
    if type(query_dicts) is dict:
        query_dicts = [query_dicts]
    try:
        db = get_db(mode)
        if query_dicts is None:
            cursor = db[collection_id].find()
            return extract_docs(cursor)
        else:
            docs = []
            for query_dict in query_dicts:
                if _mongo_id in query_dict.keys():
                    query_dict[_mongo_id] = ObjectId(query_dict[_mongo_id])
                cursor = db[collection_id].find(query_dict)
                docs.extend(extract_docs(cursor))
            return docs
    except Exception as e:
        print type(e)
        print e
        raise e


def update(collection_id, updated_docs, mode=DEBUG):
    # Machine Learning may call this function directly and pass a dictionary, so make sure that it's wrapped in a list
    if type(updated_docs) is dict:
        updated_docs = [updated_docs]
    db = get_db(mode)
    updated_ids = []
    for updated_doc in updated_docs:
        try:
            id_ = updated_doc[ID]
            del updated_doc[ID]
            updated_doc = {'$set': updated_doc}
            result = db[collection_id].update_one({_mongo_id: ObjectId(id_)}, updated_doc)
            print type(result)
            print result
            updated_ids.append(id_)
        except Exception as e:
            print type(e)
            print e
            raise e
    return updated_ids


def delete(collection_id, ids, mode=DEBUG):
    # Machine Learning may call this function directly and pass a string, so make sure that it's wrapped in a list
    if type(ids) is str:
        ids = [ids]
    db = get_db(mode)
    for id_ in ids:
        try:
            results = db[collection_id].delete_one({_mongo_id: ObjectId(id_)})
            print type(results)
            print results
        except Exception as e:
            print type(e)
            print e
            raise e
    return ids
