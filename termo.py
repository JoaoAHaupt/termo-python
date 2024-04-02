from colorama import Fore, init
import random
init()

palavras = ['certo', 'feira', 'jovem', 'troca', 'amigo', 'bemol', 'folia', 'grava', 'limpo', 'noite']
palavra = random.choice(palavras)

teste = ["_" for _ in palavra]
tentativa3 = []

while True:
    tentativa = input().strip().lower()

    tentativa2 = [" " for _ in palavra]

    pontos = 0

    for i, letra in enumerate(palavra):
        if tentativa[i] == palavra[i]:
            tentativa2[i] = Fore.GREEN + tentativa[i]
            pontos += 1
        elif tentativa[i] in palavra:
            tentativa2[i] = Fore.YELLOW + tentativa[i]
        else:
            tentativa2[i] = Fore.RED + tentativa[i]


    tentativa3.append(tentativa2)
    print('\n' * 100)
    for tentativas in tentativa3:
        print(''.join(tentativas))

    if pontos == 4:
        print('Ganhou')
        break

    print('\n')
