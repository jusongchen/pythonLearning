
# Lab: argparse
# modify the RE/grep lab to use -f to specify the filename and -p to specify the pattern
# also add -v or --version as an option
# if you have time add a -c ('context') option which will print the preceding and following line for each line that matches

from __future__ import print_function
import argparse
import sys


def grep(f, pattern):
    '''
    grep(f, pattern) reads from file Object f then search regex pattern and print out matches
    '''
    import re
    for line in f:
        if re.search(pattern, line):
            print(line, end='')


def main():
    parser = argparse.ArgumentParser(description='mygrep:a simple prpgram like Unix grep')
    parser.add_argument('-f', dest='filename', help='the input file, mandatory')
    parser.add_argument('-p', dest='pattern', help='the pattern, mandatory')
    parser.add_argument('-v', '--version', action='store_true')
    args = parser.parse_args()

    if args.version:
        print('version 1.0')
        sys.exit(0)

    if not args.pattern or not args.filename:
        parser.print_help()
        sys.exit(1)

    filename = args.filename
    pattern = args.pattern
    try:
        f = open(filename)
    except IOError as e:
        print("open {}:{}".format(filename, e))
        sys.exit(1)
    else:
        grep(f, pattern)
        f.close()


if __name__ == '__main__':
    main()
