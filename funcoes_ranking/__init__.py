import json

def add_ranking(nome, pontuação):
    lista_jogs= []

    jogador = {
        'nome': nome,
        'pontuação': pontuação
    }
    try:

        with open('ranking.json', 'r') as arq:
            lista_jogs = json.load(arq)

    except:

        lista_jogs = []

    finally:

        lista_jogs.append(jogador)
        lista_jogs.sort(key=lambda x: x["pontuação"], reverse=True)

    with open('ranking.json', 'w', encoding='utf-8') as arq:
        json.dump(lista_jogs, arq)

def ler_ranking(nome):
    try:
        with open(nome, 'r') as arq:
            lista_r = json.load(arq)
    except:
        print('ERRO: ranking não criado')
        lista_r = []
    finally:
        return lista_r

def mostrar_ranking(ranking):
    
    for n,r in enumerate(ranking):
        print(f'{n+1}º: {r["nome"]}, pts: {r["pontuação"]}')