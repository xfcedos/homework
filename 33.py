result = 1.0
for num in range(10, 99):
    d1num = int(str(num)[0])
    d2num = int(str(num)[1])
    num = float(num)
    for denom in range(10, 99):
        denom = float(denom)
        if num % 10 == 0 or denom % 10 == 0 or num >= denom:
            continue
        expected = 0.0
        ddenom = 0
        if str(d1num) in str(denom):
            ddenom = int(str(int(denom)).replace(str(d1num), '', 1))
            expected = float(d2num/ddenom)
        if expected == num/denom:
            result = result * denom/num
        if str(d2num) in str(denom):
            ddenom = int(str(int(denom)).replace(str(d2num), '', 1))
            expected = float(d1num/ddenom)
        if expected == num/denom:
            result = result * denom/num
print(result)
