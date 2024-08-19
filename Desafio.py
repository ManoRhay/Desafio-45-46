import random

def determinar_vencedor(jogador, computador):
    if jogador == computador:
        return "Empate"
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "papel" and computador == "pedra") or \
         (jogador == "tesoura" and computador == "papel"):
        return "Você venceu"
    else:
        return "Computador venceu"

opcoes = ["pedra", "papel", "tesoura"]

while True:
    jogador = input("Escolha: pedra, papel ou tesoura? ").lower()
    if jogador in opcoes:
        break
    else:
        print(f"A opção '{jogador}' é inválida: Escolha 'pedra', 'papel' ou 'tesoura'.")

computador = random.choice(opcoes)

print(f"Você escolheu: {jogador}")
print(f"Computador escolheu: {computador}")

resultado = determinar_vencedor(jogador, computador)
print(resultado)