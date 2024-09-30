import random
import subprocess
import webbrowser
import sys

def menu():
    print('''
Menu
    [1] - Iniciar Quiz
    [2] - Simular Corrida
    [3] - Site Oficial da Fórmula E
    [4] - Sair
    ''')
    escolha = input('Escolha uma opção: ')
    return escolha

def main():
    while True:
        escolha = menu()

        if escolha == "1":
            print('\nVocê escolheu a opção 1: Iniciar Quiz.\n')
            menu_quiz()
        elif escolha == "2":
            print('\nVocê escolheu a opção 2: Simular Corrida.\n')
            # Executa corrida.py e captura o código de saída
            result = subprocess.run(["python", "corrida.py"])
            if result.returncode == 1:
                print('\nSaindo do programa. Até mais!')
                sys.exit()
        elif escolha == "3":
            print('\nVocê escolheu a opção 3: Acessar Site Oficial da Fórmula E.\n')
            url = 'https://synthica.netlify.app/'
            webbrowser.open(url)
        elif escolha == "4":
            print('\nSaindo do programa. Até mais!')
            sys.exit()
        else:
            print('\nOpção inválida. Por favor, escolha uma opção válida.\n')

# Dicionário com perguntas e respostas
quiz_data = {
    "perguntas": [
        "Qual é a principal característica que diferencia a Fórmula E de outras categorias de automobilismo?",
        "Qual cidade sediou a primeira corrida da Fórmula E?",
        "Qual é o nome do campeonato de pilotos da Fórmula E?",
        "Qual é o nome do troféu concedido ao vencedor do campeonato de equipes na Fórmula E?",
        "Em qual ano foi criada a Fórmula E?",
        "Qual é a duração típica de uma corrida da Fórmula E?",
        "Qual piloto detém o maior número de vitórias na Fórmula E até 2024?",
        "Qual equipe foi a campeã da temporada inaugural da Fórmula E?",
        "Qual é o nome da bateria utilizada nos carros da Fórmula E?",
        "Qual inovação tecnológica é frequentemente testada na Fórmula E para promover a sustentabilidade?"
    ],
    "opcoes": [
        {
            "a": "Uso de combustíveis fósseis",
            "b": "Veículos com motor a combustão interna",
            "c": "Carros totalmente elétricos",
            "d": "Corridas em pistas de terra",
            "e": "Veículos com pneus de trilha"
        },
        {
            "a": "Paris",
            "b": "Londres",
            "c": "Beijing",
            "d": "Nova York",
            "e": "São Paulo"
        },
        {
            "a": "Campeonato de Pilotos da Fórmula E",
            "b": "Campeonato Mundial de Fórmula E",
            "c": "Campeonato de Corridas Elétricas",
            "d": "Campeonato de Fórmula Elétrica",
            "e": "Campeonato Global de E-Pilotos"
        },
        {
            "a": "Troféu de Campeão de Equipes",
            "b": "Troféu de Equipe do Ano",
            "c": "Troféu de Campeão Mundial de Equipes",
            "d": "Troféu de Equipe de Fórmula E",
            "e": "Troféu de Equipe Campeã"
        },
        {
            "a": "2010",
            "b": "2012",
            "c": "2014",
            "d": "2016",
            "e": "2018"
        },
        {
            "a": "30 minutos",
            "b": "45 minutos",
            "c": "60 minutos",
            "d": "90 minutos",
            "e": "120 minutos"
        },
        {
            "a": "Lucas di Grassi",
            "b": "Sébastien Buemi",
            "c": "Jean-Éric Vergne",
            "d": "António Félix da Costa",
            "e": "Mitch Evans"
        },
        {
            "a": "DS Techeetah",
            "b": "e.dams Renault",
            "c": "Audi Sport ABT",
            "d": "BMW i Andretti",
            "e": "Jaguar Racing"
        },
        {
            "a": "Íon de lítio",
            "b": "NMC",
            "c": "LFP",
            "d": "Solid-state",
            "e": "Potássio"
        },
        {
            "a": "Painéis solares nos carros",
            "b": "Biocombustíveis",
            "c": "Tecnologias de recuperação de energia",
            "d": "Pneus biodegradáveis",
            "e": "Carros autônomos"
        }
    ],
    "respostas": [
        "c",
        "c",
        "b",
        "c",
        "c",
        "c",
        "c",
        "b",
        "a",
        "c"
    ]
}

