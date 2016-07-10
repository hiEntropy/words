import unittest
import mongodb


class MongoTests(unittest.TestCase):
    mongo_creds = open('mongo_creds')
    user_id = mongo_creds.readline().split(':')[1]
    user_id = user_id[0:len(user_id)-1]
    password = mongo_creds.readline().split(':')[1]
    mongodb_obj = mongodb.mongodb(user_id, password,'words','topologies')

    def testUpdate(self):
        topology = '?l?l?l?l'
        test = {topology: 1}
        results = self.mongodb_obj.update(test)
        self.assertTrue(len(results) == 0)
        self.assertTrue(self.mongodb_obj.delete(topology))

if __name__ == '__main__':
    unittest.main()
