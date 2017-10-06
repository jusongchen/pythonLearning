# Lab: File I/O + dicts
# write a Python program to read a file and count the number of occurrences of each word in the file
# use a dict, indexed by word, to count the occurrences
# remember d.get(key) will return None if there is no such key in the dict (vs. d[key] which will throw an exception) and also the in operator
# treat The and the as the same word when counting
# print out words and counts, from most common to least common
# EXTRA: remove punctuation, so Hamlet, == Hamlet
# Road Not Taken and Hamlet are available at https://github.com/davewadestein/Python-Core

import sys


def count_word_in_file(in_file):
    word_cnt = {}
    for line in in_file:
        # split line to words
        for word in line.split():
            import string
            lowcase = word.translate(None, string.punctuation).lower()
            word_cnt[lowcase] = word_cnt.get(lowcase, 0) + 1

    return word_cnt


def main():
    if len(sys.argv) != 2:
        print 'usage: ' + sys.argv[0] + ' input_file'
        sys.exit(1)

    in_file_name = sys.argv[1]

    try:
        in_file = open(in_file_name, 'rt')
        word_cnt = count_word_in_file(in_file)
    except IOError as e:
        print("open " + in_file_name + ":" + e.message)
        sys.exit(1)
    finally:
        in_file.close()

    for k in sorted(word_cnt, key=word_cnt.get, reverse=True):
        print(k, word_cnt[k])

    sys.exit(0)


if __name__ == '__main__':
    main()
