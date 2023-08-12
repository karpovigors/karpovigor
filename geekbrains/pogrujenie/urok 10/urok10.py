class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def display_info(self):
        print(f"{self.name} is a {self.species}.")

class Fish(Animal):
    def __init__(self, name, species, habitat):
        super().__init__(name, species)
        self.habitat = habitat

    def display_info(self):
        print(f"{self.name} is a {self.species} and lives in {self.habitat}.")

class Bird(Animal):
    def __init__(self, name, species, can_fly):
        super().__init__(name, species)
        self.can_fly = can_fly

    def display_info(self):
        print(f"{self.name} is a {self.species} and can fly: {self.can_fly}.")

class Mammal(Animal):
    def __init__(self, name, species, legs):
        super().__init__(name, species)
        self.legs = legs

    def display_info(self):
        print(f"{self.name} is a {self.species} and has {self.legs} legs.")

# Класс-фабрика
class AnimalFactory:
    def create_animal(self, animal_type, *args):
        if animal_type == "Fish":
            return Fish(*args)
        elif animal_type == "Bird":
            return Bird(*args)
        elif animal_type == "Mammal":
            return Mammal(*args)
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Задача по сериализации данных
class Serializer:
    def __init__(self, data=None):
        self.data = data

    def serialize_to_json(self):
        import json
        return json.dumps(self.data)

    def deserialize_from_json(self, json_data):
        import json
        self.data = json.loads(json_data)

# Пример использования:
print("\nAnimal Factory:")
factory = AnimalFactory()
f = factory.create_animal("Fish", "Goldfish", "Fish", "Freshwater")
f.display_info()

b = factory.create_animal("Bird", "Eagle", "Bird", True)
b.display_info()

m = factory.create_animal("Mammal", "Dog", "Canine", 4)
m.display_info()

print("\nSerializer:")
s = Serializer({"name": "John", "age": 30})
json_data = s.serialize_to_json()
print("Serialized Data:", json_data)

s.deserialize_from_json(json_data)
print("Deserialized Data:", s.data)
