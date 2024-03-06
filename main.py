from funcoes_musica import *
from funcoes_jogo import *
from funcoes_ranking import *
import time

while True:

    menu()
    opc = input_limitado(0,6)

    match opc:

        case 1:
            play = True
            listaArtistas = ler_musicas('musicas.json')

            while play:
                result = 0
                art = []
                cont = 0

                player = input('digite seu nome: ')

                print('ESCOLHA UM ARTISTA')

                for artista in listaArtistas:
                    art.append(str(artista.keys())[12:-3])

                printar_alternativas(art)
                opc = input_limitado(0,3)

                listaMusicas = listaArtistas[opc-1].values()
                
                for musicas in listaMusicas:

                    for m in musicas:

                        print(m['letra'])

                        printar_alternativas(m['alternativas'])
                        escolha = input_limitado(0,5)

                        result += resultado(m['alternativas'],escolha,m['nome'])

                        cond = condicao('deseja continuar?\n[S/N]: ')
                        cont += 1
                        time.sleep(1)

                        if cond == 'N' or cont >= 10:
                            play = False
                            break
            
            add_ranking(player,result)

        case 2:

            print('OBS: por inconsistência da API e o numero limitado de requisições podem ocorrer erros na adicão do artista')

            try:
                nome = input('digite o nome do artista \n(certifique-se de digitar o nome corretamente): ')

                listaIds = retornaIds(nome)
                musicas = retornaInfos(listaIds)

                add_json(nome,musicas)
            except:
                print('ERRO: artista não adicionado')
            else:
                print('artista adicionado')
        
        case 3:

            ranking = ler_ranking('ranking.json')

            mostrar_ranking(ranking)

        case 4:
            break

print('jOGO ENCERRADO')