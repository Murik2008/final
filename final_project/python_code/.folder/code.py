from datetime import datetime

class Animal:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def show_commands(self):
        return self.commands

    def age_in_months(self):
        return (datetime.now().year - self.birth_date.year) * 12 + datetime.now().month - self.birth_date.month

class DomesticAnimal(Animal):
    def __init__(self, name, birth_date, animal_type):
        super().__init__(name, birth_date)
        self.animal_type = animal_type

class PackAnimal(Animal):
    def __init__(self, name, birth_date, animal_type):
        super().__init__(name, birth_date)
        self.animal_type = animal_type

class Registration:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def show_all_animals(self):
        for animal in self.animals:
            print(f"Name: {animal.name}, Type: {type(animal).__name__}, Commands: {animal.show_commands()}")

    def train_animal(self, animal_name, command):
        for animal in self.animals:
            if animal.name == animal_name:
                animal.add_command(command)
                print(f"Added command '{command}' to {animal.name}")


registration = Registration()


dog = DomesticAnimal(name="Buddy", birth_date="2021-06-15", animal_type="Dog")
registration.add_animal(dog)


registration.train_animal("Buddy", "Sit")

registration.show_all_animals()

class Counter:
    def __init__(self):
        self._count = 0
        self._is_resource_open = False

    def __enter__(self):
        self._is_resource_open = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._is_resource_open = False

    def add(self):
        if not self._is_resource_open:
            raise RuntimeError("Counter must be used within a 'with' statement")
        self._count += 1

    @property
    def count(self):
        return self._count


try:
    with Counter() as counter:
        counter.add()
        print(f"Counter value: {counter.count}")
except RuntimeError as e:
    print(e)