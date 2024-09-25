import random

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

    while True:
        print(f"\nEnergia: {energia}, Posição: {posicao}")
        print("Escolha sua ação:")
        print("1: Tentar ultrapassagem (gasta energia)")
        print("2: Manter posição (gasta pouca energia)")
        print("3: Forçar uma ultrapassagem (gasta muita energia, chance maior de perder posições)")

        escolha = obter_opcao("Digite o número da ação escolhida: ", ['1', '2', '3'])

        if escolha == '1':
            energia -= random.randint(10, 20)
            if random.randint(1, 100) <= 50:
                posicao -= 1
                print("Você ultrapassou um adversário!")
            else:
                print("A tentativa de ultrapassagem não foi bem-sucedida.")

        elif escolha == '2':
            energia -= random.randint(5, 10)
            if random.randint(1, 100) <= 30:
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

        # Verifica se o jogador ficou sem energia
        if energia <= 0:
            energia = 0
            posicao += 1  # O jogador perde uma posição para "descarregar"
            print("Você ficou sem energia e perdeu uma posição para descarregar.")
            print(f"Você agora está na posição: {posicao}")
            continue

        # Verifica se o jogador chegou em primeiro
        if posicao == 1:
            print(f"\nParabéns, {piloto_nome}, da {equipe_nome}! Você venceu a corrida!")
            return

def main():
    print("=== BEM-VINDO AO JOGO DE FÓRMULA E ===")
    piloto_nome = input("Digite o seu nome: ")

    print("\nEscolha sua equipe:")
    for key, value in equipes.items():
        print(f"{key}: {value['nome']}")
    equipe_escolhida = obter_opcao("Digite o número da equipe escolhida: ", equipes)

    # Iniciando a corrida
    print("\nIniciando a Corrida...")
    simular_corrida(piloto_nome, equipes[equipe_escolhida]['nome'])

if __name__ == "__main__":
    main()
