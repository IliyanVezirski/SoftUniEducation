from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__budget >= price and self.__animal_capacity - len(self.animals) > 0:
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        if self.__budget < price:
            return f'Not enough budget'
        if self.__animal_capacity - len(self.animals) >= 0:
            return f'Not enough space for animal'

    def hire_worker(self, worker: Worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return f'Not enough space for worker'

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f'{worker_name} fired successfully'
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self, ):
        current_salary = 0
        for worker in self.workers:
            current_salary += worker.salary
        if current_salary <= self.__budget:
            self.__budget -= current_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        current_tend = 0
        for animal in self.animals:
            current_tend += animal.money_for_care
        if current_tend <= self.__budget:
            self.__budget -= current_tend
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = ''
        result += f"You have {len(self.animals)} animals\n"
        lions = []
        tigers = []
        cheetah = []
        for animal in self.animals:
            if animal.__class__.__name__ == 'Lion':
                lions.append(animal)
            elif animal.__class__.__name__ == 'Tiger':
                tigers.append(animal)
            elif animal.__class__.__name__ == 'Cheetah':
                cheetah.append(animal)
        result += f"----- {len(lions)} Lions:\n" + '\n'.join([str(i) for i in lions]) + '\n'
        result += f"----- {len(tigers)} Tigers:\n" + '\n'.join([str(i) for i in tigers]) + '\n'
        result += f"----- {len(cheetah)} Cheetahs:\n" + '\n'.join([str(i) for i in cheetah])
        return result

    def workers_status(self):
        result = ''
        result += f"You have {len(self.workers)} workers\n"
        keeper = []
        caretaker = []
        vets = []
        for worker in self.workers:
            if worker.__class__.__name__ == 'Keeper':
                keeper.append(worker)
            elif worker.__class__.__name__ == 'Caretaker':
                caretaker.append(worker)
            elif worker.__class__.__name__ == 'Vet':
                vets.append(worker)
        result += f"----- {len(keeper)} Keepers:\n" + '\n'.join([str(i) for i in keeper]) + '\n'
        result += f"----- {len(caretaker)} Caretakers:\n" + '\n'.join([str(i) for i in caretaker]) + '\n'
        result += f"----- {len(vets)} Vets:\n" + '\n'.join([str(i) for i in vets])
        return result
