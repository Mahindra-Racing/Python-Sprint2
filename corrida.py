import random

# Dicionário com pilotos e peças, com custo e atributos para diferentes níveis de dificuldade
pilotos = {
    '1': {'nome': 'Piloto Iniciante', 'habilidade': 60, 'agressividade': 50, 'experiência': 55, 'custo': 0},
    '2': {'nome': 'Piloto Intermediário', 'habilidade': 75, 'agressividade': 70, 'experiência': 65, 'custo': 20000},
    '3': {'nome': 'Piloto Avançado', 'habilidade': 90, 'agressividade': 85, 'experiência': 80, 'custo': 50000}
}

pecas = {
    'lataria': {
        '1': {'nome': 'Lataria Básica', 'peso': 100, 'resistencia': 70, 'custo': 0},
        '2': {'nome': 'Lataria Intermediária', 'peso': 85, 'resistencia': 80, 'custo': 5000},
        '3': {'nome': 'Lataria Avançada', 'peso': 75, 'resistencia': 90, 'custo': 10000},
    },
    'motor': {
        '1': {'nome': 'Motor Básico', 'potencia': 60, 'eficiencia': 65, 'custo': 0},
        '2': {'nome': 'Motor Intermediário', 'potencia': 75, 'eficiencia': 80, 'custo': 10000},
        '3': {'nome': 'Motor Avançado', 'potencia': 90, 'eficiencia': 90, 'custo': 20000},
    },
    'bateria': {
        '1': {'nome': 'Bateria Básica', 'capacidade': 60, 'eficiencia': 65, 'custo': 0},
        '2': {'nome': 'Bateria Intermediária', 'capacidade': 75, 'eficiencia': 80, 'custo': 8000},
        '3': {'nome': 'Bateria Avançada', 'capacidade': 90, 'eficiencia': 90, 'custo': 15000},
    },
    'pneus': {
        '1': {'nome': 'Pneus Básicos', 'aderencia': 60, 'durabilidade': 65, 'custo': 0},
        '2': {'nome': 'Pneus Intermediários', 'aderencia': 75, 'durabilidade': 80, 'custo': 6000},
        '3': {'nome': 'Pneus Avançados', 'aderencia': 90, 'durabilidade': 90, 'custo': 12000},
    },
    'acessorios': {
        '1': {'nome': 'Acessórios Básicos', 'controle': 60, 'durabilidade': 65, 'custo': 0},
        '2': {'nome': 'Acessórios Intermediários', 'controle': 75, 'durabilidade': 80, 'custo': 7000},
        '3': {'nome': 'Acessórios Avançados', 'controle': 90, 'durabilidade': 90, 'custo': 12000},
    }
}

def obter_opcao(menu, categoria):
    while True:
        opcao = input(menu)
        if opcao in categoria:
            return opcao
        else:
            print("Opção inválida. Por favor, tente novamente.")

def montar_equipe(dinheiro):
    print("=== MONTAGEM DA EQUIPE ===")
    print(f"\nVocê tem R$ {dinheiro} para montar sua equipe.")

    print("\nEscolha seu piloto:")
    for key, value in pilotos.items():
        print(f"{key}: {value['nome']} - Habilidade: {value['habilidade']}, Custo: R$ {value['custo']}")
    piloto_escolhido = obter_opcao("Digite o número do piloto escolhido: ", pilotos)
    dinheiro -= pilotos[piloto_escolhido]['custo']
    dinheiro = max(dinheiro, 0)  # Garantir que o dinheiro não fique negativo
    print(f"Dinheiro restante: R$ {dinheiro}")

    print("\nEscolha suas peças:")

    print("\nLATARIA:")
    for key, value in pecas['lataria'].items():
        print(f"{key}: {value['nome']} - Peso: {value['peso']}, Resistência: {value['resistencia']}, Custo: R$ {value['custo']}")
    lataria_escolhida = obter_opcao("Digite o número da lataria escolhida: ", pecas['lataria'])
    dinheiro -= pecas['lataria'][lataria_escolhida]['custo']
    dinheiro = max(dinheiro, 0)  # Garantir que o dinheiro não fique negativo
    print(f"Dinheiro restante: R$ {dinheiro}")

    print("\nMOTOR:")
    for key, value in pecas['motor'].items():
        print(f"{key}: {value['nome']} - Potência: {value['potencia']}, Eficiência: {value['eficiencia']}, Custo: R$ {value['custo']}")
    motor_escolhido = obter_opcao("Digite o número do motor escolhido: ", pecas['motor'])
    dinheiro -= pecas['motor'][motor_escolhido]['custo']
    dinheiro = max(dinheiro, 0)  # Garantir que o dinheiro não fique negativo
    print(f"Dinheiro restante: R$ {dinheiro}")

    print("\nBATERIA:")
    for key, value in pecas['bateria'].items():
        print(f"{key}: {value['nome']} - Capacidade: {value['capacidade']}, Eficiência: {value['eficiencia']}, Custo: R$ {value['custo']}")
    bateria_escolhida = obter_opcao("Digite o número da bateria escolhida: ", pecas['bateria'])
    dinheiro -= pecas['bateria'][bateria_escolhida]['custo']
    dinheiro = max(dinheiro, 0)  # Garantir que o dinheiro não fique negativo
    print(f"Dinheiro restante: R$ {dinheiro}")

    print("\nPNEUS:")
    for key, value in pecas['pneus'].items():
        print(f"{key}: {value['nome']} - Aderência: {value['aderencia']}, Durabilidade: {value['durabilidade']}, Custo: R$ {value['custo']}")
    pneus_escolhidos = obter_opcao("Digite o número dos pneus escolhidos: ", pecas['pneus'])
    dinheiro -= pecas['pneus'][pneus_escolhidos]['custo']
    dinheiro = max(dinheiro, 0)  # Garantir que o dinheiro não fique negativo
    print(f"Dinheiro restante: R$ {dinheiro}")

    print("\nACESSÓRIOS:")
    for key, value in pecas['acessorios'].items():
        print(f"{key}: {value['nome']} - Controle: {value['controle']}, Durabilidade: {value['durabilidade']}, Custo: R$ {value['custo']}")
    acessorio_escolhido = obter_opcao("Digite o número do acessório escolhido: ", pecas['acessorios'])
    dinheiro -= pecas['acessorios'][acessorio_escolhido]['custo']
    dinheiro = max(dinheiro, 0)  # Garantir que o dinheiro não fique negativo
    print(f"Dinheiro restante: R$ {dinheiro}")

    if dinheiro < 0:
        print("\nVocê excedeu seu orçamento! Tente novamente.")
        return montar_equipe(dinheiro)

    return piloto_escolhido, lataria_escolhida, motor_escolhido, bateria_escolhida, pneus_escolhidos, acessorio_escolhido, dinheiro

