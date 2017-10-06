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


def reverse_lines(in_file, out_file):
    lines = in_file.readlines()
    # check the last charactor of the last line
    if lines[-1][-1] != '\n':
        lines[-1] = lines[-1] + '\n'

    out_file.writelines(sorted(lines, reverse=True))
    return


def main():
    if len(sys.argv) != 3:
        print 'usage: ' + sys.argv[0] + ' input_file output_file'
        sys.exit(1)

    in_file_name = sys.argv[1]
    try:
        in_file = open(in_file_name, 'rt')
    except IOError as e:
        print("open " + in_file_name + ":" + e.message)

        sys.exit(1)

    out_file_name = sys.argv[2]
    try:
        out_file = open(out_file_name, 'wt')
    except IOError as e:
        print("open " + out_file_name + ":" + e.message)
        sys.exit(1)
    try:
        reverse_lines(in_file, out_file)
    finally:
        in_file.close()
        out_file.close()

    sys.exit(0)


if __name__ == '__main__':
    main()
