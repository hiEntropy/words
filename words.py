import sys
from Utilities import dictionary_to_sorted_list, pretty_print_dictionary
from topology import parse_topologies, words_by_topology


def main(argsv):
    len_argsv = len(argsv)
    if len_argsv == 2:
        if argsv[1] == "-h":
            print_options()
    elif len_argsv == 4:
        if argsv[2] == '-w':
            results = words_by_topology(argsv[3],argsv[1])
            sorted_results = dictionary_to_sorted_list(results)
            pretty_print_dictionary(sorted_results)
    elif  argsv[2] == '-t':
        run_parse_topologies(argsv)
    else:
        print_options()


def run_parse_topologies(argsv):
    if type(argsv) is not list:
        exit()
    min_len = 0
    max_len = 99
    local = False
    url = argsv[2]
    for x in range(1, len(argsv)):
        cur = argsv[x]
        if cur == '-min':
            min_len = int(argsv[x+1])
        elif cur == '-max':
            max_len = int(argsv[x+1])
        elif cur == '-l':
            local = True
    parse_topologies(url, min_len, max_len, local)
 

def print_options():
    print("commands:")
    print("words.py file -t ([-min][int]) ([-max][int])")
    print("words.py file -w topology ")
    sys.exit()


main(sys.argv)
