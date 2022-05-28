# string = input("Write down a text:\n")
#
# signs = ['.', ',', ':', ';',
#          '!', '?', '(', ')']
#
# words = string.split()
#
# i = 0
# for word in words:
#     if word[-1] in signs:
#         words[i] = word[:-1]
#         word = words[i]
#     if word[0] in signs:
#         words[i] = word[1:]
#     i += 1
#
# for i in words:
#     print(i, end=' ')
# print()

# 2 способ
string = input("Write down a text:\n")
signs = ['.', ',', ':', ';',
         '!', '?', '(', ')']
for i in signs:
    string = string.replace(i, '')


words = string.split()
words = tuple(words)
print(words)


