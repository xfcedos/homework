maxcount = 0
neededn = 0
for n in range(1000000, 1, -1):
    count = 1
    backupn = n
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n+1
        count = count + 1
        if maxcount < count:
            maxcount = count
            neededn = backupn
        continue
    continue
print(neededn)
