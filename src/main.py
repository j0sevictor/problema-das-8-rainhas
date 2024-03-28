from algorithms import GeneticAlgorithm, HillClimbing, Algorithm
from os import system

def main() -> None:
    while True:
        printMenu()
        option = inputListInt('-> ', [1, 2, 0])

        if option:
            algorithms: dict[int, Algorithm] = {1: GeneticAlgorithm(), 2: HillClimbing(toOptimal=True)}

            bestIndividual = algorithms[option].run()
            print(f'\nMelhor Indivíduo:\n {bestIndividual}')
            continue
        break

def printMenu() -> None:
    title: str = ' Problema das 8 Rainhas '
    action: str = ' Escolha um dos algoritmos para a resolução '

    print(f'\n{title:-^80}')
    print(f'{action:-^80}\n')
    print('1 - Algoritmo Genético')
    print('2 - Subida na Encosta')
    print('0 - Sair')

def inputListInt(message: str, options: list[int]) -> None:
    option = None
    while option not in options:
        option = input(message)
        if not option.isnumeric():
            continue
        option = int(option)
    return option

if __name__ == '__main__':
    main()

