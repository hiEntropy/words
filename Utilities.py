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


def credentials():
    mongo_creds = open('mongo_creds')
    user_id = mongo_creds.readline().split(':')[1]
    user_id = user_id[0:len(user_id) - 1]
    password = mongo_creds.readline().split(':')[1]
    return tuple(user_id, password)
