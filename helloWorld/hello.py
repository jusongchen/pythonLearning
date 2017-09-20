import sys

if len(sys.argv) ==1:
    print 'expect at least one argument'
    sys.exit(1)

print 'hello '+' '.join(sys.argv[1:])
  