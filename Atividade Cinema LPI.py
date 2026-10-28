while True:    
    print("===== SISTEMA DE AVALIAÇÃO =====\n")
    print("1. Cadastrar avaliação\n2. Listar avaliações\n3. Consultar estatísticas\n4. Sair\n")
    opcao = int(input("Escolha uma opção:\n"))

    if opcao == 1:
        with open("avaliacoes.txt", "a") as arquivo:
            idade = int(input("Qual a sua idade?\n"))
            opcao_de_avaliacao = str(input("Como você avalia o atendimento do nosso estabelecimento?\nÓtimo\nBom\nRegular\nPéssimo\n")).capitalize()
            arquivo.write(f"{idade};{opcao_de_avaliacao}\n")

    try:    
        if opcao == 2:
            with open("avaliacoes.txt", "r") as arquivo:
                print("===== AVALIAÇÕES CADASTRADAS =====\n")
                for indice, linha in enumerate(arquivo, 1):
                    linha_limpa = linha.strip()
                    
                    if not linha_limpa:
                        continue

                    idade, avaliacao = linha.strip().split(";")
                    print(f"Cliente {indice} - Idade: {idade} - Avaliação: {avaliacao}\n")

    except FileNotFoundError:
        print("Ainda não há avaliações cadastradas.\n")

    if opcao == 3:
        print("===== ESTATÍSTICAS DAS AVALIAÇÕES =====\n")

        total_respondentes = 0
        qtd_otimo = 0
        qtd_bom = 0
        qtd_regular = 0
        qtd_pessimo = 0

        idade_mais_velho = 0
        avaliacao_mais_velho = ""
        idade_mais_novo = 0
        avaliacao_mais_novo = ""

        try:
            with open("avaliacoes.txt", "r") as arquivo:
                for linha in arquivo:
                    linha_limpa = linha.strip()

                    if not linha_limpa: #Para o código ignorar linhas sem conteúdo/vazias
                        continue
                    
                    total_respondentes += 1
                    idade_str, avaliacao = linha_limpa.split(";")
                    idade_avaliacao = int(idade_str)
                    avaliacao = avaliacao.strip()

                    if avaliacao == "Ótimo":
                        qtd_otimo += 1
                    elif avaliacao == "Bom":
                        qtd_bom += 1
                    elif avaliacao == "Regular":
                        qtd_regular += 1
                    elif avaliacao == "Péssimo":
                        qtd_pessimo += 1

                    if total_respondentes == 1:
                        idade_mais_velho = idade_avaliacao
                        avaliacao_mais_velho = avaliacao
                        idade_mais_novo = idade_avaliacao
                        avaliacao_mais_novo = avaliacao
                    else:
                        if idade_avaliacao > idade_mais_velho:
                            idade_mais_velho = idade_avaliacao
                            avaliacao_mais_velho = avaliacao
                        
                        if idade_avaliacao < idade_mais_novo:
                            idade_mais_novo = idade_avaliacao
                            avaliacao_mais_novo = avaliacao
                
                print(f"Respondente mais velho:\nIdade: {idade_mais_velho} anos\nAvaliação: {avaliacao_mais_velho}\n")
                print(f"Respondente mais novo:\nIdade: {idade_mais_novo} anos\nAvaliação: {avaliacao_mais_novo}\n")

        except FileNotFoundError:
            print("Ainda não há avaliações cadastradas.\n")

    if opcao == 4:
        print("Encerrando programa...")
        break