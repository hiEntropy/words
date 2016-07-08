import sys
from Utilities import dictionary_to_sorted_list, pretty_print_dictionary
from topology import parse_topologies


def main(argsv):
    if len(argsv) < 2:
        print("Too few arguments -h for help")
        sys.exit()
    if len(argsv) == 2:
        if argsv[1] == "-h":
            print("commands:")
            print("'words.py file -t [-min] [-max]")
            sys.exit()
    if len(argsv) == 3:
        if argsv[2] == '-t':
            results = parse_topologies(argsv[1])
            sorted_results = dictionary_to_sorted_list(results)
            pretty_print_dictionary(sorted_results)


main(sys.argv)
