def popular_words(text: str, words: list) -> dict:
    lower_text = text.lower()
    word_count = {}
    for word in words:
        word_count[word] = lower_text.split().count(word)
    return word_count
# def popular_words (text, words):
# pass
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
