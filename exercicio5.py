#Peça ao usuário para digitar um número. O programa deve verificar e mostrar:
#Número positivo" se o número for maior que zero.
#"Número negativo" se for menor que zero.
# "Zero" se o número for exatamente zero.

numero = float(input("Digite um número: "))

if numero > 0:
    print(f"O número {numero}, é positivo.")

elif numero < 0:
    print(f"O número {numero}, é negativo.")

else:
    print(f"O número {numero}, é exatamente 0.")