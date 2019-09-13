finalsum = 0
for n in range (1, 1000):
    i = pow(n, n)
    finalsum = finalsum + i
print(str(finalsum)[-10:])
