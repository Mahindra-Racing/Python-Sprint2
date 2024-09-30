# Quiz e Simulação de Corrida da Fórmula E

## Descrição do Projeto
Este projeto consiste em dois programas em Python que oferecem uma experiência interativa relacionada à Fórmula E. O primeiro código apresenta um menu principal, que permite ao usuário escolher entre participar de um quiz, simular uma corrida, acessar o site oficial da Fórmula E ou sair do programa. O segundo código gerencia a simulação da corrida, onde o usuário interage tomando decisões durante a competição.

## Componentes do Projeto

### 1. Primeiro Código: Menu Principal e Quiz
#### Funcionalidades:
- **Menu Principal**: Oferece as opções de iniciar o quiz, simular uma corrida, acessar o site oficial ou sair.
- **Quiz**: Oferece perguntas sobre a Fórmula E, com modos solo ou competitivo (dois jogadores).
- **Navegação**: Permite retornar ao menu principal ou encerrar o programa após o quiz.
- **Integração**: O código chama o segundo programa (`corrida.py`) para simular a corrida.

#### Estrutura:
- **Funções Principais**:
  - `menu()`: Exibe o menu principal e captura a escolha do usuário.
  - `main()`: Controla o fluxo principal do programa com base nas escolhas do menu.
  - `quiz()`: Gerencia o modo de quiz solo.
  - `competitivo()`: Gerencia o modo de quiz competitivo para dois jogadores.
  - `menu_quiz()`: Submenu para selecionar entre os modos solo, competitivo ou voltar ao menu principal.
  - `fazer_pergunta()`: Apresenta cada pergunta e valida a resposta do usuário.

### 2. Segundo Código: Simulação de Corrida (corrida.py)
#### Funcionalidades:
- **Configuração da Corrida**: O usuário insere o nome do piloto e escolhe uma equipe.
- **Simulação Dinâmica**: A corrida ocorre em múltiplos rounds, onde o jogador faz escolhas que afetam a energia e posição.
- **Eventos Aleatórios**: Introduz sorte nos resultados, como ultrapassagens e reabastecimento.
- **Resultados**: Determina a posição final e oferece opções para jogar novamente, retornar ao menu ou sair.

#### Estrutura:
- **Funções Principais**:
  - `main()`: Inicia a corrida solicitando informações do jogador e inicializa a simulação.
  - `simular_corrida()`: Controla a lógica da corrida, incluindo escolhas e atualizações de energia e posição.
  - `obter_opcao()`: Valida a entrada do usuário durante a corrida.

## Diagrama em Blocos: Funcionamento do Projeto

```plaintext
     +--------------------+
     |    Início do       |
     |    Programa        |
     +---------+----------+
               |
               v
     +--------------------+
     |   Menu Principal   |
     |  [1] Iniciar Quiz   |
     |  [2] Simular Corrida|
     |  [3] Site Oficial   |
     |  [4] Sair           |
     +---------+----------+
               |
               +--------------------------+
               |                          |
               v                          v
      +----------------+        +-------------------------+
      |   Iniciar Quiz |        |   Simular Corrida       |
      |                |        |  (Chama corrida.py)     |
      +-------+--------+        +-----------+-------------+
              |                             |
              v                             v
      +----------------+         +-------------------------+
      |   Submenu Quiz |         |   Simulação da Corrida  |
      | [1] Solo       |         |  - Escolha de ações     |
      | [2] Competitivo |        |  - Atualização de energia|
      | [3] Voltar      |        |  - Determinação do resultado|
      +-------+--------+         +-----------+-------------+
              |                             |
              v                             v
     +----------------+         +-------------------------+
     |     Quiz       |         |      Resultado          |
     | - Apresenta    |         | - Exibe posição final   |
     |   perguntas    |         | - Opções: Jogar novamente|
     | - Calcula      |         |   ou voltar ao menu      |
     |   pontuação    |         +-------------------------+
     +-------+--------+
             |
             v
     +----------------+
     |  Exibir Resultado|
     |  e opções finais |
     +----------------+
             |
             v
     +----------------+
     |  Retornar ao   |
     |  Menu Principal|
     +----------------+
             |
             v
     +----------------+
     |     Sair       |
     +----------------+
