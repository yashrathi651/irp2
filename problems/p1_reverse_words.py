
def reverse_words(text):
    punctuation = ""

    if text and text[-1] in ".,!?":
        punctuation = text[-1]
        text = text[:-1]

    words = text.split()
    return " ".join(words[::-1]) + punctuation


sentence = input()
print(reverse_words(sentence))
I love coding.