class Person:
    def __init__(self, name):
        self.name = name


class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
        else:
            print("The bus is full.")

    def remove_passenger(self):
        if self.passengers:
            self.passengers.pop()
        else:
            print("The bus is empty.")


bus = Bus(2)

person_1 = Person("Ana")
person_2 = Person("Carlos")
person_3 = Person("Luis")

bus.add_passenger(person_1)
bus.add_passenger(person_2)
bus.add_passenger(person_3)

print(len(bus.passengers))