def fazer_pergunta(numero, pergunta, opcoes, resposta_certa):
    print(f'---------------------\nPergunta {numero}: {pergunta}')

    for chave, valor in opcoes.items():
        print(f"  {chave}) {valor}")

    while True:
        resposta = input("Sua resposta (a/b/c/d/e): ").strip().lower()
        if resposta in opcoes:
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida (a/b/c/d/e).")

    if resposta == resposta_certa:
        print("✅ Correto!\n")
        return True
    else:
        resposta_upper = resposta_certa.upper()
        resposta_texto = opcoes[resposta_certa]
        print(f"❌ Incorreto! A resposta correta era {resposta_upper}) {resposta_texto}\n")
        return False

def quiz():
    perguntas = quiz_data["perguntas"]
    opcoes = quiz_data["opcoes"]
    respostas = quiz_data["respostas"]

    indices = list(range(len(perguntas)))
    random.shuffle(indices)  # Randomiza a ordem das perguntas

    pontuacao = 0
    total_perguntas = len(perguntas)

    for idx, i in enumerate(indices, 1):
        pergunta = perguntas[i]
        opcoes_pergunta = opcoes[i]
        resposta_certa = respostas[i]

        if fazer_pergunta(idx, pergunta, opcoes_pergunta, resposta_certa):
            pontuacao += 1

    print(f"🎉 Seu resultado: {pontuacao}/{total_perguntas}")

    while True:
        escolha = input('Escolha uma opção:\n  [1] Voltar ao menu\n  [2] Sair\nSua escolha: ').strip()
        if escolha == "1":
            print()
            return  # Retorna ao loop principal
        elif escolha == "2":
            print('\nSaindo do programa. Até mais!')
            sys.exit()
        else:
            print('Opção inválida. Por favor, escolha uma opção válida (1/2).\n')

def competitivo():
    print("\n🏁 Modo Competitivo - Dois Jogadores 🏁")
    jogador1 = input('Nome do Jogador 1: ').strip()
    jogador2 = input('Nome do Jogador 2: ').strip()

    if not jogador1 or not jogador2:
        print("Os nomes dos jogadores não podem estar vazios.")
        return competitivo()

    perguntas = quiz_data["perguntas"]
    opcoes = quiz_data["opcoes"]
    respostas = quiz_data["respostas"]

    indices = list(range(len(perguntas)))
    random.shuffle(indices)  # Randomiza a ordem das perguntas

    total_perguntas = len(perguntas)
    pontuacao_jogador_1 = 0
    pontuacao_jogador_2 = 0

    print(f"\n🔹 Turno do {jogador1} 🔹")
    for idx, i in enumerate(indices, 1):
        pergunta = perguntas[i]
        opcoes_pergunta = opcoes[i]
        resposta_certa = respostas[i]

        if fazer_pergunta(idx, pergunta, opcoes_pergunta, resposta_certa):
            pontuacao_jogador_1 += 1

    print(f"\n🔹 Turno do {jogador2} 🔹")
    for idx, i in enumerate(indices, 1):
        pergunta = perguntas[i]
        opcoes_pergunta = opcoes[i]
        resposta_certa = respostas[i]

        if fazer_pergunta(idx, pergunta, opcoes_pergunta, resposta_certa):
            pontuacao_jogador_2 += 1

    print("\n🏆 Resultado Final 🏆")
    print(f"{jogador1}: {pontuacao_jogador_1}/{total_perguntas}")
    print(f"{jogador2}: {pontuacao_jogador_2}/{total_perguntas}")

    if pontuacao_jogador_1 > pontuacao_jogador_2:
        print(f"🎉 O vencedor é {jogador1}! 🎉\n")
    elif pontuacao_jogador_2 > pontuacao_jogador_1:
        print(f"🎉 O vencedor é {jogador2}! 🎉\n")
    else:
        print("🤝 Empate! 🤝\n")

    while True:
        escolha = input('Escolha uma opção:\n  [1] Voltar ao menu\n  [2] Sair\nSua escolha: ').strip()
        if escolha == "1":
            print()
            return  # Retorna ao loop principal
        elif escolha == "2":
            print('\nSaindo do programa. Até mais!')
            sys.exit()
        else:
            print('Opção inválida. Por favor, escolha uma opção válida (1/2).\n')

def menu_quiz():
    print('''
Modo de Jogo
    [1] - Solo
    [2] - Competitivo
    [3] - Voltar para o Menu
    ''')
    while True:
        escolha = input('Escolha uma opção: ').strip()

        if escolha == "1":
            print('\nVocê escolheu jogar no modo Solo.\n')
            quiz()
            break
        elif escolha == "2":
            print('\nVocê escolheu jogar no modo Competitivo.\n')
            competitivo()
            break
        elif escolha == "3":
            print()
            return  # Retorna ao loop principal
        else:
            print('Opção inválida. Por favor, escolha uma opção válida (1/2/3).\n')

if __name__ == "__main__":
    main()
