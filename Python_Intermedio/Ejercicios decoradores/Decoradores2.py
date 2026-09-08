def validate_numbers(function):
    def wrapper(*args, **kwargs):
        for value in args:
            if not isinstance(value, (int, float)):
                raise TypeError("Todos los parámetros deben ser números.")

        for value in kwargs.values():
            if not isinstance(value, (int, float)):
                raise TypeError("Todos los parámetros deben ser números.")

        return function(*args, **kwargs)

    return wrapper


@validate_numbers
def multiply(a, b):
    return a * b


print(multiply(5, 3))