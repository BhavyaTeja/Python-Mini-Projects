def value(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1


def RomanToNumeric(num):
    res, i = 0, 0
    while(i < len(num)):
        num1 = value(num[i])
        if i+1 < len(num):
            num2 = value(num[i+1])
            if num1 >= num2:
                res = res + num1
                i += 1
            else:
                res = res + num2 - num1
                i += 2
    return res

x = RomanToNumeric('MCMXIV')

print x
