def pswrd_validator(i):
    password = True

    if len(i) < 8:
        print("Password should be greather than 8 digits.")
        password = False
    if len(i) > 12:
        print("Password should not be greather than 12 digits.")
        password = False
    if not any(char.isdigit() for char in i):
        print("Ther must be atleast one digit in the password.")
        password = False
    if not any(char.isupper() for char in i):
        print("There must be atleast one Uppercase letter in the password.")
        password = False
    if not any(char.islower() for char in i):
        print("There must be atleat one Lowercase letter in the password.")
        password = False
    if password:
        return password


def main():
    i = "Babuca1rr"
    if (pswrd_validator(i)):
        print("Password is correct.")
    else:
        print("Invalid password")


if __name__ == "__main__":
    main()
