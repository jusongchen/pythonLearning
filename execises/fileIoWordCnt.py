# ## Lab: File I/O
# * write a Python program which prompts the user for a filename, then opens that file and writes the contents of the file to a new file, in reverse order, i.e.,

# <pre><b>
#     Original file       Reversed file
#     Line 1              Line 4
#     Line 2              Line 3
#     Line 3              Line 2
#     Line 4              Line 1
# </b></pre>

import sys


def count_word_in_file(in_file):
    wordMap = {}
    for line in in_file:
        # split line to words
        for w in line.split():
            import string
            lowcase = w.translate(None, string.punctuation).lower()
            wordMap[lowcase] = wordMap.get(lowcase, 0) + 1

    return wordMap


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
