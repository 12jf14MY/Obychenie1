string = "python java c c++ javascript pascal php"
print(string)

words = string.split()
print(words)
print(max(words, key=len))

# id_longest = 0
# c = 0
# for i in words:
#     if len(words) < len(words[c]):
#         id_longest = c
#     c += 1
# print(words[id_longest])
