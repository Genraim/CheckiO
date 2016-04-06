def checkio(str):
    str = str.lower()
    str = str.split(' ')
    three_word_checker = 0
    for w in str:
        if w.isalpha():
           three_word_checker += 1
        else:
            three_word_checker = 0
        if three_word_checker == 3:
            return True
    if three_word_checker < 3:
        return False
    return True

print(checkio("Hello World hello") == True)
print(checkio("He is 123 man") == False)
print(checkio("1 2 3 4") == False)
print(checkio("bla bla bla bla") == True)
print(checkio("Hi") == False)


def checkio_best(words):
    succ = 0
    for word in words.split():
        succ = (succ + 1)*word.isalpha()
        if succ == 3: return True
    else: return False
