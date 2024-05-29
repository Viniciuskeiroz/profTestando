import random

numero_secreto = random.randint(1, 100)

tentativas = 0
while True:
    tentativas += 1
    palpite = int(input("Digite um numero de 1 a 100: "))

    if palpite < numero_secreto:
        print("O número secreto é maior.")
    elif palpite > numero_secreto:
        print("O número secreto é menor.")
    else:
          print(f"Parabéns! Você acertou o número secreto em {tentativas} tentativas.")
          break