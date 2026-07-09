def is_prime(number):

    if number <= 1:
        return False

    for i in range(2, number):

        if number % i == 0:
            return False

    return True


def get_prime_numbers(numbers):

    prime_numbers = []

    for number in numbers:

        if is_prime(number):
            prime_numbers.append(number)

    return prime_numbers


numbers = [1, 4, 6, 7, 13, 9, 67]

print(get_prime_numbers(numbers))