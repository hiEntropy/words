import operator
import sys
from topology import parse_topologies, pretty_print_dictionary

def main(argsv):
    if len(argsv) < 2:
        print("Too few arguments -h for help")
        sys.exit()
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


main(sys.argv)
