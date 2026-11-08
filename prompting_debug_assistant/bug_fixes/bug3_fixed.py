def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty.")

    total = sum(numbers)
    count = len(numbers)

    average = total / count

    return average


def main():
    numbers = []

    try:
        result = calculate_average(numbers)
        print("Average:", result)
    except ValueError as error:
        print("Error:", error)


main()
