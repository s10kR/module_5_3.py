class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.nuber_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.nuber_of_floors or new_floor < 1:
            print("Такого этажа не существует.")
        else:
            for new_floor in range(new_floor + 1):
                if new_floor < 1:
                    continue
                print(new_floor)
    def __len__(self):
        return self.nuber_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.nuber_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.nuber_of_floors == other.nuber_of_floors
        elif isinstance(other,int):
            return self.nuber_of_floors == other

    def __iter__(self, other):
        return self.nuber_of_floors < other.nuber_of_floors

    def __le__(self, other):
        return self.nuber_of_floors <= other.nuber_of_floors

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, value):
        if isinstance(value, int):
            self.nuber_of_floors += value
        elif isinstance(value, House):
            self.nuber_of_floors += value.nuber_of_floors
            return self

    def __radd__(self, other: int):
        return self.__add__(other)

    def __iadd__(self, other: int):
        return self.__add__(other)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 = 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
