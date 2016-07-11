# -*- coding: utf-8 -*-

from collections import Counter

## NOTES FOR SEARCH FUNCTIONS IN PROGRESS
## see below for link on collections
## -  http://pyparsing.wikispaces.com/file/view/searchparser.py
## -  http://kitchingroup.cheme.cmu.edu/blog/2014/03/31/Using-pyparsing-for-search-queries-with-tags/

## -  http://stackoverflow.com/questions/2917372/how-to-search-a-list-of-tuples-in-python
## -  http://stackoverflow.com/questions/9542738/python-find-in-list
## -  http://stackoverflow.com/questions/7571635/fastest-way-to-check-if-a-value-exist-in-a-list
## -  http://stackoverflow.com/questions/11963711/what-is-the-most-efficient-way-to-search-nested-lists-in-python
## -  http://stackoverflow.com/questions/18944101/find-matching-values-in-a-list-of-lists-using-python
## -  http://stackoverflow.com/questions/1156087/python-search-in-lists-of-lists
## -  https://home.regit.org/2014/11/python-search-string-in-a-set-of-strings/

## -  http://www.tutorialspoint.com/python/list_index.htm
## -  https://docs.python.org/2/library/bisect.html

def list_contains(list_, string_):
    test = (string_ in list_)
    return test
    
def list_of_lists_contains(list_, string_):
    ## http://stackoverflow.com/questions/11963711/what-is-the-most-efficient-way-to-search-nested-lists-in-python
    test = any(string_ in x for x in list_)
    return test


## Collections -- tons of great ideas for indexing and searching
## https://docs.python.org/2.7/library/collections.html#collections

def list_counter(list_):
    """Count occurances in list"""
    ## https://docs.python.org/2.7/library/collections.html#collections.Counter
    cnt = Counter(list_)
    # cnt = Counter()
    # for item in list_:
    #     cnt[item] += 1
    return cnt

def list_of_lists_counter(list_):
    ## http://stackoverflow.com/questions/5828123/nested-list-and-count
    def flatten(seq,container=None):
        if container is None:
            container = []
        for s in seq:
            if hasattr(s,'__iter__'):
                flatten(s,container)
            else:
                container.append(s)
        return container
    cnt = Counter(flatten(list_))
    return cnt
    ## https://bytes.com/topic/python/answers/36420-counter-items-lists-lists



