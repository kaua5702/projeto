#Peça ao usuário para digitar um número inteiro.
#O programa deve mostrar todos os múltiplos desse número entre 1 e 100.

numero = int(input("Digite um número inteiro para ver seus múltiplos de 1 a 100: "))

print(f"Múltiplos de {numero} entre 1 e 100: ")

for i in range(1, 101):
    if i % numero == 0:
        print(i)