import random

# Параметры
length = 20 # длина цепочки ДНК
population_size = 20 # размер популяции
generations = 10 # количество поколений
population_mutation = 1.0 # шанс мутации индивида внутри популяции
number_mutations = 1 # Количество мутаций за итерацию

# ФУНКЦИИ

# Генерирование (прочитывание из файла) базовой популяции
def generate_DNA(length):
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
def multiply_population(population, length=length):
    # primitiva recoimbination
    for _ in range(len(population)):
        parents = population[_ : _ + 2]
        child = parents[0][0:length//2] + parents[1][length//2::]
        population.append(child)
    return population

# ЭВОЛЮЦИЯ
# Генерирование (прочитывание из файла) базовой популяции
print("Generating base population")
population_list = [generate_DNA(length) for _ in range(population_size)]
population_selected = population_list
population_size = len(population_selected)
generation = 1

while population_size > 1:
    print("Generation # " + str(generation))
    print("Population size: " + str(population_size))
    # Скрещивание (мутация)
    population_mutated = [mutate_DNA(creature) for creature in population_selected]
    # Получение признаков/ прочитывание генов (подсчет % нуклеотидов)
    # Отбор на основе признаков/критериев (GC < 0.4)
    population_selected = selection(population_mutated, 0.6)
    population_new = multiply_population(population_selected)

    population_size = len(population_new)
    print("Population size: " + str(population_size))
    generation += 1

# Получение результатов работы И/ИЛИ визуализация
