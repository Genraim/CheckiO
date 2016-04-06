def count_words(str, s):
    str = str.lower()
    count = 0
    for word in s:
        if str.find(word) != -1:
            count += 1
    return count

print(count_words("blA trblas blabla", {"bla"}))
print(count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3)
print(count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2)
print(count_words("Bananas, give me bananas!!!", {"banana", "bananas"}))
print(count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.", {"sum", "hamlet", "infinity", "anything"}) == 1)


def count_words_better(text, words):
    return sum(word in text.lower() for word in words)


def count_words_lambda(text, words):
    return len(filter(lambda word: text.lower().find(word) >= 0, words))