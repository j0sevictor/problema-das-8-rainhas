
SIZE = 8

class Entity():
    __id: int = 0

    def __init__(self, vector: list[int], generation: int) -> None:
        if len(vector) != SIZE:
            raise ValueError(f'O vetor do indivíduo deve conter exatamente {SIZE} posições')

        self.__id: int = Entity.__id
        self.__generation: int = generation
        self.__vector: list[int] = vector
        Entity.__id += 1

    def getId(self) -> int:
        """
        Retorna o ID único do indivíduo.
        """
        return self.__id
    
    def getGeneration(self) -> int:
        """
        Retorna na geração em que o indivíduo foi criado.
        """
        return self.__generation

    def getVector(self) -> list[int]:
        """
        Retorna o vetor de valores do indivíduo.
        """
        return self.__vector
    
    def getVectorSize(self) -> int:
        """
        Retorna o tamanho do vetor.
        """
        return len(self.__vector)
    
    def get(self, index: int) -> int:
        """
        Retorna o valor da posição do vetor especificada pelo index.
        """
        if index < 0 or index >= SIZE:
            raise ValueError('Argumento index fora do limite do vetor')
        return self.__vector[index]

    def __eq__(self, __value: object) -> bool:
        """
        Compara se o vertor dos indivíduos são iguais.
        """
        if isinstance(__value, Entity) and __value.getVector() == self.getVector():
            return True
        return False

