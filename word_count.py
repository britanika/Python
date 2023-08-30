def word_count(text):
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1 # O(n)
    return word_count


text = "Hello World"
print(word_count(text))
# {'Hello': 1, 'World': 1}
