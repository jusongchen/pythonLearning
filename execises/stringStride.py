
from __future__ import print_function

def slice_str(s, stride):
    if stride < 1:
        print ('invalid stride {}'.format(stride))

    print ('stride:{}'.format(stride))
    res = []
    # l = 0
    # while l < len(s):
    #     res.append( s[l:l+stride])
    #     l += stride
    # return res
    for i in range(0,len(s),stride):
        res.append(s[l:l+stride])

if __name__ == '__main__':
    instr = raw_input('your string?')
    strideStr = raw_input('slide(number only)?')

    try:
        stride = int(strideStr)
    except:
        print ('slide {} you give is not a number.'.format(strideStr))

    slices = slice_str(instr, stride)
    print (slices)

    res = ""
    make_upper = False
    for  s in slices:
        if make_upper:
            res += s.upper()
        else:
            res += s
        make_upper = not make_upper

    print (res)



            


    
    

