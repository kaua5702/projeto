#Peça ao usuário para digitar dois números. O programa deve comparar os dois e mostrar:
# #"O maior número é: X" se um for maior que o outro.
#"Os números são iguais" se ambos forem iguais.

num1 = float(input("N1 Digite um número: "))
num2 = float(input("N2 Digite um número: "))

if num1 > num2:
    print(f"O maior número é o número {num1}.")

elif num1 < num2:
    print(f"O maior número é o número {num2}.")

else:
    print("Os números são iguais.")