from abc import ABC, abstractmethod
from individual import Individual
from parameters import BEST_FITNESS, FIRST_GENERATION

class Algorithm(ABC):

    def __init__(self) -> None:
        self.__generation: int = FIRST_GENERATION

    def getGeneration(self) -> int:
        """
        Retorna a geração atual do algoritmo.
        """
        return self.__generation
    
    def nextGeneration(self) -> None:
        """
        Incrementa em 1 o atributo geração.
        """
        self.__generation += 1
    
    def resetGenerations(self) -> None:
        """
        Zera o número de gerações.
        """
        self.__generation = 0

    @abstractmethod
    def run(self) -> Individual:
        """
        Executa o algoritmo e retorna o melhor indivíduo encontrado.
        """

    @abstractmethod
    def bestIndividual(self) -> Individual:
        """
        Retorna o melhor indivíduo com base nos valores de ``fitness`` encontrados.
        """
    
    def bestFitness(self) -> int:
        """
        Retorna o melhor valor de ``fitness`` encontrado.
        """
        return self.bestIndividual().getFitness()
    
    def hasBestFitness(self) -> bool:
        """
        Retorna ``True`` se o indivíduo ótimo foi encontrado.
        """
        return self.bestFitness() == BEST_FITNESS
