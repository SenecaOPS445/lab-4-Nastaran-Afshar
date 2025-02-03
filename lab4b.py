#!/usr/bin/env python3

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

def join_lists(list1, list2):
    return list(set(list1) | set(list2))

def match_lists(list1, list2):
    return list(set(list1) & set(list2))

def diff_lists(list1, list2):
    return list(set(list1) ^ set(list2))

if __name__ == '__main__':
    list1 = list(range(1,10))
    list2 = list(range(5,15))
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', list(join_lists(list1, list2)))
    print('match: ', list(match_lists(list1, list2)))
    print('diff: ', list(diff_lists(list1, list2)))