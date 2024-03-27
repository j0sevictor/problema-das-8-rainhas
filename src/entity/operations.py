from .entity import Entity, SIZE
from random import randint

def fitness(entity: Entity):
    """
    Avalia a qualidade de um indivíduo.\n
    Dado pela quantidade pares de rainhas que não se ameaçam. 
    """
    fitValue = 0
    for i in range(SIZE):
        for j in range(i + 1, SIZE):
            # Checa se o par de rainhas i, j está na mesma linha
            if entity.get(i) == entity.get(j): continue
            # Checa se o par de rainhas i, j está na mesma diagonal primária
            if abs(i - entity.get(i)) == abs(j - entity.get(j)): continue
            # Checa se o par de rainhas i, j está na mesma diagonal secundária
            if (i + j) == (SIZE + 1): continue
            fitValue += 1
    return fitValue 

def crossover(father: Entity, mother: Entity, generation: int) -> tuple[Entity, Entity]:
    """
    Gera dois filhos a partir dos dois indivúduis passados.\n
    Os filhos são criados a partir de um index de corte dos vetores dos pais.\n
    Existe um posibilidade dos filhos sofrerem mutações
    """
    # Gera o index de corte
    cutIndex = randint(1, SIZE - 2)
    vector1 = father.getVector()[:cutIndex] + mother.getVector()[cutIndex:]
    vector2 = mother.getVector()[:cutIndex] + father.getVector()[cutIndex:]
    
    return Entity(vector1, generation), Entity(vector2, generation)


