def remove_odd(numbers):
    result = []

    for num in numbers:
        if num % 2 == 0:
            result.append(num)

    return result


# main program
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

new_list = remove_odd(numbers)

print("Original list:", numbers)
print("Without odd numbers:", new_list)