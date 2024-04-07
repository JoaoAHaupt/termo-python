from colorama import Fore, init
import random
init()

palavras = ['certo', 'feira', 'jovem', 'troca', 'amigo', 'bemol', 'folia', 'grava', 'limpo', 'noite']
palavra = random.choice(palavras)

tentativas_anteriores = []

num_tentativas = 0

print('TERMO')

while True:
    tentativa = input().strip().lower()
    if len(tentativa) != 5:
        for i in range(5):
            tentativa = tentativa + tentativa[len(tentativa) - 1]

    validacao = [" " for _ in palavra]



    for i, letra in enumerate(palavra):
        if tentativa[i] == palavra[i]:
            validacao[i] = Fore.GREEN + tentativa[i]
        elif tentativa[i] in palavra:
            validacao[i] = Fore.YELLOW + tentativa[i]
        else:
            validacao[i] = Fore.RED + tentativa[i]


    tentativas_anteriores.append(validacao)
    print('\n' * 100)
    for tentativas in tentativas_anteriores:
        print(''.join(tentativas))

    if palavra == tentativa:
        print('Ganhou!')
        break

    num_tentativas += 1

    if num_tentativas == 5:
        print(Fore.RED + 'PERDEU!')
        print('Palavra correta ' + palavra)
        break

    print('\n')
