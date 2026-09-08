def sort_words(text):

    words = text.split("-")

    words.sort()

    result = "-".join(words)

    return result


text = "python-variable-funcion-computadora-monitor"

print(sort_words(text))