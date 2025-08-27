#Peça ao usuário para digitar duas notas.
#O programa deve calcular a média dessas notas e mostrar:
#"Aprovado" se a média for maior ou igual a 6.
#"Reprovado" se a média for menor que 6.

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
media = (nota1 + nota2) /2

if media >= 6:
    print("Aprovado.")

else:
    print("Reprovado.")