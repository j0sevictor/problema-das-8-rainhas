from population import Population, generateStartedPopulation, createProbabilities, selectParents, addPopulations
from parameters import MAX_TAM_POPULATION, MAX_ITERATION
from individual import Individual, crossover
from .algorithm import Algorithm

class GeneticAlgorithm(Algorithm):

    def __init__(self) -> None:
        self.__population: Population = generateStartedPopulation()
        super().__init__()

    def getPopulation(self) -> Population:
        """
        Retorna a ppopulação do algoritmo.
        """
        return self.__population
    
    def removeBadIndividuals(self) -> None:
        """
        Remove continuamente o pior elemento da população.\n
        Isso enquanto a população tenha mais indivíduos que o definido em ``MAX_TAM_POPULATION``.
        """
        while self.getPopulation().getPopulationSize() > MAX_TAM_POPULATION:
            self.getPopulation().removeWoseIndividual()

    # overriding abstract method
    def bestIndividual(self) -> Individual:
        return self.__population.bestIndividual()

    # overriding abstract method
    def run(self) -> Individual:
        while self.getGeneration() <= MAX_ITERATION and not self.hasBestFitness():
            newPopulation = Population()
            probabilities: list[float] = createProbabilities(self.getPopulation())
            for _ in range(self.getPopulation().getPopulationSize()):
                father, mother = selectParents(self.getPopulation(), probabilities)
                child1, child2 = crossover(father, mother, self.getGeneration())
                newPopulation.add(child1)
                newPopulation.add(child2)
            addPopulations(self.getPopulation(), newPopulation)
            self.removeBadIndividuals()

            print('-' * 27 + f' Generation {self.getGeneration():2} ' + '-' * 27)
            print(self.getPopulation())

            self.nextGeneration()
        return self.bestIndividual()
