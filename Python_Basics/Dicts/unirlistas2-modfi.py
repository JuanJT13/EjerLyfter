lista_a = ["name", "age", "country"]
lista_b = ["Juan", "20", "Costa Rica"]

dictionary = {}

for key, value in zip(lista_a, lista_b):
    dictionary[key] = value

print(dictionary)