import operator
import sys
<<<<<<< HEAD
from topology import parse_topologies, pretty_print_dictionary
=======

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


def parse_topologies(url,min_len=0,max_len=99):
    topologies = {}
    fp = open(url, 'r', errors='strict')
    line = fp.readline()
    while line:
        len_line = len(line)
        if min_len < len_line and max_line > len_line
            topology = get_topology(line)
            if topology in topologies.keys():
                topologies[topology] += 1
            else:
                topologies[topology] = 1
        try:
            line = fp.readline()
        except ValueError:
            continue
    return topologies


def words_by_topology(topology,url):
    words = {}
    fp = open(url, 'r', errors='strict')
    line = fp.readline()
    while line:
        result = get_topology(line)
        if topology == result:
            if line in words.keys():
                words[line] += 1
            else:
                words[line] = 1
        else:
            try:
                line = fp.readline()
            except ValueError:
                continue
    return words


def pretty_print_dictionary(list_topologies):
    count = 1
    for x in reversed(list_topologies):
        print("{0}. {1}".format(count, str(x)))
        count += 1

>>>>>>> abd56407b9462fd4f1a6267c6d292a57e518f18b

def main(argsv):
    if len(argsv) < 2:
        print("Too few arguments -h for help")
        sys.exit()
<<<<<<< HEAD
    if len(argsv) ==2:
        if argsv[1] == "-h":
            print("commands:")
            print("'words.py file -t [-min] [-max]")
            sys.exit()
    if len(argsv) == 3:
        if argsv[2] == '-t':
            results = parse_topologies(argsv[1])
            sorted_results = sorted(results.items(), key=operator.itemgetter(1))
            pretty_print_dictionary(sorted_results)
=======
    if argsv[1] == "-h":
        print("commands:")
        print("'words.py file -t' will print the topologies of all words\n" +
              "in a supplied file. Words must be newline delineated")
        sys.exit()
    if argsv[2] == '-t':
        results = parse_topologies(argsv[1])
        sorted_results = sorted(results.items(), key=operator.itemgetter(1))
        pretty_print_dictionary(sorted_results)
>>>>>>> abd56407b9462fd4f1a6267c6d292a57e518f18b


main(sys.argv)
