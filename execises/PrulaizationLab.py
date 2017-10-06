# -*- coding: utf-8 -*-
#
#  Lab: Pluralization
# write a program (or function) which takes a word as a command line argument and
# outputs the plural of that word
# your program should follow these rules:
# if the word ends in 's', 'x', or 'z', the plural adds 'es',
# e.g., ax => axes, loss => losses
# if the word ends in an 'h', which is not preceded by a vowel or 'd', 'g',
# 'k', 'p', 'r', or 't', the plural adds 'es',
#   e.g., moth => moths,but match = > matches
# if the word ends in a 'y' which is not preceded by a vowel, then the plural
# strips the 'y' and adds 'ies', e.g., baby => babies, but boy => boys
# otherwise just add 's'


import re


def pluralize(word):
    '''
    Pluralizate takes a word as a command line argument and outputs the plural of that word
    by following these rules:
        if the word ends in 's', 'x', or 'z', the plural adds 'es', e.g., ax => axes, loss => losses
        if the word ends in an 'h', which is not preceded by a vowel or 'd', 'g', 'k', 'p', 'r', or 't', the plural adds 'es', e.g., moth => moths, but match => matches
        if the word ends in a 'y' which is not preceded by a vowel, then the plural strips the 'y' and adds 'ies', e.g., baby => babies, but boy => boys
        otherwise just add 's'
    '''
    if len(word) == 0:
        return word
    match = re.search(r'.*[sxz]$', word)
    if match:
        return match.group(0) + 'es'

    match = re.search(r'.*[^aeioudgkprt]h$', word)
    if match:
        return match.group(0) + 'es'

    match = re.search(r'.*[^aeiou]y$', word)
    if match:
        return match.group(0)[:-1] + 'ies'
    return word + 's'


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(origin, got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s,\torigin: %s \tgot: %s \texpected: %s' % (prefix, origin, repr(got), repr(expected))


# Calls the above functions with interesting inputs.
def main():

    print
    print 'Test pluralize'
    testcases = {
        '': '',
        'computer': 'computers',
        # if the word ends in 's', 'x', or 'z', the plural adds 'es', e.g., ax => axes, loss => losses
        'box': 'boxes',
        'bus': 'buses',
        'buzz': 'buzzes',
        # if the word ends in an 'h',
        # which is not preceded by a vowel or 'd', 'g', 'k', 'p', 'r', or 't',
        # the plural adds 'es',
        # e.g., moth => moths, but match => matches
        'oah': 'oahs',
        'moth': 'moths',
        'jargh': 'jarghs',
        'match': 'matches',
        'mash': 'mashes',
        # if the word ends in a 'y' which is not preceded by a vowel, then the plural strips the 'y' and adds 'ies', e.g., baby => babies, but boy => boys
        'boy': 'boys',
        'dummy': 'dummies'
    }

    for tc in testcases:
        test(tc, pluralize(tc), testcases[tc])


if __name__ == '__main__':
    main()
