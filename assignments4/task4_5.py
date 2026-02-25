def remove_odd(numbers):
    new_list = []
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            new_list.append(numbers[i])
    return new_list
my_list = [1, 2, 3, 4, 5, 6]
even_list = remove_odd(my_list)
print("Original:", my_list)
print("New list:", even_list)