def melhorar_carro(dinheiro, lataria, motor, bateria, pneus, acessorio):
    while True:
        print("\n=== MELHORIA DO CARRO ===")
        print(f"Você tem R$ {dinheiro} para melhorar seu carro.")

        print("\nEscolha a peça para melhorar:")
        print("1: Lataria")
        print("2: Motor")
        print("3: Bateria")
        print("4: Pneus")
        print("5: Acessórios")
        escolha = obter_opcao("Digite o número da peça escolhida: ", ['1', '2', '3', '4', '5'])

        if escolha == '1':
            print("\nLATARIA:")
            for key, value in pecas['lataria'].items():
                if key != lataria:
                    print(f"{key}: {value['nome']} - Peso: {value['peso']}, Resistência: {value['resistencia']}, Custo: R$ {value['custo']}")
            nova_lataria = obter_opcao("Digite o número da nova lataria: ", pecas['lataria'])
            custo = pecas['lataria'][nova_lataria]['custo']
            if custo <= dinheiro:
                lataria = nova_lataria
                dinheiro -= custo
                print(f"Lataria atualizada para {pecas['lataria'][lataria]['nome']}. Dinheiro restante: R$ {dinheiro}")
            else:
                print("Dinheiro insuficiente para essa melhoria.")

        elif escolha == '2':
            print("\nMOTOR:")
            for key, value in pecas['motor'].items():
                if key != motor:
                    print(f"{key}: {value['nome']} - Potência: {value['potencia']}, Eficiência: {value['eficiencia']}, Custo: R$ {value['custo']}")
            novo_motor = obter_opcao("Digite o número do novo motor: ", pecas['motor'])
            custo = pecas['motor'][novo_motor]['custo']
            if custo <= dinheiro:
                motor = novo_motor
                dinheiro -= custo
                print(f"Motor atualizado para {pecas['motor'][motor]['nome']}. Dinheiro restante: R$ {dinheiro}")
            else:
                print("Dinheiro insuficiente para essa melhoria.")

        elif escolha == '3':
            print("\nBATERIA:")
            for key, value in pecas['bateria'].items():
                if key != bateria:
                    print(f"{key}: {value['nome']} - Capacidade: {value['capacidade']}, Eficiência: {value['eficiencia']}, Custo: R$ {value['custo']}")
            nova_bateria = obter_opcao("Digite o número da nova bateria: ", pecas['bateria'])
            custo = pecas['bateria'][nova_bateria]['custo']
            if custo <= dinheiro:
                bateria = nova_bateria
                dinheiro -= custo
                print(f"Bateria atualizada para {pecas['bateria'][bateria]['nome']}. Dinheiro restante: R$ {dinheiro}")
            else:
                print("Dinheiro insuficiente para essa melhoria.")

        elif escolha == '4':
            print("\nPNEUS:")
            for key, value in pecas['pneus'].items():
                if key != pneus:
                    print(f"{key}: {value['nome']} - Aderência: {value['aderencia']}, Durabilidade: {value['durabilidade']}, Custo: R$ {value['custo']}")
            novos_pneus = obter_opcao("Digite o número dos novos pneus: ", pecas['pneus'])
            custo = pecas['pneus'][novos_pneus]['custo']
            if custo <= dinheiro:
                pneus = novos_pneus
                dinheiro -= custo
                print(f"Pneus atualizados para {pecas['pneus'][pneus]['nome']}. Dinheiro restante: R$ {dinheiro}")
            else:
                print("Dinheiro insuficiente para essa melhoria.")

        elif escolha == '5':
            print("\nACESSÓRIOS:")
            for key, value in pecas['acessorios'].items():
                if key != acessorio:
                    print(f"{key}: {value['nome']} - Controle: {value['controle']}, Durabilidade: {value['durabilidade']}, Custo: R$ {value['custo']}")
            novo_acessorio = obter_opcao("Digite o número do novo acessório: ", pecas['acessorios'])
            custo = pecas['acessorios'][novo_acessorio]['custo']
            if custo <= dinheiro:
                acessorio = novo_acessorio
                dinheiro -= custo
                print(f"Acessório atualizado para {pecas['acessorios'][acessorio]['nome']}. Dinheiro restante: R$ {dinheiro}")
            else:
                print("Dinheiro insuficiente para essa melhoria.")

        if dinheiro < 0:
            dinheiro = 0

        continuar = obter_opcao("Deseja melhorar outra peça? (s/n): ", ['s', 'n'])
        if continuar == 'n':
            break

    return lataria, motor, bateria, pneus, acessorio, dinheiro

