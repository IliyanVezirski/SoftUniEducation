class Vet:
    space = 5
    animals = []
    def __init__(self, name):
        self.name = name
        self.current_animals = 0
        self.animals = []

    def register_animal(self, animal_name):
        if self.current_animals < self.space:
            self.animals.append(animal_name)
            self.current_animals += 1
            return f"{animal_name} registered in the clinic"
        else:
            return f"Not enough space"

    def unregister_animal(self, animal_name):
        if animal_name in self.current_animals:
            self.animals.remove(animal_name)
            self.current_animals -= 1
            return f"{animal_name} unregistered successfully"
        else:
            return f"{animal_name} not in the clinic"

    def info(self):
        return f'{self.name} has {self.current_animals} animals. {self.space - len(self.animals)} space left in clinic'

