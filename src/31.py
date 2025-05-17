def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("The average is:", average)
