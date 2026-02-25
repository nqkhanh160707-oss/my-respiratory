def sum_list(numbers):
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
    return total
my_list = [1, 2, 3, 4, 5]
result = sum_list(my_list)
print(result)