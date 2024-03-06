import requests
import json
import random

with open('apikey.txt', 'r') as key:
    chave = key.readline()

def request_Na_Api(id):

	url = "https://genius-song-lyrics1.p.rapidapi.com/song/lyrics/"

	querystring = {"id":id}

	headers = {
			"X-RapidAPI-Key": chave,
			"X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
		}

	response = requests.get(url, headers=headers, params=querystring)

	infos = response.json()
	
	return infos


class Alternativas:

	def criaAlternativas(listaMus):

		for c,i in enumerate(listaMus):

			alternativ = []

			while len(alternativ) < 3:

				indice = random.randint(0,len(listaMus)-1)

				altern = listaMus[indice]['nome']

				if altern not in alternativ and altern != i['nome']:
					alternativ.append(altern)

			alternativ.append(i['nome'])
			alternativ = random.sample(alternativ,len(alternativ))
			listaMus[c]['alternativas'] = alternativ

		return listaMus

def retornaIds(nome):

	lista_ids = []

	url = "https://geniuslyrics-api.p.rapidapi.com/search_artist"

	querystring = {"artist":nome}

	headers = {
		"X-RapidAPI-Key": chave,
		"X-RapidAPI-Host": "geniuslyrics-api.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	lista = response.json()
	lista = lista['popular']

	for c in lista:
		lista_ids.append(c['songID'])
    
	return lista_ids[:10]


def retornaInfos(listaIds):
	
	lista_mus= []

	for id in listaIds:

		infos = request_Na_Api(id)

		nome = infos['lyrics']['tracking_data']['title']
		letra = str(infos['lyrics']['lyrics']['body']['html'].replace('<br>', '').replace('<p>', '').replace('</p>', ''))
		letra = letra[69:200]

		dic_mus = {
			'nome': nome,
			'letra': letra,
		}

		lista_mus.append(dic_mus)

	lista_mus = Alternativas.criaAlternativas(lista_mus)

	return lista_mus

def add_json(nomeArtista,listaDeMusicas):
	listaMus = ler_musicas('musicas.json')
	
	dicArt = {
		nomeArtista : listaDeMusicas
	}

	listaMus.append(dicArt)

	with open('musicas.json', 'w', encoding='utf-8') as arq:
		json.dump(listaMus, arq)

def ler_musicas(nome_arq):
    try:
        with open(nome_arq, 'r', encoding='utf-8') as arq:
            lista_musicas = json.load(arq)

    except:
        lista_musicas = []
    finally:
        return lista_musicas
    