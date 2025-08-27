#Crie um programa pedindo para digitar um número, e diga se ele é impar ou par


número = int(input("Digite um número inteiro: "))

if número %2 == 0:
    print(f"O número {número}, é par")
else:
    print(f"O número {número}, é ímpar")

# O "%" foi usado para resto da divisão 