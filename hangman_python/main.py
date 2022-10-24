while True: # tudo esta em um while porque quero ter uma maneira de recomeçar o programa no final caso o jogador queira jogar novamente
    from mimetypes import init
    import random #Importação da função já definida "Random"
    file = open('palavras.txt','r') #conexão entre o script e o arquivo txt
    content = file.readlines() #Vai ler o conteudo do arquivo txt
    def linha(): print("\n------------------------------------------------------------------------------\n") #variavel para linhas separadoras no terminal
    linha()
    print("Bem Vindo a Forca! Escreva uma letra para adivinhar a palavra!")
    linha()
    random = random.randint(0, len(content)-1)

    palavraSecreta = content[random] #variavel para a palavra secreta

    if '\n' in palavraSecreta:
        length = len(palavraSecreta)-1
    else:
        length = len(palavraSecreta)

    chutesLista = ['_']*length

    counter = 0
    wrong = 0

    while '_' in chutesLista:
        if wrong > 5:
            print('Acabaram suas chances!')
            print('A palavra secreta era....', palavraSecreta)
            print('Game Over!')
            exit()
        print(chutesLista)
        chute = input('Escreva uma letra: ').upper()

        if chute in palavraSecreta: 
            print('\n')
            print("Chute esta certo!")
            linha()
            counter = counter + 1
            
            for x in range (0, length):
                if palavraSecreta[x] == chute:
                    chutesLista[x] = chute
        else:
            print('Letra não encontrada!')
            linha()
            counter = counter + 1
            wrong = wrong + 1
    

    print('Você levou', counter, 'tentativas')
    print('A palavra secreta era....', palavraSecreta)
    resposta = input('Gostaria de jogar novamente? (s/n): ')
    if 's' in resposta: 
        continue
    elif 'n' in resposta:
        exit()            
    


    

