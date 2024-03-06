def menu():
    print('''MENU
    [1] JOGAR
    [2] ADICIONAR ARTISTA
    [3] RANKING
    [4] SAIR
    ''')

def printar_alternativas(lista):

    for c, d in enumerate(lista):
        print(f'({c+1}) {d}')

def resultado(lista,resposta, nome):

    if lista[resposta-1] == nome:
        print('você acertou')
        return 10
    else:
        print('você errou')
        return 0

def condicao(frase):

    while True:
        cond = input(frase).upper().strip()
        if cond in 'SN':
            break

    return cond

def input_limitado(min, max):

    while True:
        
        try:
            while True:
                num = int(input(': '))
                if num > min and num < max:
                    break
                else:
                    print('ERRO: o valor não está entre as opções')
        except:
            print('ERRO: digite um valor valido!')
        else:
            return num 
