from unittest import TestCase
from topology import get_topology


class TestTopology(TestCase):
    word_File = open("test_words.txt", 'r').read()

    def test_get_topology(self):
        password = "?l?l?l?l?l?l?l?l"
        specials = "?s?s?s?s?s"
        mix = "?U?S?l?l?l?l?n?n"
        self.assertEquals(password, get_topology("password"))
        self.assertEquals(specials, get_topology(".^!@%"))
        self.assertEquals("", get_topology("P@sswo63"))
        self.assertEquals("", None)

    def test_parse_topologies(self):
        self.fail()

    def test_words_by_topology(self):
        self.fail()
