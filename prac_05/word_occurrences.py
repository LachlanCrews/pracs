word_count = {}
text = input("Text: ")
words = text.split()

for i in words:
    frequency = word_count.get(i, 0)
    word_count[i] = frequency + 1

words = list(word_count.keys())
words.sort()

length = max((len(i) for i in words))
for i in words:
    print("{:{}} : {}".format(i, length, word_count[i]))
