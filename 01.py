word = input().upper().split(" + ")
cifra = int(input())
print(", ".join(filter(lambda x: not len(x) % cifra, word)))
