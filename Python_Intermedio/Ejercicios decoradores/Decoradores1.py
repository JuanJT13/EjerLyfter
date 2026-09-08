def print_parameters_and_result(function):
    def wrapper(*args, **kwargs):
        print("Parámetros:", args, kwargs)

        result = function(*args, **kwargs)

        print("Retorno:", result)

        return result

    return wrapper


@print_parameters_and_result
def add(a, b):
    return a + b


add(5, 3)