from funcoes import *

opcao = 0

while opcao != 8:

    print("\nMENU")
    print("1. Cadastrar novo jogador")
    print("2. Mostrar todos os jogadores cadastrados")
    print("3. Mostrar relatório completo")
    print("4. Pesquisar jogador pelo nome")
    print("5. Alterar informações de um jogador")
    print("6. Remover jogador do cadastro")
    print("7. Mostrar estatísticas gerais")
    print("8. Encerrar programa")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        cadastrar_jogador()

    elif opcao == 2:
        mostrar_jogadores()

    elif opcao == 3:
        mostrar_relatorio()

    elif opcao == 4:
        pesquisar_jogador()

    elif opcao == 5:
        alterarInfo_jogador()

    elif opcao == 6:
        remover_jogador()

    elif opcao == 7:
        estatistica = 0
        while estatistica != 8:
            print('\nESTATISTICAS')
            print("1. Quantidade total de jogadores cadastrados")
            print("2. Maior média de desempenho")
            print("3. Menor média de desempenho")
            print("4. Média geral dos jogadores")
            print("5. Nome do jogador com melhor desempenho")
            print("6. Quantidade de jogadores com desempenho excelente")
            print("7. Quantidade de jogadores que precisam melhorar")
            print("8. Voltar para o menu")

            estatistica = int(input("Escolha uma opção: "))

            if estatistica == 1:
                qtde_jogadores()
            elif estatistica == 2:
                maiorMedia()
            elif estatistica == 3:
                menorMedia()
            elif estatistica == 4:
                mediaGeral()
            elif estatistica == 5:
                melhorDesempenho()
            elif estatistica == 6:
                qtdeJog_Excelente()
            elif estatistica == 7:
                qtdeJog_Melhorar()
            elif estatistica == 8:
                print("Voltando para o menu")

    elif opcao == 8:
        print("Programa encerrado.")

    else:
        print("Opção inválida.")
