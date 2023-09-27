def calculate_median(numbers):
    numbers.sort()

    if not numbers:
        return None

    middle_index = len(numbers) // 2

    if len(numbers) % 2 == 1:
        return numbers[middle_index]
    else:
        middle1 = numbers[middle_index - 1]
        middle2 = numbers[middle_index]
        return (middle1 + middle2) / 2

try:
    print("Enter a list of numbers separated by commas: ")
    input_str = input()
    numbers = [float(value) for value in input_str.split(",")]

    median = calculate_median(numbers)

    if median is not None:
        print("Median:", median)
except ValueError:
    print("Some input could not be converted to a number!")
def calculate_median(numbers):
    numbers.sort()

    if not numbers:
        return None

    middle_index = len(numbers) // 2

    if len(numbers) % 2 == 1:
        return numbers[middle_index]
    else:
        middle1 = numbers[middle_index - 1]
        middle2 = numbers[middle_index]
        return (middle1 + middle2) / 2

try:
    print("Enter a list of numbers separated by commas: ")
    input_str = input()
    numbers = [float(value) for value in input_str.split(",")]

    median = calculate_median(numbers)

    if median is not None:
        print("Median:", median)
except ValueError:
    print("Some input could not be converted to a number!")
