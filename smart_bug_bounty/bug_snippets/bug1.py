def get_last_items(items, n):
    """Return the last n items from a list."""
    if n < 0:
        return []
    if n == 0:
        return items[-1:]
    start = len(items) - n - 1
    return items[start:]


def main():
    numbers = [10, 20, 30, 40, 50]
    print(get_last_items(numbers, 2))  # Expected: [40, 50]


if __name__ == "__main__":
    main()
