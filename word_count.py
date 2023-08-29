def word_count(text):
    words = text.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count # O(n)


text = "Hello World"
print(word_count(text))
# {'Hello': 1, 'World': 1}