def simular_corrida(dificuldade, piloto, lataria, motor, bateria, pneus, acessorio):
    energia = 100
    posicao = 5
    recompensa = {'fácil': 10000, 'mediana': 20000, 'difícil': 30000}
    chance_perda = {'fácil': 10, 'mediana': 20, 'difícil': 30}

    while energia > 0 and posicao > 0:
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
                if random.randint(1, 100) <= chance_perda[dificuldade]:
                    posicao += 2
                    print("Você perdeu 2 posições!")

        if energia <= 0:
            print("Você ficou sem energia! A corrida terminou.")
            return 0  # Nenhuma recompensa

    print(f"\nVocê terminou na {posicao}º posição!")
    if posicao == 1:
        print(f"Parabéns! Você venceu a corrida e ganhou R$ {recompensa[dificuldade]}.")
        return recompensa[dificuldade]
    else:
        print(f"Você não venceu a corrida. Sem recompensa.")
        return 0

def main():
    dinheiro = 0
    vitórias = {'fácil': 0, 'mediana': 0, 'difícil': 0}

    print("=== BEM-VINDO AO JOGO DE FÓRMULA E ===")

    piloto_escolhido, lataria_escolhida, motor_escolhido, bateria_escolhida, pneus_escolhidos, acessorio_escolhido, dinheiro = montar_equipe(dinheiro)

    # Corrida 1 - Fácil
    while True:
        print("\nIniciando Corrida Fácil...")
        recompensa = simular_corrida('fácil', piloto_escolhido, lataria_escolhida, motor_escolhido, bateria_escolhida, pneus_escolhidos, acessorio_escolhido)
        if recompensa > 0:
            dinheiro += recompensa
            vitórias['fácil'] += 1
            lataria_escolhida, motor_escolhido, bateria_escolhida, pneus_escolhidos, acessorio_escolhido, dinheiro = melhorar_carro(dinheiro, lataria_escolhida, motor_escolhido, bateria_escolhida, pneus_escolhidos, acessorio_escolhido)
            break
        print("Você perdeu a corrida. Tente novamente.")

    print(f"\nVocê agora tem R$ {dinheiro}.")

    # Corrida 2 - Mediana
    while True:
        print("\nIniciando Corrida Mediana...")
        recompensa = simular_corrida('mediana', piloto_escolhido, lataria_escolhida, motor_escolhido, bateria_escolhida, pneus_escolhidos, acessorio_escolhido)
        if recompensa > 0:
            dinheiro += recompensa
            vitórias['mediana'] += 1
            lataria_escolhida, motor_escolhido, bateria_escolhida, pneus_escolhidos, acessorio_escolhido, dinheiro = melhorar_carro(dinheiro, lataria_escolhida, motor_escolhido, bateria_escolhida, pneus_escolhidos, acessorio_escolhido)
            break
        print("Você perdeu a corrida. Tente novamente.")

    print(f"\nVocê agora tem R$ {dinheiro}.")

    # Corrida 3 - Difícil
    while True:
        print("\nIniciando Corrida Difícil...")
        recompensa = simular_corrida('difícil', piloto_escolhido, lataria_escolhida, motor_escolhido, bateria_escolhida, pneus_escolhidos, acessorio_escolhido)
        if recompensa > 0:
            dinheiro += recompensa
            vitórias['difícil'] += 1
            lataria_escolhida, motor_escolhido, bateria_escolhida, pneus_escolhidos, acessorio_escolhido, dinheiro = melhorar_carro(dinheiro, lataria_escolhida, motor_escolhido, bateria_escolhida, pneus_escolhidos, acessorio_escolhido)
            break
        print("Você perdeu a corrida. Tente novamente.")

    print(f"\nVocê terminou o jogo com R$ {dinheiro}.")
    print(f"Vitórias: Fácil: {vitórias['fácil']}, Mediana: {vitórias['mediana']}, Difícil: {vitórias['difícil']}")

if __name__ == "__main__":
    main()
