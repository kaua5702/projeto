import time

while True:
    numero = int(input('\nDigite um numero inteiro: '))
    time.sleep(1)
    print(f'\n A tabuada de {numero} é:\n ')
    time.sleep(1)

    for i in range(1, 11):
       print(f'{numero} x {i} = {numero * i} ')
       time.sleep(0.5)
       
    escolha = input('\nDeseja tentar outro número? (s/n): ') 
    time.sleep(1)
    if escolha == 's':
        continue
    else:
        print('ok, encerrando...')
        time.sleep(1)
        break
           