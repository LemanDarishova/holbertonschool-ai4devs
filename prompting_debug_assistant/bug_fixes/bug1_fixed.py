def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"


def main():
    age = 22
    result = check_age(age)
    print("User status:", result)


main()
