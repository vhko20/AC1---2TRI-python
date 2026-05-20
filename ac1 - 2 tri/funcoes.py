from arrays import nomes, partidas, gols

def media(i):
    return gols[i] / partidas[i]

def desempenho(i):
    m = media(i)

    if m >= 2:
        return "Excelente"
    elif m >= 1:
        return "Bom"
    else:
        return "Precisa melhorar"

def cadastrar_jogador():

    continuar = "s"

    while continuar == "s":

        nome = input("Digite o nome do jogador: ")
        partida = float(input("Digite a quantidade de partidas: "))
        gol = float(input("Digite a quantidade de gols: "))

        nomes.append(nome)
        partidas.append(partida)
        gols.append(gol)

        print("Jogador cadastrado com sucesso.")

        continuar = input("Deseja cadastrar outro jogador? (s/n): ")


def mostrar_jogadores():
    print('\nJOGADORES')
    print(nomes)
    

def mostrar_relatorio():
    if len(nomes)==0:
        print("Sem jogadores cadastrados")
    else:
        print("\nRelátorio dos jogadores")
        for i in range(len(nomes)):
            m = media(i)
            d = desempenho(i)
            print(f"Nome:{nomes[i]} | Partidas: {partidas[i]} | Gols: {gols[i]} | Média p/ partida: {m} | Desempenho: {d}")
            i+=1


def pesquisar_jogador():

    if len(nomes) == 0:
        print("Sem jogadores cadastrados")

    else:
        pesquisa = input("Digite o nome do jogador: ")

        if pesquisa in nomes:
            i = nomes.index(pesquisa)
            m = media(i)
            d = desempenho(i)
            print(f"Nome:{nomes[i]} | Partidas: {partidas[i]} | Gols: {gols[i]} | Média p/ partida: {m} | Desempenho: {d}")
        else:
            print("Não há um jogador com esse nome")


def alterarInfo_jogador():

    if len(nomes) == 0:
        print("Sem jogadores cadastrados")

    else:
        jogadorAlt = input("Digite o nome do jogador: ")

        if jogadorAlt in nomes:
            mudar = input("O que você quer alterar? (partidas/gols)")
            index = nomes.index(jogadorAlt)
            if mudar == partidas:
                novaPartida = float(input("Digite a nova quantidade de partidas"))
                partidas[index] = novaPartida
                print("Quantidade de partidas alterada com sucesso")
            elif mudar == gols:
                novoGols = float(input("Digite a nova quantidade de gols"))
                gols[index] = novoGols
                print("Quantidade de gols alterada com sucesso")
            else:
                print("Opção inválida")

        else:
            print("Não há um jogador com esse nome")


def remover_jogador():
    if len(nomes) == 0:
        print("Sem jogadores cadastrados")
    else:
        jogadorRemove = input("Digite o nome do jogador: ")
        posicao = nomes.index(jogadorRemove)
        if jogadorRemove in nomes:
            nomes.pop(posicao)
            partidas.pop(posicao)
            gols.pop(posicao)


def qtde_jogadores():
    qtde = len(nomes)
    print(qtde)

def maiorMedia():
    maiorMedia = 0
    for i in range(len(nomes)):
        m = media(i)
        if maiorMedia < m:
            maiorMedia = m
    print(f"A maior média é: {maiorMedia}")

def menorMedia():
    menorMedia = 10
    for i in range(len(nomes)):
        m = media(i)
        if menorMedia > m:
            menorMedia = m
    print(f"A menor média é: {menorMedia}")

def mediaGeral():
    somatotal = 0
    for i in range(len(partidas)):
        m = media(i)
        somatotal+=m
    mediaGeral = somatotal / len(partidas)
    print(f"A média geral dos jogadores é {mediaGeral}")

def melhorDesempenho():
    maiorMedia = 0
    for i in range(len(nomes)):
        m = media(i)
        if maiorMedia < m:
            maiorMedia = m
            posicao = i
    print(f"O jogador com o maior desempenho é o {nomes[posicao]}")

def qtdeJog_Excelente():
    qtdeExcelente = 0
    for i in range(len(nomes)):
        m = media(i)
        if m>=2:
            qtdeExcelente+=1
    print(f"Tem {qtdeExcelente} jogadores excelentes")

def qtdeJog_Melhorar():
    qtdeMelhorar = 0
    for i in range(len(nomes)):
        m = media(i)
        if m<1:
            qtdeMelhorar+=1
    print(f"Tem {qtdeMelhorar} jogadores que precisam melhorar")
