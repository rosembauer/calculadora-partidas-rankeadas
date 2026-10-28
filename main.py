def calcular_nivel_rankeado(vitorias, derrotas):
    # Cálculo do saldo de rankeadas (vitórias - derrotas)
    saldo_vitorias = vitorias - derrotas
    nivel = ""

    # Estrutura de decisão para determinar o nível com base nas vitórias
    if vitorias < 10:
        nivel = "Ferro"
    elif 10 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"

    return saldo_vitorias, nivel


# Lista de jogadores para demonstrar o uso de laços de repetição
historico_jogadores = [
    {"vitorias": 8, "derrotas": 3},
    {"vitorias": 15, "derrotas": 5},
    {"vitorias": 35, "derrotas": 12},
    {"vitorias": 75, "derrotas": 20},
    {"vitorias": 88, "derrotas": 15},
    {"vitorias": 95, "derrotas": 10},
    {"vitorias": 120, "derrotas": 25}
]

# Laço de repetição (for) para percorrer e exibir os resultados
for jogador in historico_jogadores:
    saldo, nivel = calcular_nivel_rankeado(jogador["vitorias"], jogador["derrotas"])
    print(f"O Herói tem de saldo de {saldo} está no nível de {nivel}")