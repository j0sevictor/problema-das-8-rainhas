from population import Population, generateStartedPopulation, createProbabilities, selectParents, addPopulations
from individual import Individual, crossover
from parameters import FIRST_GENERATION, MAX_TAM_POPULATION, BEST_FITNESS, MAX_ITERATION

class GeneticAlgorithm():

    def __init__(self) -> None:
        self.__population: Population = generateStartedPopulation()
        self.__generation: int = FIRST_GENERATION
    
    def getGeneration(self) -> int:
        return self.__generation
    
    def getPopulation(self) -> Population:
        return self.__population
    
    def bestFitness(self) -> int:
        return self.__population.bestIndividual().getFitness()
    
    def hasBestFitness(self) -> bool:
        return self.bestFitness == BEST_FITNESS
    
    def removeBadIndividuals(self) -> None:
        while self.getPopulation().getPopulationSize() > MAX_TAM_POPULATION:
            self.getPopulation().removeWoseIndividual()

    def nextGeneration(self) -> None:
        self.__generation += 1

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
        return self.getPopulation().bestIndividual()

