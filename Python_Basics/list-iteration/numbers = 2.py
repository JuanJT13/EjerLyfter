numbers = []
for i in range(10):
    n = int(input(f"ingrese el numero {i+1}:"))
    numbers.append(n)
mayor = max(numbers)
print(numbers)
print("El mas alto fue:", mayor)
