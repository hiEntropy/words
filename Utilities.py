import operator


def dictionary_to_sorted_list(dictionary):
    sorted(dictionary.items(), key=operator.itemgetter(1))


def pretty_print_dictionary(list_topologies):
    count = 1
    for x in reversed(list_topologies):
        print("{0}. {1}".format(count, str(x)))
        count += 1


def trim_newline(line):
    len_line = len(line)
    if line[len_line - 1] == '\n':
        return line[:len_line - 1]
    else:
        return line
