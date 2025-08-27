import time

numero = int(input("Digite um numero inteiro positivo para iniciar o lançamento do míssil: "))


while numero >= 0:
    print(numero)
    time.sleep(1)
    numero -= 1 

print("\n LANÇAR!!! \n") 

time.sleep(2)

print("O ataque foi um sucesso! \n",) 
time.sleep(2)

print("Os soviéticos foram derrotados! \n")
time.sleep(2)

print("Aguerde instruções para a próxima missão. \n")
time.sleep(2)

print("Câmbio e desligo.")

