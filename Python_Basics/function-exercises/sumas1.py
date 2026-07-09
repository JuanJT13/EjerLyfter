def sum_list(numbers_list):
    total_sum = 0
    for number in numbers_list:
        total_sum +=number
    return total_sum
my_list = [4, 6, 23, 29]
resultado = sum_list(my_list)

print(resultado)