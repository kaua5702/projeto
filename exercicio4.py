#Peça ao usuário para digitar o nome e a idade, verifique se a pessoa tem 18 anos ou mais e exiba uma mensagem personalizada:"Fulano pode entrar." (se tiver 18 ou mais)"Fulano não pode entrar." (se tiver menos de 18)

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print(f"{nome}, pode entrar")

else:
    print(f"{nome}, você não pode entrar")