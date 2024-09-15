import random


def menu():
    print('''
Menu
    [1] - Iniciar Quiz
    [2] - Opção 2''
    [3] - Opção 3
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
    elif escolha == "3":
        print('Você escolheu a opção 3.')
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

def menu_quiz():
    print('''
Modo de jogo
    [1] - Solo  (descrição)
    [2] - Competitivo   (descrição)
    [3] - Opção 3   (descrição)
        ''')
    escolha = input('Escolha uma opção: ')

    if escolha == "1":
        print('Você escolheu a opção 1.')
        quiz()
    elif escolha == "2":
        print('Você escolheu a opção 2.')
    elif escolha == "3":
        print('Você escolheu a opção 3.')
    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')
        main()

if __name__ == "__main__":
    main()
