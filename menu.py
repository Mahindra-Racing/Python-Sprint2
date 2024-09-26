import random
import subprocess
import webbrowser


def menu():
    print('''
Menu
    [1] - Iniciar Quiz
    [2] - Simular Corrida
    [3] - Site
    [4] - Sair
    ''')
    escolha = input('Escolha uma opção: ')
    return escolha



def main():
    escolha = menu()

    if escolha == "1":
        print('Você escolheu a opção 1.')
        menu_quiz()
    elif escolha == "2":
        print('Você escolheu a opção 2.')
        subprocess.run(["python", "corrida.py"])
    elif escolha == "3":
        print('Você escolheu a opção 3.')
        url = 'https://www.pornhub.com'
        webbrowser.open(url)
        main()
    elif escolha =="4":
        exit()
    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')
        main()




# Dicionário com perguntas e respostas
quiz_data = {
    "Qual é a principal característica que diferencia a Fórmula E de outras categorias de automobilismo?": {
        "a": "Uso de combustíveis fósseis",
        "b": "Veículos com motor a combustão interna",
        "c": "Carros totalmente elétricos",
        "d": "Corridas em pistas de terra",
        "e": "Veículos com pneus de trilha",
        "resposta": "c"
    },
    "Qual cidade sediou a primeira corrida da Fórmula E?": {
        "a": "Paris",
        "b": "Londres",
        "c": "Beijing",
        "d": "Nova York",
        "e": "São Paulo",
        "resposta": "c"
    },
    "Qual é o nome do campeonato de pilotos da Fórmula E?": {
        "a": "Campeonato de Pilotos da Fórmula E",
        "b": "Campeonato Mundial de Fórmula E",
        "c": "Campeonato de Corridas Elétricas",
        "d": "Campeonato de Fórmula Elétrica",
        "e": "Campeonato Global de E-Pilotos",
        "resposta": "b"
    },
    "Qual é o nome do troféu concedido ao vencedor do campeonato de equipes na Fórmula E?": {
        "a": "Troféu de Campeão de Equipes",
        "b": "Troféu de Equipe do Ano",
        "c": "Troféu de Campeão Mundial de Equipes",
        "d": "Troféu de Equipe de Fórmula E",
        "e": "Troféu de Equipe Campeã",
        "resposta": "c"
    },
    "Em qual ano foi criada a Fórmula E?": {
        "a": "2010",
        "b": "2012",
        "c": "2014",
        "d": "2016",
        "e": "2018",
        "resposta": "c"
    }
}

contador = 0

def fazer_pergunta(pergunta, opcoes, resposta_certa):
    global contador
    contador += 1
    print(f'---------------------\n{contador} - {pergunta}')

    for chave, valor in opcoes.items():
        print(f"{chave}: {valor}")

    while True:
        resposta = input("Escolha a resposta: ").strip().lower()
        if resposta in opcoes:
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida (a/b/c/d/e).")

    if resposta == resposta_certa:
        print("Correto!")
        return True
    else:
        respostaUpper = resposta_certa.strip().upper()
        print(f"- Incorreto! - A resposta correta era {respostaUpper} {opcoes[resposta_certa]}")
        return False


def quiz():
    perguntas = list(quiz_data.keys())
    random.shuffle(perguntas)  # Randomiza a ordem das perguntas

    pontuacao = 0
    total_perguntas = len(perguntas)

    for pergunta in perguntas:
        dados = quiz_data[pergunta]
        opcoes = {chave: valor for chave, valor in dados.items() if chave != "resposta"}
        resposta_certa = dados["resposta"]

        if fazer_pergunta(pergunta, opcoes, resposta_certa):
            pontuacao += 1

    print(f"\nSeu resultado: {pontuacao}/{total_perguntas}")
    while True:
        asas = input('1: Voltar ao menu\n2: Sair\n: ')
        if asas == "1":
            main()
            break
        elif asas == "2":
            exit()
        else:
            print('Escolha uma opção válida.')


def competitivo():
    print("Modo Competitivo - Dois jogadores")
    jogador1 = input('Jogador 1: ')
    jogador2 = input('Jogador 2: ')
    jogadores = [jogador1, jogador2]
    pontuacao_jogador_1 = 0
    pontuacao_jogador_2 = 0

    perguntas = list(quiz_data.keys())
    random.shuffle(perguntas)

    total_perguntas = len(perguntas)


    print(f"\nTurno do {jogador1} ")
    for pergunta in perguntas:
        dados = quiz_data[pergunta]
        opcoes = {chave: valor for chave, valor in dados.items() if chave != "resposta"}
        resposta_certa = dados["resposta"]

        if fazer_pergunta(pergunta, opcoes, resposta_certa):
            pontuacao_jogador_1 += 1

    print(f"\nTurno do {jogador2} ")
    for pergunta in perguntas:
        dados = quiz_data[pergunta]
        opcoes = {chave: valor for chave, valor in dados.items() if chave != "resposta"}
        resposta_certa = dados["resposta"]

        if fazer_pergunta(pergunta, opcoes, resposta_certa):
            pontuacao_jogador_2 += 1

    print(f"\nResultado Final:")
    print(f"{jogador1}: {pontuacao_jogador_1}/{total_perguntas}")
    print(f"{jogador2}: {pontuacao_jogador_2}/{total_perguntas}")

    if pontuacao_jogador_1 > pontuacao_jogador_2:
        print(f"O vencedor é o {jogador1}!")
    elif pontuacao_jogador_2 > pontuacao_jogador_1:
        print(f"O vencedor é o {jogador2}!")
    else:
        print("Empate!")

    while True:
        asas = input('1: Voltar ao menu\n2: Sair\n: ')
        if asas == "1":
            main()
            break
        elif asas == "2":
            exit()
        else:
            print('Escolha uma opção válida.')


def menu_quiz():
    print('''
    Modo de jogo
        [1] - Solo  (descrição)
        [2] - Competitivo   (descrição)
        [3] - Voltar para o Menu
    ''')
    while True:
        escolha = input('Escolha uma opção: ')

        if escolha == "1":
            print('Você escolheu jogar no modo Solo.')
            quiz()
            break
        elif escolha == "2":
            print('Você escolheu jogar no modo Competitivo.')
            competitivo()
            break
        elif escolha == "3":
            main()
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')

if __name__ == "__main__":
    main()
