from GA import GeneticAlgorithm

if __name__ == '__main__':
    GA = GeneticAlgorithm()
    bestIndividual = GA.run()
    print(f'Beste Individual:\n {bestIndividual}')
