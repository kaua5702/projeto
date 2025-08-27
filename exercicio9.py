#Peça ao usuário para digitar um número inteiro.
#O programa deve mostrar a tabuada desse número de 1 até 10.

numero = int(input("Digite um número inteiro para ver a tabuada: "))

print(f"Tabuada do {numero}: ")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
