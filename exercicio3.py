#Crie um programa que:Peça ao usuário para digitar um número,calcule e mostre o dobro e o triplo do número e exiba o quadrado do número.

numero = float(input("Digite um número: "))
dobro = numero * 2
triplo = numero * 3
quadrado_do_numero = numero ** 2

print(f"O dobro do número {numero}, é {dobro}. ")
print(f"O triplo do número {numero}, é {triplo}. ")
print(f"O quadrado do número {numero}, é {quadrado_do_numero}. ")

