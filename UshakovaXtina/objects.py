import random

class Creature:
    def __init__(self, DNA_length=20):
        self.DNA_length = DNA_length
        self.DNA = ''.join(random.choice('CGTA') for _ in range(DNA_length))

    def mutate_DNA(self, number_mutations=1):
        DNA_list = [i for i in self.DNA] #перевод строки в лист т.к строки неизменяемы
        for _ in range(number_mutations):
            DNA_list[random.randrange(len(DNA_list))] = random.choice('ATGC') #выбираем рандомный индекс в созданном выше листе и заменяем на рандомну
            self.DNA = ''.join(DNA_list)


class Population:
    def __init__(self, population_size=20):
        self.population_size = population_size

    def initial_population(population_size=20):
        return [Creature() for _ in range(20)]

    #def mutate():
        # mutate creatures
