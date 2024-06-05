def classify_words(sentence):
    words = sentence.split()

    alphabetic_words = []
    numeric_words = []
    alphanumeric_words = []

    for word in words:
        if word.isalpha():
            alphabetic_words.append(word)
        elif word.isdigit():
            numeric_words.append(word)
        elif word.isalnum():
            alphanumeric_words.append(word)

    return alphabetic_words, numeric_words, alphanumeric_words

sentence = input("문장을 입력하시오: ")

alphabetic_words, numeric_words, alphanumeric_words = classify_words(sentence)
print("영문 단어:", ' '.join(alphabetic_words))
print("숫자:", ' '.join(numeric_words))
print("영문자+숫자:", ' '.join(alphanumeric_words))
