def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)

    average = total / count

    return average


def main():
    numbers = []
    result = calculate_average(numbers)

    print("Average:", result)


main()
