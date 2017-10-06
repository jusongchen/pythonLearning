
def findFactors(num):
    import math
    upto = math.sqrt(num)

    for n in range(2,int(upto)+1):
        q,mod = divmod(num,n)
        if n != num and mod== 0:
            return (False,n,q)
    return (True,num,1)


def processNumbers(fromNum, toNum):
    if fromNum <=0 or toNum <=0 or fromNum >toNum:
        print ('invalid input')
        return []

    for n in range(fromNum,toNum+1):
        isPrime,factor1,factor2 = findFactors(n)
        if isPrime:
            print ('Prime:' + str(n))
        else:
            print ('{} = {}*{}'.format(n,factor1,factor2))

if __name__ == '__main__':
    lower = input('your lower boundry:')
    higher = input ('higher boundery:')

    r = processNumbers(int(lower),int(higher))
