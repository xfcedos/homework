c = 0
for a in range(999, 900, -1):
    for b in range(999, 900, -1):
        c = a * b
        if c == int(str(c)[::-1]):
            print(c)
            quit()
