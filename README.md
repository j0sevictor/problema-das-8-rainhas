# Resolvendo o Problema das 8 Rainhas

## Introdução

O Problema das 8 Rainhas é um clássico desafio na área de computação e inteligência artificial. O objetivo é posicionar oito rainhas em um tabuleiro de xadrez convencional 8x8 de tal forma que nenhuma rainha possa atacar outra. Ou seja, nenhuma rainha deve compartilhar a mesma linha, coluna ou diagonal. Uma das abordagens para solucionar este problema é por meio de algoritmos genéticos, outra é utiliza o algorítmo de subida na colina (hill climbing).

## Algoritmo Genético

Os algoritmos genéticos usam técnicas de otimização inspiradas na evolução biológica. Eles operam em uma população de soluções candidatas e utilizam operadores genéticos como seleção, recombinação e mutação para gerar soluções melhores ao longo de várias gerações.

## Subida na Colina

O algorítmo de subida na colina se baseia em um princípio básico, a partir de uma solução candidata, análisa-se sua vizinhança, se um vizinho é melhor, troca-se a solução candidata por esse novo indivíduo. Repete-se esse processo até que não haja melhorias. O algoritmo só garante encontrar o máximo/mínimo local, mas, o aplicando várias vezes, é possível encontrar a solução ótima. 

# Sobre este Repositório

Neste repositório, apresento uma implementação de ambos os algoritmos descritos, a fim de resolver o Problema das 8 Rainhas. O código está escrito em Python e uma explicação mas detalhada segue abaixo.

## Funcionamento

**Representação dos Indivíduos**: Para os algoritmos, cada solução candidata, chamadas de indivíduos, foram representadas como um vetor unidimencional de 8 posições, cada posição representa uma coluna do tabuleiro, o valor, a linha no qual se encontra a rainha daquela coluna. Por exemplo o vertor [1, 4, 6, 2, 8, 7, 5, 3] representa o seguinte cenário:

<p align="center">
  <img src="https://github.com/j0sevictor/problema-das-8-rainhas/assets/56090571/31c32fc5-e587-4654-891d-d4c765bb4a30">
</p>

**Avaliação Fitness**: Gera um valor numérico, para todo indivíduo, sobre a qualidade da solução em termos de quantos pares de rainhas não se atacam. Dessa forma para encontrar a solução tem-se que maximizar essa medida.

### Algoritmo Genético Guloso

**Inicialização da População**: Começamos com uma população inicial de indivíduos gerados aleatóriamente. Cada solução representa um arranjo possível das 8 rainhas no tabuleiro.

**Seleção**: Selecionamos os indivíduos para a próxima geração com base em sua avaliação. Soluções com alto *fitness* têm maior probabilidade de serem selecionadas.

**Recombinação**: As soluções selecionadas são cruzadas (*crossover*) para produzir descendentes. Isso é feito combinando partes das soluções parentais.

**Mutação**: Após a geração dos descendentes por recombinação, existe uma pequena taxa de mutação para manter diversidade na população. Isso ajuda a evitar a convergência prematura para uma solução não ótima.

**Critério de Parada**: Repetimos os processos anteriores até que uma solução ótima seja encontrada ou até que um número máximo de gerações seja atingido, caso em que é retornado o melhor indivíduo encontrado até aquele momento.

### Subida na Colina

**Inicialização da Solução Candidata**: Começamos com um indivíduo inicial gerado aleatóriamente.

**Seleção do Melhor Vizinho**: Seleciona o melhor vizinho da solução candidata. Os vizinhos são todos os tabuleiros que podem ser gerados pela movimentação de uma das 8 rainhas.

**Critério de Parada**: Repetimos o processo de seleção enquanto hover melhora na avaliação do vizinho selecionado.

**Reexecução**: Caso o melhor indivíduo encontrado não seja a solução ótima, executamos o algorítmo do início novamente.

# Execução

Para executar o projeto e resolver o Problema das 8 Rainhas, siga as instruções.

## Pré-requisito

Certifique-se de ter Python 3 instalado no seu sistema. Você pode baixá-lo em <a href="https://www.python.org/downloads/" target="_blank">python.org</a>.

## Instalação

1. Clone o repositório para a sua máquina:

   ```bash
   git clone https://github.com/j0sevictor/problema-das-8-rainhas.git
   ```
2. Navegue até o diretório do projeto:

   ```bash
   cd ...\problema-das-8-rainhas
   ```

## Executando o Projeto

Para executar o projeto, execute o seguinte comando:

- No Windows:
  ```bash
  python src\main.py
  ```
- No Unix ou MacOS:
  ```bash
  python src/main.py
  ```
