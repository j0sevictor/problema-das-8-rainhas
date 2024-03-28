from random import randint
from parameters import SIZE, RANGE_START, RANGE_END

class Individual():
    __id: int = 1

    def __init__(self, vector: list[int], generation: int) -> None:
        if len(vector) != SIZE:
            raise ValueError(f'O vetor do indivíduo deve conter exatamente {SIZE} posições')

        self.__id: int = Individual.__id
        self.__generation: int = generation
        self.__vector: list[int] = vector
        self.__fitness: int = fitness(self)

        Individual.__id += 1

    def getId(self) -> int:
        """
        Retorna o ID único do indivíduo.
        """
        return self.__id
    
    def getGeneration(self) -> int:
        """
        Retorna na geração em que o indivíduo foi criado.
        """
        return self.__generation

    def getVector(self) -> list[int]:
        """
        Retorna o vetor de valores do indivíduo.
        """
        return self.__vector
    
    def getVectorSize(self) -> int:
        """
        Retorna o tamanho do vetor.
        """
        return len(self.__vector)
    
    def getFitness(self) -> int:
        """
        Retorna a qualidade do indivíduo.
        """
        return self.__fitness
    
    def get(self, index: int) -> int:
        """
        Retorna o valor da posição do vetor especificada pelo ``index``.
        """
        if index < 0 or index >= SIZE:
            raise ValueError('Argumento index fora do limite do vetor')
        return self.__vector[index]
    
    def set(self, index: int, value: int) -> None:
        """
        Altera o valor do gene da posição ``index``.\n
        """
        if value < RANGE_START or value > RANGE_END:
            raise ValueError('O valor passado está fora do limite permitido')
        if index < 0 or index >= SIZE:
            raise ValueError('O index passado está fora do limite do vetor')
        self.__vector[index] = value

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Individual) and __value.getVector() == self.getVector():
            return True
        return False
    
    def __repr__(self) -> str:
        return f'Individual(generation={self.__generation}, id={self.__id}, vector={self.__vector}, fitness={self.__fitness})'
    
    def __str__(self) -> str:
        return f'Generation {self.getGeneration():2} | Genes {self.getVector()} | Fitness {self.getFitness():2} | ID {self.getId()}'


def fitness(individual: Individual) -> int:
    """
    Avalia a qualidade de um indivíduo.\n
    Dado pela quantidade pares de rainhas que não se ameaçam. 
    """
    fitValue: int = 0
    for i in range(SIZE - 1):
        for j in range(i + 1, SIZE):
            # Checa se o par de rainhas i, j está na mesma linha
            if individual.get(i) == individual.get(j): continue
            # Checa se o par de rainhas i, j está na mesma diagonal primária
            if abs(i - individual.get(i)) == abs(j - individual.get(j)): continue
            # Checa se o par de rainhas i, j está na mesma diagonal secundária
            if (i + j) == (SIZE + 1): continue
            fitValue += 1
    return fitValue 

def generateStartedIndividual() -> Individual:
    vector: list[int] = []
    for _ in range(SIZE):
        vector.append(randint(RANGE_START, RANGE_END))
    return Individual(vector, 0)
