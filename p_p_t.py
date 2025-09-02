import random
import time

print('\nVamos jogar pedra, papel e tesoura?\n ')
time.sleep(1)

opçoes = ['pedra', 'papel', 'tesoura']
def escolha_opçao(opçoes):
    escolha_usuario = input('Escolha pedra, papel ou tesoura: ').lower()
    time.sleep(1)
    while escolha_usuario not in opçoes:
        escolha_usuario = input('Escolha uma opção válida: ').lower()
        time.sleep(1)
    print(f'Você escolheu {escolha_usuario}')
    time.sleep(1)
    return escolha_usuario
        

def opçao_pc(opçoes):
    escolha_pc = random.choice(opçoes)
    print(f'O computador escolheu {escolha_pc}')
    time.sleep(1)
    return escolha_pc

def ler_resultado(jogador, pc):
    if jogador == pc:
        print('Empate!')
        time.sleep(1)

    elif jogador == ('pedra' and pc == 'tesoura') or \
         jogador == ('papel' and pc == 'pedra') or \
         jogador == ('tesoura' and pc == 'papel'):
         print('Você ganhou!!')
         time.sleep(1)

    else:
        print('Computador ganhou!!')
        time.sleep(1)

while True:
    escolha_usuario = escolha_opçao(opçoes)
    escolha_pc = opçao_pc(opçoes)
    resultado = ler_resultado(escolha_usuario, escolha_pc)

    escolha = input('Deseja jogar novamente? (s/n): ').lower()
    time.sleep(1)
    if escolha == 's':
        continue
    else:
        print('Encerrando...')
        time.sleep(1)
        break
