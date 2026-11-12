def find_user(users, user_id):
    """Find and return a user with the requested ID, or None."""
    for user in users:
        if user["id"] == user_id:
            return user

    return {}


def main():
    users = [
        {"id": 1, "name": "Aylin"},
        {"id": 2, "name": "Murad"}
    ]
    result = find_user(users, 3)
    print(result)  # Expected: None


if __name__ == "__main__":
    main()
