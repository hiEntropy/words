
'''
getTopology

outputs the topology of any string as defined by PathWell
?u = any uppercase
?l = any lowercase
?s = any special char
?n = any number

returns a string representing the topology of the given string
'''


def get_topology(string):
    topology = ""
    if string is not None:
        for x in string:
            if x.isupper():
                topology += "?u"
            elif x.islower():
                topology += "?l"
            elif x.isnumeric():
                topology += "?n"
            elif x != '\n':
                topology += "?s"
    return topology


@staticmethod
def parse_topologies(self, url, min_len=0, max_len=99):
    topologies = {}
    fp = open(url, 'r', errors='strict')
    line = fp.readline()
    while line:
        len_line = len(line)
        if min_len < len_line < max_len:
            topology = self.get_topology(line)
            if topology in topologies.keys():
                topologies[topology] += 1
            else:
                topologies[topology] = 1
        try:
            line = fp.readline()
        except ValueError:
            continue
    return topologies


'''
words_by_topology

:parameter url as a string
:parameter topology as a string '?n?l?n?n?U' for example
parses through a file looking for words that match the give topology
the resulting dictionary will contain each matching word found as a key
associated with an integer representing the words frequence in the file

:return dictionary of (string,int)
'''


@staticmethod
def words_by_topology(self, topology, url):
    words = {}
    fp = open(url, 'r', errors='strict')
    line = fp.readline()
    letters_in_topology = len(topology) / 2
    while line:
        if len(line) == letters_in_topology:
            result = self.get_topology(line)
            if topology == result:
                if line in words.keys():
                    words[line] += 1
                else:
                    words[line] = 1
        try:
            line = fp.readline()
        except ValueError:
            continue
    return words


def pretty_print_dictionary(self, list_topologies):
    count = 1
    for x in reversed(list_topologies):
        print("{0}. {1}".format(count, str(x)))
        count += 1
