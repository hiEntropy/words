from Utilities import trim_newline,credentials
import mongodb

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


'''
parse_topologies

url is a string representing the path to a file of '\\n' separated words
min_len is the minimum word length that will be processed default is zero
max_len is the maximum word length that will be precessed default is 99

returns a dictionary of topologies as a strings with a count of how often
the topology appears in the given file. dictionary pairs are (string, int)
'''


def parse_topologies(url, min_len=0, max_len=99,local = True):
    topologies = {}
    creds = None
    mongodb_obj = None
    if not local:
        creds = credentials()
        mongodb_obj = mongodb.mongodb(creds[0],creds[1],'words','topologies')
    fp = open(url, 'r', errors='strict')
    line = fp.readline()
    while line:
        line = trim_newline(line)
        len_line = len(line)
        if min_len <= len_line <= max_len:
            topology = get_topology(line)
            if topology in topologies.keys():
                topologies[topology] += 1
            else:
                topologies[topology] = 1
            if not local and len(topologies) > 10000:
                mongodb_obj.update(topologies)
                topologies.clear()
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
associated with an integer representing the words frequency in the file

:return dictionary of (string,int)
'''


def words_by_topology(topology, url):
    words = {}
    fp = open(url, 'r', errors='strict')
    line = fp.readline()
    letters_in_topology = len(topology) / 2
    while line:
        line = trim_newline(line)
        if len(line) == letters_in_topology:
            result = get_topology(line)
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


def is_topology(topology):
    for x in range(0, len(topology)):
        if (x % 2) == 0:
            if topology[x] != '?':
                return False
        elif topology[x] not in ['s', 'l', 'u', 'n']:
            return False
    return True


