def add(*args):
    result = 0
    for i in args:
        result += i
    return result


a = add(1, 2, 3, 4)
print(a)


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n, kwargs)


calculate(5, add=2, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="Fiat", model="500x")
print(my_car.make)
