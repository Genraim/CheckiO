def find_message(str):
    message = ""
    for letter in str:
        if letter.isupper():
            message += letter
    return message
print(find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO")