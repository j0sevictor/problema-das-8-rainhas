from GA import GeneticAlgorithm
from population import createProbabilities

if __name__ == '__main__':
    GA = GeneticAlgorithm()
    best = GA.run()
    print(f'Beste Individual:\n {best}')
