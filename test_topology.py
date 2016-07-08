import unittest
from topology import get_topology, words_by_topology, parse_topologies


class TopologyTests(unittest.TestCase):
    def test_get_topology1(self):
        specials = "?s?s?s?s?s"
        self.assertEquals(specials, get_topology(".^!@%"))

    def test_get_topology2(self):
        password = "?l?l?l?l?l?l?l?l"
        self.assertEquals(password, get_topology("password"))

    def test_get_topology3(self):
        mix = "?u?s?l?l?l?l?n?n"
        self.assertEquals(mix, get_topology("P@sswo63"))

    def test_get_topology4(self):
        self.assertEquals("", get_topology(None))

    def test_words_by_topology(self):
        results = words_by_topology("?l?l?l?l?l?l?l?l","test_file")
        self.assertEquals(results["password"],6)
        self.assertFalse('test' in results.keys())
        self.assertEquals(results['finessed'],4)

    def test_parse_topologies_defaults(self):
        results = parse_topologies('test_file')
        self.assertEquals(results["?l?l?l?l?l?l?l?l"],11)
        self.assertEquals(results["?l?l?l?l?l?l?l?l?l?l?l?n?n?n?n?n"], 1)
        self.assertEquals(results["?n?n?n?n?n?n?n?n"], 1)
        self.assertEquals(results["?l?l?n?n?l?l?l?l?l?n"], 1)
        self.assertFalse("?l?l?l?l?l?l?l?l?s" in results.keys())

    def test_parse_topologies_with_min(self):
        results = parse_topologies('test_file',min_len=10)
        self.assertFalse("?l?l?l?l?l?l?l?l" in results.keys())
        self.assertEquals(results["?l?l?l?l?l?l?l?l?l?l?l?n?n?n?n?n"], 1)
        self.assertFalse("?n?n?n?n?n?n?n?n" in results.keys())
        self.assertEquals(results["?l?l?n?n?l?l?l?l?l?n"], 1)
        self.assertFalse("?l?l?l?l?l?l?l?l?s" in results.keys())

    def test_parse_topologies_with_max(self):
        results = parse_topologies('test_file',max_len=10)
        self.assertEquals(results["?l?l?l?l?l?l?l?l"],11)
        self.assertFalse("?l?l?l?l?l?l?l?l?l?l?l?n?n?n?n?n" in results.keys())
        self.assertEquals(results["?n?n?n?n?n?n?n?n"], 1)
        self.assertEquals(results["?l?l?n?n?l?l?l?l?l?n"], 1)
        self.assertFalse("?l?l?l?l?l?l?l?l?s" in results.keys())


if __name__ == '__main__':
    unittest.main()
