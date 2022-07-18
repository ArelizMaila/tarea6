# Función 1. Creación de una población con alelos al azar

import scipy

def build_population(N, p):
    """En la creación de la población se tienen dos variables, N que es número de individuos de la población y p que es la probabilidad de obtener el alelo dominante A. Para generar una población al azar se utilizará scipy, es decir que los pares de alelos de la población se formaran aleatoriamente.
    """
    population = []
    for i in range(N):
        allele1 = "A"
        if scipy.random.rand() > p:
            allele1 = "a"
        allele2 = "A"
        if scipy.random.rand() > p:
            allele2 = "a"
        population.append((allele1, allele2))
    return population

#Función 2. Cuantificación de frecuencias de alelos (Conteo de pares de alelos).

def compute_frequencies(population):
    """ En este apartado se cuentan las frecuencias genotipicas"""
    AA = population.count(("A", "A"))
    Aa = population.count(("A", "a"))
    aA = population.count(("a", "A"))
    aa = population.count(("a", "a"))
    return({"AA": AA, "aa": aa, "Aa": Aa, "aA": aA})

#Función 3. Creación de la población hija.(Creación de una nueva población)

def reproduce_population(population):
    """ Para crear la nueva población se cumplirá para cada individuo nuevo que:
        - Los padre se seleccionan aleatoriamente 
        - La desendecia recibe un cromosoma de cada uno de los padres.
    """
    new_generation = []
    N = len(population)
    for i in range(N):
        # random integer between 0 and N-1
        dad = scipy.random.randint(N)
        mom = scipy.random.randint(N)
        # which chromosome comes from mom
        chr_mom = scipy.random.randint(2)
        offspring = (population[mom][chr_mom], population[dad][1 - chr_mom])
        #if offspring == ("a", "a"): 
          #next()
        new_generation.append(offspring)
    return new_generation

