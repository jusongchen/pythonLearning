import sys


def Greeting(name):
    """Say Hi to some one"""   
    print 'hello '+' '.join(sys.argv[1:])
    print '__name__=='+str(__name__)
    print '__module__=='+str(__package__)
    print '__file__=='+str(__file__)
    # print '__path__ == ' +str(__path__)


if __name__=='__main__':
if len(sys.argv) ==1:
    print 'expect at least one argument'
    sys.exit(1)
else:
    Greeting(sys.argv)


    
