import unittest
from topology import get_topology


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


if __name__ == '__main__':
    unittest.main()
