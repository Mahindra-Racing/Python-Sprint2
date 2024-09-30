import random
import sys

# Dicionário com as equipes
equipes = {
    '1': {'nome': 'Equipe 1'},
    '2': {'nome': 'Equipe 2'},
    '3': {'nome': 'Equipe 3'}
}

def obter_opcao(menu, categoria):
    while True:
        opcao = input(menu)
        if opcao in categoria:
            return opcao
        else:
            print("Opção inválida. Por favor, tente novamente.")

def simular_corrida(piloto_nome, equipe_nome):
    energia = 100
    posicao = 5
    rounds = random.randint(10, 15)  # Define um número aleatório de rounds entre 10 e 15

    print(f"\nA corrida terá {rounds} rounds.\n")

    for round_atual in range(1, rounds + 1):
        print(f"\n=== Round {round_atual} ===")

        # Mensagem avisando que a corrida está quase acabando, um round antes do final
        if round_atual == rounds - 1:
            print("A corrida está quase acabando! Prepare-se para a última volta.")

        print(f" Energia: {energia}, Posição: {posicao}")
        print("Escolha sua ação:")
        print("1: Tentar ultrapassagem (gasta energia)")
        print("2: Manter posição (gasta pouca energia)")
        print("3: Forçar uma ultrapassagem (gasta muita energia, chance maior de perder posições)")
        print("4: Abandonar a corrida (fechar o aplicativo)")

        escolha = obter_opcao("Digite o número da ação escolhida: ", ['1', '2', '3', '4'])

        if escolha == '1':
            energia -= random.randint(10, 20)
            if random.randint(1, 100) <= 50:
                posicao -= 1
                print("Você ultrapassou um adversário!")
            else:
                print("A tentativa de ultrapassagem não foi bem-sucedida.")

        elif escolha == '2':
            energia -= random.randint(5, 10)
            print("Você manteve sua posição.")

        elif escolha == '3':
            energia -= random.randint(20, 30)
            if random.randint(1, 100) <= 40:
                posicao -= 2
                print("Você avançou 2 posições!")
            else:
                print("Forçou a ultrapassagem sem sucesso.")
                if random.randint(1, 100) <= 20:
                    posicao += 1
                    print("Você perdeu 1 posição!")

        elif escolha == '4':
            print('\nSaindo do programa. Até mais!')
            sys.exit(1)  # Encerra com código de saída 1

        # Verifica se o jogador ficou sem energia
        if energia <= 0:
            energia = 0
            perda_posicoes = random.randint(0, 2)  # Perde de 0 a 2 posições
            posicao += perda_posicoes
            print(f"Você ficou sem energia e perdeu {perda_posicoes} posições para reabastecer.")
            print("Seu carro foi abastecido!")  # Mensagem de abastecimento
            energia = 100  # Reabastecendo a energia
            print(f"Você agora está na posição: {posicao}")
            continue

        # Assegurando que a posição está entre 1 e 20
        posicao = max(1, min(posicao, 20))

    # Fim da corrida - mensagem de resultado
    if posicao == 1:
        print(f"\nParabéns, {piloto_nome}, da {equipe_nome}! Você venceu a corrida!")
    else:
        print(f"\nA corrida acabou! Você perdeu a corrida e terminou na posição {posicao}.")

    # Opção de jogar novamente ou voltar ao menu
    while True:
        voltar_menu = input('1: Jogar novamente\n2: Voltar ao menu\n Escolha: ').strip().lower()
        if voltar_menu == '1':
            main()
        elif voltar_menu == '2':
            sys.exit(0)  # Encerrar com código de saída 0 para voltar ao menu
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

def main():
    print("=== BEM-VINDO AO JOGO DE FÓRMULA E ===")
    piloto_nome = input("Digite o seu nome: ").strip()

    if not piloto_nome:
        print("O nome do piloto não pode estar vazio.")
        return main()

    print("\nEscolha sua equipe:")
    for key, value in equipes.items():
        print(f"{key}: {value['nome']}")
    equipe_escolhida = obter_opcao("Digite o número da equipe escolhida: ", equipes.keys())

    # Iniciando a corrida
    print("\nIniciando a Corrida...")
    simular_corrida(piloto_nome, equipes[equipe_escolhida]['nome'])

if __name__ == "__main__":
    main()