from urllib.request import urlopen

shakespeare = urlopen('http://composingprograms.com/shakespeare.txt')

words = set(shakespeare.read().decode().split())

print(2 + 2)
print({w for w in words if len(w) == 6 and w[::-1] in words})

print({w for w in words if len(w) == 8 and w[::-1] in words})

# https://composingprograms.com/
# 正序反序相同的单词
