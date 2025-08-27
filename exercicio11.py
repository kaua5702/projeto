#Peça ao usuário para digitar três notas (valores de 0 a 10).
#Calcule a média das notas.
#Informe se o aluno está "Aprovado" (média maior ou igual a 7) ou "Reprovado" (média menor que 7).

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) /3

if media >= 7:
    print("Aprovado.")

else: 
    print("Reprovado.")