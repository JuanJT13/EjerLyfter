from datetime import date


class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()

        age = today.year - self.date_of_birth.year

        if (today.month, today.day) < (
            self.date_of_birth.month,
            self.date_of_birth.day
        ):
            age -= 1

        return age


def adult_required(function):
    def wrapper(user, *args, **kwargs):
        if user.age < 18:
            raise ValueError("El usuario debe ser mayor de edad.")

        return function(user, *args, **kwargs)

    return wrapper


@adult_required
def enter_bar(user):
    return "Acceso permitido"


user = User(date(2000, 5, 10))

print(user.age)
print(enter_bar(user))   