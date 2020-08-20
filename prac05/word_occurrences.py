text=str(input("Please enter the test: "))
words = text.split()
counts = dict()
dict={}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
    dict[word] = counts[word]

print("text: {}".format(text))
for i in dict:
    print("{:{}} : {}".format(i, 10, counts[i]))





