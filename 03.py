word = input().split("-")
word.remove("question")
word.sort()
print(*word)