def NumericToRoman(num):
    roman = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'I': 1}
    list = []
    for key, value in roman.items():
        count = num // value
        num -= count * value
        list.append(count * key)
    return ''.join(list)

print(NumericToRoman(463))