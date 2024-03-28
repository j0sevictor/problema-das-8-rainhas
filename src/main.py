from GA import GeneticAlgorithm

if __name__ == '__main__':
    GA = GeneticAlgorithm()
    best = GA.run()
    print(f'Beste Individual:\n {best}')
