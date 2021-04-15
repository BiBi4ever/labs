import random

'''

    В этом файле будут жить функции, используемые алгоритмом

'''


# Генерация (прочитывание из файла) базовой популяции
def generate_DNA(length=20):
    DNA = ''.join(random.choice('CGTA') for _ in range(length)) # это с равными вероятностями для любого нуклеотида
    return DNA

# Мутирование строки
def mutate_DNA(DNA, number_mutations=1):
    DNA_list = [i for i in DNA] #перевод строки в лист т.к строки неизменяемы
    for _ in range(number_mutations):
        DNA_list[random.randrange(len(DNA_list))] = random.choice('ATGC') #выбираем рандомный индекс в созданном выше листе и заменяем на рандомну
    return ''.join(DNA_list)

# Получение признаков/ прочитывание генов (подсчет % GC)
def calculate_GC(DNA):
    return (DNA.count('G') + DNA.count('C'))/(len(DNA))

# Отбор (GC < 0.4)
def selection(population, GC_threshold=0.4):
    population_selected = [creature for creature in population if calculate_GC(creature) >= GC_threshold]
    return population_selected

# Размножение/рекомбинация
def multiply_population(population, length=20):
    # primitiva recoimbination
    for _ in range(len(population)):
        parents = population[_ : _ + 2]
        child = parents[0][0:length//2] + parents[1][length//2::]
        population.append(child)
    return population
