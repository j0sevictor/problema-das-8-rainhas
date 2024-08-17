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
    TITLE: str = ' Problema das 8 Rainhas '
    ACTION: str = ' Escolha um dos algoritmos para a resolução '

    print(f'\n{TITLE:-^80}')
    print(f'{ACTION:-^80}\n')
    print('1 - Algoritmo Genético')
    print('2 - Subida na Encosta')
    print('0 - Sair')

def inputListInt(message: str, options: list[int]) -> int:
    """
    Retorna uma das opções especificadas da lista a partir do input do usuário.
    """
    while True:
        option: str = input(message)
        if not option.isnumeric() or int(option) not in options:
            continue
        break
    return int(option)

if __name__ == '__main__':
    main()
