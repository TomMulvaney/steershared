from FlaskWebProject import app
from FlaskWebProject.data.data_consts import ID, DEBUG
from shared_consts import DB_ID, DOCUMENTDB_HOST, DOCUMENTDB_MASTER_KEY
import pydocumentdb.errors as errors
import pydocumentdb.document_client as document_client


class IDisposable:
    """ A context manager to automatically close an object with a close method
    in a with statement. """

    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj  # bound to target

    def __exit__(self, exception_type, exception_val, trace):
        # extra cleanup in here
        self = None


def get_client():
    return document_client.DocumentClient(app.config[DOCUMENTDB_HOST], {'masterKey': app.config[DOCUMENTDB_MASTER_KEY]})


def get_db_link(mode):
    return 'dbs/{0}_{1}'.format(app.config[DB_ID], mode)


def get_collection_link(id_, mode):
    return get_db_link(mode) + '/colls/{0}'.format(id_)


def get_document_link(collection_id, id_, mode):
    return get_collection_link(collection_id, mode) + '/docs/{0}'.format(id_)


# This is more encapsulated but the introspection feels a bit hacky (see create_doc and create_docs below)
def create(collection_id, docs, mode=DEBUG):
    with IDisposable(get_client()) as client:
        created_ids = []
        if type(docs) is dict:
            docs = [docs]
        for doc in docs:
            new_doc = client.CreateDocument(get_collection_link(collection_id, mode), doc)
            created_ids.append(new_doc[ID])
        return created_ids


def read(collection_id, query_dicts, mode=DEBUG):
    with IDisposable(get_client()) as client:
        docs = []
        if query_dicts is None:
            docs = client.ReadDocuments(get_collection_link(collection_id, mode)).fetch_items()
        else:
            for query_dict in query_dicts:
                try:
                    # TODO: Optimize! If the only query involves an id then use ReadDocument instead
                    doc = client.QueryDocument(get_collection_link(collection_id, mode), query_dict)
                    docs.append(doc)
                except errors.DocumentDBError as e:
                    if e.status_code == 404:
                        print('A {0} with id \'{1}\' does not exist'.format(collection_id, query_dict))
                    else:
                        raise errors.HTTPFailure(e.status_code)
    return docs


def update(collection_id, new_docs, mode=DEBUG):
    with IDisposable(get_client()) as client:
        if type(new_docs) is dict:
            new_docs = [new_docs]
        updated_ids = []
        for new_doc in new_docs:
            try:
                existing_doc = client.ReadDocument(get_document_link(collection_id, new_doc[ID], mode))
                existing_doc.update(new_doc)
                client.ReplaceDocument(get_document_link(collection_id, existing_doc[ID], mode), existing_doc)
                updated_ids.append(existing_doc[ID])
            except errors.DocumentDBError as e:
                if e.status_code == 404:
                    print('A {0} with id \'{1}\' does not exist'.format(collection_id, new_doc[ID]))
                else:
                    raise errors.HTTPFailure(e.status_code)
        return updated_ids


def delete(collection_id, ids, mode=DEBUG):
    with IDisposable(get_client()) as client:
        deleted_ids = []
        for id_ in ids:
            try:
                client.DeleteDocument(get_document_link(collection_id, id_, mode))
                deleted_ids.append(id_)
            except errors.DocumentDBError as e:
                if e.status_code == 404:
                    print('A {0} with id \'{1}\' does not exist'.format(collection_id, id_))
                else:
                    raise errors.HTTPFailure(e.status_code)
    return deleted_ids
