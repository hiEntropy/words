import pymongo
from topology import is_topology


class mongodb:
    collection = None

    def __init__(self, user_id, password, database, collection):
        # mongodb://<dbuser>:<dbpassword>@ds017205.mlab.com:17205/words
        mongodb_uri = "mongodb://" + user_id + ":" + password + "@ds017205.mlab.com:17205/" + database
        client = pymongo.MongoClient(mongodb_uri)
        db = client[database]
        self.collection = db[collection]

    '''
    update

    :param topologies a dictionary of the form ('string',int) representing a topology
    and its occurrences

    This method will always add to the database. the schema is enforced via this method.
    the schema is {'topology':'topology string','count':count_int}

    :return a list of all topologies that failed. failure is if no documents where affected
    '''

    def update(self, topologies):
        count = 0
        bad = []
        if self.collection is not None and type(topologies) is dict:
            for x in topologies.keys():
                if not is_topology(x):
                    continue
                count = topologies[x]
                result = self.collection.update(
                    {'topology': str(x)},
                    {'$inc': {'count': count}},
                    upsert=True
                )
                if result is None or 'writeError' in result.keys():
                    bad.append(str(x))
            return bad
        else:
            return False

    def delete(self, topology):
        if self.collection is not None:
            query = {'topology': topology}
            self.collection.remove(query)
            return True
        else:
            return False
