from .individual import Individual, SIZE, RANGE_END, RANGE_START
from random import randint, choices

MUTATION_RATE = .01

def fitness(individual: Individual) -> int:
    """
    Avalia a qualidade de um indivíduo.\n
    Dado pela quantidade pares de rainhas que não se ameaçam. 
    """
    fitValue: int = 0
    for i in range(SIZE):
        for j in range(i + 1, SIZE):
            # Checa se o par de rainhas i, j está na mesma linha
            if individual.get(i) == individual.get(j): continue
            # Checa se o par de rainhas i, j está na mesma diagonal primária
            if abs(i - individual.get(i)) == abs(j - individual.get(j)): continue
            # Checa se o par de rainhas i, j está na mesma diagonal secundária
            if (i + j) == (SIZE + 1): continue
            fitValue += 1
    return fitValue 

def crossover(father: Individual, mother: Individual, generation: int) -> tuple[Individual, Individual]:
    """
    Gera dois filhos a partir dos dois indivúduis passados.\n
    Os filhos são criados a partir de um index de corte dos vetores dos pais.\n
    Existe um posibilidade dos filhos sofrerem mutações
    """
    # Gera o index de corte
    cutIndex = randint(1, SIZE - 2)
    vector1 = father.getVector()[:cutIndex] + mother.getVector()[cutIndex:]
    vector2 = mother.getVector()[:cutIndex] + father.getVector()[cutIndex:]

    individual1 = Individual(vector1, generation)
    individual2 = Individual(vector2, generation)
    
    mutation(individual1)
    mutation(individual2)

    return individual1, individual2 

def mutation(individual: Individual) -> None:
    """
    Gera mutações nos genes do indivíduo passado.\n
    Isso a depender da taxa de mutação.
    """
    def hasMutation() -> bool:
        """
        Retorna ``True`` ou ``False``.\n
        P(True) = MUTATION_RATE\n
        P(False) = 1 - MUTATION_RATE
        """
        return choices([True, False], weights=[MUTATION_RATE, 1 - MUTATION_RATE])[0]
    
    for i in range(individual.getVectorSize()):
        if hasMutation():
            individual.set(i, randint(RANGE_START, RANGE_END))

