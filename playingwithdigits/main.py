def dig_pow(num, p):
    nsum = 0 
    for i,n in enumerate(str(num)):
        number = int(n)
        pp = p+i
        nsum= nsum + number**pp

    if (nsum%num == 0):
        return (int(nsum/num))
    else:   
        return -1

# dig_pow(89, 1)
# dig_pow(92, 1)
dig_pow(46288, 3)