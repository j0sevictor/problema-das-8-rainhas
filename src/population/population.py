from random import choices
from individual import Individual, generateStartedIndividual
from parameters import MAX_TAM_POPULATION

class Population():
    """
    Representação da populção de inidivíduos.
    """

    def __init__(self) -> None:
        self.__individuals: list[Individual] = []
        self.__totalFitness = 0
        self.__qtdIndividuals = 0

    def getPopulationSize(self) -> int:
        """
        Retorna a quantidade de indivíduos atualmente na população.
        """
        return self.__qtdIndividuals

    def getIndividuals(self) -> list[Individual]:
        """
        Retorna a lista de indivíduos da população.
        """
        return self.__individuals

    def getTotalFitness(self) -> int:
        """
        Retorna o somatório dos atributos ``fitness`` dos indivíduos.
        """
        return self.__totalFitness

    def empty(self) -> bool:
        """
        Retorna se a população é vazia ou não.
        """
        return self.__qtdIndividuals == 0

    def full(self) -> bool:
        """
        Retorna se a população está cheia.
        """
        return self.__qtdIndividuals == MAX_TAM_POPULATION

    def getIndividal(self, index: int) -> Individual:
        """
        Retorna o indivíduo da população identificado pelo índice.
        """
        if index < 0 or index >= self.__qtdIndividuals:
            raise ValueError('index out of bound')
        return self.__individuals[index]

    def add(self, individual: Individual) -> bool:
        """
        Adiciona um novo indivíduo a população.
        """
        inserted = False
        if self.empty():
            self.__individuals.append(individual)
            inserted = True

        for i in range(self.getPopulationSize()):
            if individual.getFitness() > self.getIndividal(i).getFitness():
                self.__individuals.insert(i, individual)
                inserted = True
                break

        if not inserted and not self.full():
            self.__individuals.append(individual)
            inserted = True

        if inserted:
            self.__totalFitness += individual.getFitness()
            self.__qtdIndividuals += 1
        return inserted

    def bestIndividual(self) -> Individual:
        """
        Retorna o melhor indivíduo da população.
        """
        return self.__individuals[0]

    def removeWoseIndividual(self) -> None:
        """
        Remove o indivíduo com pior valor de ``fitness``.
        """
        individual = self.__individuals.pop()
        self.__totalFitness -= individual.getFitness()
        self.__qtdIndividuals -= 1

    def __repr__(self) -> str:
        return f'Population(totalFitness={self.__totalFitness},\
        qtdIndividuals={self.__qtdIndividuals})'

    def __str__(self) -> str:
        strPop = '-' * 26 + f' {self.getPopulationSize():2} Individuals ' + '-' * 26 + '\n'
        for individual in self.__individuals:
            strPop += individual.__str__() + '\n'
        if self.empty():
            strPop += 'Population Empty'
        return strPop

def generateStartedPopulation() -> Population:
    """
    Gera uma população de indivíduos gerados aleatóriamente.\n
    O tamanho da população é definido por ``MAX_TAM_POPULATION``.
    """
    population = Population()
    for _ in range(MAX_TAM_POPULATION):
        population.add(generateStartedIndividual())
    return population

def selectParents(population: Population, probabilities: list[float]) \
    -> tuple[Individual, Individual]:
    """
    Seleciona dois indivíduos da população com base nas probabilidades de cada um.
    """
    parent1 = choices(population.getIndividuals(), weights=probabilities)[0]
    parent2 = choices(population.getIndividuals(), weights=probabilities)[0]
    while parent1.getId() == parent2.getId():
        parent2 = choices(population.getIndividuals(), weights=probabilities)[0]
    return parent1, parent2

def createProbabilities(population: Population) -> list[float]:
    """
    Gera uma lista com as probabilidades de cada indivíduo da população ser escolhido.
    """
    probabilities = []
    for individual in population.getIndividuals():
        probabilities.append(individual.getFitness() / population.getTotalFitness())
    return probabilities

def addPopulations(oldPopulation: Population, newPopulation: Population) -> None:
    """
    Adiciona os melhores indivíduos da nova população na antiga.
    """
    i = 0
    added = True
    while added and i < newPopulation.getPopulationSize():
        added = oldPopulation.add(newPopulation.getIndividal(i))
        i += 1
