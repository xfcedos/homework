count = 0
alphabet = []
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    alphabet.append(char)
trianglenums = []
for n in range(1, 50):
    trianglenums.append(n*(n+1)/2)
words = open("words.txt").read().replace('"', '').split(",")
for word in words:
    sum = 0
    for char in word:
        sum = sum + alphabet.index(char) + 1
    if sum in trianglenums:
        count = count + 1
print(count)
