list = (11, 14, 17, 20, 25, 30, 43, 53, 34, 90)
new_list = []
for num in list:
    if num % 2 == 0:
        new_list.append(num)
        print(new_list)