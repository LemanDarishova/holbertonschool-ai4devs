def get_last_items(items, n):
    """Return the last n items from a list."""
    if n <= 0:
        return []
    return items[-n:]


def main():
    numbers = [10, 20, 30, 40, 50]
    print(get_last_items(numbers, 2))  # Expected: [40, 50]


if __name__ == "__main__":
    main()
