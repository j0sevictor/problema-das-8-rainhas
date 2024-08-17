from algorithms import GeneticAlgorithm, HillClimbing, Algorithm

def main() -> None:
    """
    Função principal.
    """
    while True:
        printMenu()
        option = inputListInt('-> ', [1, 2, 0])
        if not option:
            break

        algorithms: dict[int, Algorithm] = {
            1: GeneticAlgorithm(),
            2: HillClimbing(toOptimal=True)
        }

        bestIndividual = algorithms[option].run()
        print(f'\nMelhor Indivíduo:\n {bestIndividual}')

def printMenu() -> None:
    """
    Imprime o menu do programa.
    """
    title: str = ' Problema das 8 Rainhas '
    action: str = ' Escolha um dos algoritmos para a resolução '

    print(f'\n{title:-^80}')
    print(f'{action:-^80}\n')
    print('1 - Algoritmo Genético')
    print('2 - Subida na Encosta')
    print('0 - Sair')

def inputListInt(message: str, options: list[int]) -> None:
    """
    Retorna uma das opções especificadas da lista a partir do input do usuário.
    """
    option = None
    while option not in options:
        option = input(message)
        if not option.isnumeric():
            continue
        option = int(option)
    return option

if __name__ == '__main__':
    main()
