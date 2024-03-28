from parameters import SIZE, RANGE_START, RANGE_END
from individual import Individual, generateStartedIndividual
from .algorithm import Algorithm

class HillClimbing(Algorithm):

    def __init__(self, toOptimal: bool=False) -> None:
        self.__current: Individual = generateStartedIndividual()
        self.__toOptimal: bool = toOptimal
        super().__init__()

    def toOptimal(self) -> bool:
        return self.__toOptimal

    def __setCurrent(self, newIndividual: Individual) -> None:
        """
        Altera o valor do melhor indivídue encontrado.
        """
        self.__current = newIndividual

    def getExecutions(self) -> int:
        """
        Retorna a quantidade de execuções do algoritmo.
        """
        return self.__executions

    def bestNeighbor(self) -> Individual:
        """
        Seleciona o melhor vizinho do indivíduo atual.\n
        Os vizinhos são gerados a partir da movimentação de uma rainha no tabuleiro.
        """
        neighbor: Individual = self.bestIndividual()
        for j in range(SIZE):
            vector = self.bestIndividual().getVector().copy()
            for i in range(RANGE_START, RANGE_END + 1):
                aux = vector[j]
                vector[j] = i
                individual = Individual(vector.copy(), self.getGeneration())
                if individual.getFitness() > neighbor.getFitness():
                    neighbor = individual
                vector[j] = aux
        return neighbor

    # overriding abstract method
    def bestIndividual(self) -> Individual:
        return self.__current

    # overriding abstract method
    def run(self) -> Individual:
        self.resetGenerations()
        while True:
            self.nextGeneration()
            print('-' * 27 + f' Generation {self.getGeneration()} ' + '-' * 27)
            while True:
                print(self.bestIndividual())
                neighborn = self.bestNeighbor()
                if neighborn.getFitness() <= self.bestIndividual().getFitness():
                    break
                self.__setCurrent(neighborn)
            if self.toOptimal() and not self.hasBestFitness():
                self.__setCurrent(generateStartedIndividual())
                continue
            return self.bestIndividual()
            
              
