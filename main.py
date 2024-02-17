#!/usr/bin/env python3


# Sorts and prints function arguments in character order
def print_sorted_args(*args):
    for_sort = []
    # cast args to string
    for i in args:
        for_sort.append(i.__str__())
    # sort and print args
    sorted_args = sorted(for_sort)
    print(sorted_args)


print_sorted_args("Emil", "Tobias", "Linus", "Alex", 10, 12, 23)
