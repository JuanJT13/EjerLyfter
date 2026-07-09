def show_menu():

    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Clear result")
    print("6. Exit")


def get_number():

    while True:

        try:
            number = float(input("Enter a number: "))
            return number

        except:
            print("Invalid number")


def add(current, number):

    return current + number


def subtract(current, number):

    return current - number


def multiply(current, number):

    return current * number


def divide(current, number):

    if number == 0:
        print("Cannot divide by zero")
        return current

    return current / number


def main():

    current_number = float(input("Enter the initial number: "))

    while True:

        print("\nCurrent number:", current_number)

        show_menu()

        option = input("Choose an option: ")

        if option == "1":

            number = get_number()

            current_number = add(current_number, number)

            print("Result:", current_number)


        elif option == "2":

            number = get_number()

            current_number = subtract(current_number, number)

            print("Result:", current_number)


        elif option == "3":

            number = get_number()

            current_number = multiply(current_number, number)

            print("Result:", current_number)


        elif option == "4":

            number = get_number()

            current_number = divide(current_number, number)

            print("Result:", current_number)


        elif option == "5":

            current_number = 0

            print("Result cleared")


        elif option == "6":

            print("Goodbye")
            break


        else:

            print("Invalid option")


main()