from population import Population, generateStartedPopulation, createProbabilities, selectParents, addPopulations
from individual import Individual, crossover
from parameters import FIRST_GENERATION, MAX_TAM_POPULATION, BEST_FITNESS, MAX_ITERATION

class GeneticAlgorithm():

    def __init__(self) -> None:
        self.__population: Population = generateStartedPopulation()
        self.__generation: int = FIRST_GENERATION
    
    def getGeneration(self) -> int:
        """
        Retorna a geração atual do algoritmo.
        """
        return self.__generation

    def getPopulation(self) -> Population:
        """
        Retorna a ppopulação do algoritmo.
        """
        return self.__population
    
    def bestFitness(self) -> int:
        """
        Retorna o melhor valor de ``fitness`` encontrado.
        """
        return self.__population.bestIndividual().getFitness()
    
    def hasBestFitness(self) -> bool:
        """
        Retorna ``True`` se na população existe um indivíduo com a solução ótima.
        """
        return self.bestFitness() == BEST_FITNESS
    
    def removeBadIndividuals(self) -> None:
        """
        Remove continuamente o pior elemento da população.\n
        Isso enquanto a população tenha mais indivíduos que o definido em ``MAX_TAM_POPULATION``.
        """
        while self.getPopulation().getPopulationSize() > MAX_TAM_POPULATION:
            self.getPopulation().removeWoseIndividual()

    def nextGeneration(self) -> None:
        """
        Incrementa em 1 o atributo geração.
        """
        self.__generation += 1

    def run(self) -> Individual:
        """
        Executa o algoritmo genético e retorna o melhor indivíduo encontrado.
        """
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

