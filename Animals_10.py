class Animal:

    def __init__(self, initial_weight, name):
        self.weight_in_grammes = initial_weight
        self.is_alive = True
        # added for lecture 10_Files
        self.name = name 

    def feed(self, food_in_grammes):
        self.weight_in_grammes += (food_in_grammes * 0.05)

    def kill(self):
        self.is_alive = False

    def __str__(self):
        return f"A{'n' if self.is_alive else ' dead'} animal weighing {self.weight_in_grammes} grammes"


class Carnivore(Animal):

    def feed(self, food):
        if isinstance(food, Animal):
            food.kill()
            self.weight_in_grammes += food.weight_in_grammes * 0.1
        else:
            Animal.feed(self, food)
            
            
class Seal(Carnivore):

    def __init__(self, *args, **kwargs):
        self.tricks = list()
        super().__init__(*args, **kwargs)

    def learn_trick(self, trick_name):
        self.tricks.append(trick_name)