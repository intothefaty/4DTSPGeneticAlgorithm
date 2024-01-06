import random
import numpy as np

# calculate_higher_fitness fonksiyonu bize child ve parentlar arasındaki
# en düşük fitness değerinin hangisi olduğunu döndürür
def calculate_higher_fitness(parent1_fitness, parent2_fitness, child_fitness):
    if child_fitness > parent1_fitness and child_fitness > parent2_fitness:
        return 0
    else:
        if parent1_fitness > parent2_fitness:
            return 1
        else:
            return 2

# create_random_cities fonksiyonu numpy kütüphanesinin
# random fonksiyonu ile bize parametre olarak verdiğimiz
# şehir sayısı kadar 4 değişkenli şehirler oluşturur
# 1. değişken x koordinatı
# 2. değişken y koordinatı
# 3. değişken zaman penceresi başlangıcı
# 4. değişken zaman penceresi bitişi
def create_random_cities(num_cities):
    return np.random.rand(num_cities, 4)


# calculate_distance fonksiyonu iki şehrin arasındaki mesafeyi öklit yöntemi ile hesaplar
# (x1-x2)^2 + (y1-y2)^2 = distance^2
def calculate_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


# şehirleri verilen rotada toplam gidilecek mesafeyi hesaplar
# rotayı gezerek şehirler arasındaki mesafeleri toplayarak
def fitness(route, cities):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += calculate_distance(cities[route[i]], cities[route[i + 1]])
    return total_distance


# popülasyondaki birey sayısı ve şehir sayısı verildiğinde
# başındaki ve sonundaki şehir 0 olacak şekilde (başlangıç ve bitiş şehri)
# rastgele rotalar oluşturarak ilk popülasyonu oluşturur
def create_initial_population(pop_size, num_cities):
    population = []
    for _ in range(pop_size):
        route = [0]
        route.extend(random.sample(range(1, num_cities), num_cities - 1))
        route.append(0)
        population.append(route)
    return population


# ilk ve son şehir hariç rastgele bir aralık seçer
# 1. parentta bu iki aralıkta bulunan şehirleri childa aktarır
# geri kalan şehirleri sırasıyla geriye kalan boşluklara yerleştirir
# boşluk anlamını -1 değeri ile sağladık
def crossover(parent1, parent2):
    child = [-1] * (len(parent1) - 1)
    child[0] = 0
    child.append(0)
    start, end = sorted(random.sample(range(1, len(parent1) - 1), 2))
    child[start:end] = parent1[start:end]
    for city in parent2:
        if city not in child:
            for i in range(len(child)):
                if child[i] == -1:
                    child[i] = city
                    break
    return child


# rota ve mutasyon ihtimali verildiğinde
# mutasyon ihtimali gerçekleşmişse rastgele iki değer belirler
# bu değerler ilk ve son değer olamaz
# bu iki değerdeki şehirler yer değiştirir ve mutasyona uğramış olur
def mutate(route, mutation_rate):
    for i in range(1, len(route) - 1):
        if random.random() < mutation_rate:
            swap_with = random.randint(1, len(route) - 1)
            route[i], route[swap_with] = route[swap_with], route[i]
    return route


# şehir sayısı
num_cities = 10

# popülasyon boyutu
pop_size = 10

# mutasyon ihtimali
mutation_rate = 0.01

# Kaç nesil ilerletileceği
iter_count = 100

# rastgele değerlere sahip istenen kadar şehir oluşturulur
cities = create_random_cities(num_cities)
# rastgele rotalara sahip istenen kadar rota oluşturularak ilk popülasyon oluşturulur
population = create_initial_population(pop_size, num_cities)

# ilk popülasyonu yazdırır
print("\nİlk Popülasyon\n")
for route in population:
    print(route, fitness(route, cities))

# uzaklıklar hesaplanır ve bir listeye atılır
distances = []
for item in population:
    distances.append(fitness(item, cities))

# listenin en küçük değeri en iyi değer olacağı için
# en kısa mesafeye sahip rotanın uzunluğu yazılır
min_dist = min(distances)
print("\nMinimum Total Distance", min_dist)

for j in range(iter_count):

    # popülasyonda çaprazlama için index listesi oluşturulur
    pop_selection = list(range(pop_size))

    for i in range(0, len(population), 2):
        # popülasyondaki bireylerden biri rastgele seçilir
        # bu seçim index listesinden seçilir
        parent1_index = int(np.random.rand() * len(pop_selection))
        # popülasyondaki çaprazlamalarda aynı bireylerin kullanılmaması için
        # seçilen index, index listesinden çıkartılır
        pop_selection.pop(parent1_index)
        # aynı işlemler 2. parent seçiminde de yapılır
        parent2_index = int(np.random.rand() * len(pop_selection))
        pop_selection.pop(parent2_index)

        # seçilen indexler üzerinden parent rotaların ataması yapılır
        parent1, parent2 = population[parent1_index], population[parent2_index]
        # child oluşması için çaprazlama yapılır
        child = crossover(parent1, parent2)
        # mutasyon fonksiyonuna girer ve mutasyon ihtimaline göre
        # mustasyona uğrar ya da uğramaz
        mutated_child = mutate(child, mutation_rate)
        # child, parent1, parent2 rotalarının fitnessı yani total distanceları hesaplanır
        route_fitness = fitness(mutated_child, cities)
        parent1_fitness = fitness(parent1, cities)
        parent2_fitness = fitness(parent2, cities)
        # child, parent1 ve parent2 üçlüsünden en yüksek mesafedeki belirlenir
        # child için 0, parent1 için 1, parent2 için 2
        change_index = calculate_higher_fitness(
            parent1_fitness, parent2_fitness, route_fitness
        )
        # 1 ya da 2 gelmişse popülasyondaki yeri child ile değiştirilir
        if change_index == 1:
            population[parent1_index] = mutated_child
        elif change_index == 2:
            population[parent2_index] = mutated_child

    # Eğer daha iyi bir sonuca ulaşılmışsa
    # yeni popülasyon ve en kısa mesafe yazdırılır
    # kaçıncı iterasyonda oluştuğu da belirtilir
    distances = []
    for item in population:
        distances.append(fitness(item, cities))
    if min_dist > min(distances):
        min_dist = min(distances)

        # Eğer tüm iterasyonları görmek istiyorsanız
        # aşağıdaki satırları if bloğundan çıkartmanız yeterli
        print("\n******************************\n")
        print(str(j + 1) + ". İterasyon\n")
        for route in population:
            print(route, " T.Distance: ", fitness(route, cities))
        print("\nYeni Minimum Total Distance:", min_dist)
