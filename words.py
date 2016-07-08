import sys
from Utilities import dictionary_to_sorted_list, pretty_print_dictionary
from topology import parse_topologies


def main(argsv):
    len_argsv = len(argsv)
    if len_argsv == 2:
        if argsv[1] == "-h":
            print_options()
    elif len_argsv == 3:
        if argsv[2] == '-t':
            results = parse_topologies(argsv[1])
            sorted_results = dictionary_to_sorted_list(results)
            pretty_print_dictionary(sorted_results)

    elif len_argsv == 5:
        if argsv[2] == '-t' and argsv[3] == 'min':
            results = parse_topologies(argsv[1],min_len=int(argsv[4]))
            sorted_results = dictionary_to_sorted_list(results)
            pretty_print_dictionary(sorted_results)
        elif argsv[2] == '-t' and argsv[3] == 'max':
            results = parse_topologies(argsv[1], max_len=int(argsv[4]))
            sorted_results = dictionary_to_sorted_list(results)
            pretty_print_dictionary(sorted_results)
    elif len_argsv == 7:
        if argsv[2] == '-t' and argsv[3] == 'min' and argsv[5] == 'max':
            results = parse_topologies(argsv[1], min_len=int(argsv[4]), max_len=int(argsv[6]))
            sorted_results = dictionary_to_sorted_list(results)
            pretty_print_dictionary(sorted_results)
    else:
        print_options()


def print_options():
    print("commands:")
    print("'words.py file -t ([-min][int]) ([-max][int])")
    sys.exit()


main(sys.argv)
