from time import sleep

# Estabelecendo as Listas
lista_produtos = [['Mouse', 45.0, 21], ['Teclado', 89.0, 18], ['Tablet', 890.0, 12], ['Monitor', 1050.0, 8], ['Pendrive', 95, 30],
                  ['Celular', 1600, 10], ['Projetor', 3500, 5], ['Notebook', 3200, 12], ['Roteador', 205, 20], ['Impressora', 130, 10]]
lista_clientes = [['Camilly', '(83)9754-2297', []], ['Márcio', '(83)9751-6544', []], ['Rômulo', '(83)99676-2113', []],
                  ['Pablo', '(83)99688-8741', []],['Paula', '(83)99875-9933', []], ['Rogério', '(83)99356-91122', []]]
lista_vendedores = [['Ellen', '(83)99999-9992', [], []], ['Nino', '83999999999', [], []], ['Joelma', '(83)99443-7734', [], []],
                    ['Marcelo', '(83)99122-9802', [], []], ['Ana', '(83)99178-9955', [], []]]
vendas_realizadas = []

carrinho = []
sair = False  # Variável de controle para sair do loop principal


#FUNÇÃO PARA MOSTRAR CARRINHO DE COMPRAS
def mostrar_carrinho(carrinho):
    total = itens = 0
    print('=' * 60)
    print(f'{"CARRINHO DE COMPRAS":^60}')
    print('=' * 60)
    for pos, item in enumerate(carrinho, start=1):
        nome, preco, quantidade = item
        print(f'{pos:<3}{nome:<35}R$ {preco:>6.2f}{quantidade:>6} unid.')
        total += preco * quantidade
        itens += quantidade
    print('-' * 61)
    print(f'{"TOTAL":<38}R$ {total:>6.2f}{itens:>6} unid.')
    print('=' * 61)
    print('')

#FUNÇÃO PARA REMOVER UM PRODUTO DO CARRINHO DE COMPRAS
def remover_produto_carrinho(carrinho):
    mostrar_carrinho(carrinho)
    if carrinho:
        while True:
            try:
                indice = int(input('Digite o número do produto que deseja remover: '))
                if 1 <= indice <= len(carrinho):
                    print('Removendo...')
                    sleep(1)
                    # Remove a quantidade do produto do carrinho
                    produto_removido = carrinho.pop(indice - 1)
                    # Devolve a quantidade removida do produto ao estoque
                    for produto in lista_produtos:
                        if produto[0] == produto_removido[0]:
                            produto[2] += produto_removido[2]
                            break
                    if produto_removido[2] <= 1:
                        print(f'{produto_removido[2]} {plural(produto_removido[0], produto_removido[2])} foi removido do carrinho e devolvido ao estoque.')
                    elif produto_removido[2] > 1:
                        print(f'{produto_removido[2]} {plural(produto_removido[0], produto_removido[2])} foram removidos do carrinho e devolvidos ao estoque.')

                    break
                else:
                    print('Índice inválido. Tente novamente.')
            except ValueError:
                print('Valor inválido. Digite um número inteiro.')

#FUNÇÃO PARA MOSTRAR O RELATÓRIO DE VENDAS
def relatorio_vendas(vendas_realizadas):
    print('=' * 60)
    print(f'{"RELATÓRIO DE VENDAS":^60}')
    print('=' * 60)
    for venda in vendas_realizadas:
        cliente, vendedor, carrinho = venda
        total = sum(item[1] * item[2] for item in carrinho)
        impostos = total * 0.25
        comissao = total * 0.05
        print(f'Cliente: {cliente[0]} - Vendedor: {vendedor[0]}')
        for item in carrinho:
            print(f'  {item[0]:<35}R$ {item[1]:>6.2f}{item[2]:>6} unid.')
        print(f'Total: R$ {total:>6.2f}')
        print(f'Impostos (25%): R$ {impostos:>6.2f}')
        print(f'Comissão do Vendedor (5%): R$ {comissao:>6.2f}')
        print('-' * 60)
    print('=' * 60)

# FUNÇÃO PARA MOSTRAR O PLURAL DOS PRODUTOS DE FORMA CORRETA
def plural(palavra, quantia):
    if quantia == 1:
        return palavra
    # Regras básicas para formação do plural
    if palavra.endswith('ão'):
        return palavra[:-2] + 'ões'
    elif palavra.endswith('m'):
        return palavra[:-1] + 'ns'
    elif palavra.endswith('l'):
        return palavra[:-1] + 'is'
    elif palavra.endswith('r') or palavra.endswith('z'):
        return palavra + 'es'
    else:
        return palavra + 's'

while not sair:
    # Menu Inicial
    print(f'{"=-"*5}{"TECH POINT ELETRÔNICOS-"}{"=-"*5}')
    print('-'*35)
    print(f'{"O QUE DESEJA FAZER?":^35}')
    print('-'*35)
    print('[1] Cadastrar Produtos\n[2] Cadastrar Cliente\n[3] Cadastrar Vendedor\n[4] Escolher Produtos para Compra\n'
          '[5] Ir para Carrinho de Compras\n[6] Relatório de Vendas\n[7] Sair')
    print('-'*35)
    opcao = int(input('Digite a opção escolhida: '))

    # 1 Caso Escolha Cadastrar Produtos
    if opcao == 1:
        dados = []
        while True:
            produto = str(input('Produto: '))
            preco = float(input('Preço: '))
            quantidade = int(input('Quantidade: '))
            dados.append(produto)
            dados.append(preco)
            dados.append(quantidade)
            lista_produtos.append(dados[:])
            dados.clear()
            parar = str(input('Deseja Continuar? [S/N]: '))
            if parar in 'Nn':
                print('Voltando para o Menu Principal...\n')
                sleep(1)
                break

    # 2 Caso escolha Cadastrar Cliente
    elif opcao == 2:
        dados = []
        while True:
            nome = str(input('Nome do Cliente: '))
            telefone = str(input('Telefone do Cliente: '))
            dados.append(nome)
            dados.append(telefone)
            dados.append([])  # Adicionando lista  vazia - COMPRAS
            lista_clientes.append(dados[:])
            dados.clear()
            parar = str(input('Deseja Continuar? [S/N]: '))
            if parar in 'Nn':
                print('Voltando para o Menu Principal...\n')
                sleep(1)
                break

    # 3 Caso escolha Cadastrar Vendedor
    elif opcao == 3:
        dados = []
        while True:
            nome = str(input('Nome do Vendedor: '))
            telefone = str(input('Telefone do Vendedor: '))
            dados.append(nome)
            dados.append(telefone)
            dados.append([])  # Adicionando lista de vendas vazia - COMISSÃO
            dados.append([])  # Adicionando lista de vendas vazia - VENDAS
            lista_vendedores.append(dados[:])
            dados.clear()
            parar = str(input('Deseja Continuar? [S/N]: '))
            if parar in 'Nn':
                print('Voltando para o Menu Principal...\n')
                sleep(1)
                break

    # 4 Caso Escolha Realizar Compras
    elif opcao == 4:
        while True:
            print('-' * 37)
            print(f'{"LISTA DE PRODUTOS E PREÇOS":^37}')
            print('-' * 40)
            for pos in range(len(lista_produtos)):
                print('{:.<3}'.format(pos+1), end='')
                print('{:.<30}'.format(lista_produtos[pos][0]), end='')
                print('R$ {:.>.2f}'.format(lista_produtos[pos][1]))
            print('-' * 40)

            # Pergunta Qual Produto quer Comprar
            prod = int(input('Qual produto o cliente quer comprar? '))
            print(f"A quantidade de {plural(lista_produtos[prod - 1][0], 2)} no estoque é {lista_produtos[prod-1][2]}.")

            # Pergunta a Quantidade do Produto
            quant = int(input('Qual a quantidade deseja comprar? '))
            # Verifica se a quantidade pedido é maior que a quantidade em estoque.
            # Se for, dá a infor,ação e pede novamente pra escolher a quantidade.
            while quant > lista_produtos[prod-1][2]:
                print(f'A quantidade escolhida é maior que a quantidade que temos em estoque. Tente novamente. ')
                quant = int(input('Qual a quantidade deseja comprar? '))

            # A quantidade do produto que foi pra o carrinho é retirada do estoque.
            lista_produtos[prod-1][2] = lista_produtos[prod-1][2] - quant

            # Adiciona o produto ao carrinho.
            car = []
            car.append(lista_produtos[prod-1][0])
            car.append(lista_produtos[prod-1][1])
            car.append(quant)
            carrinho.append(car[:])

            # Informa o que foi adicionado ao carrinho e mostra o conteúdo dele
            produto_pluralizado = plural(lista_produtos[prod - 1][0], quant)
            sleep(0.5)
            print('-' * 50)
            print(f'{quant} {produto_pluralizado} adicionado(s) ao carrinho de compras, que agora contém: ')

            for c in range(len(carrinho)):
                print(f'{carrinho[c][2]} {plural(carrinho[c][0], carrinho[c][2])}')
            car.clear()

            # Opção de continuar comprando ou parar
            parar = str(input('\nDeseja Comprar mais Produtos? [S/N]: '))
            if parar in 'Nn':
                sleep(0.5)
                print('-' * 40)

                # Opção de Ir Direto pro pagamento ou Voltar ao Menu
                parar2 = int(input('O que você deseja?\n[1] Ir direto para o pagamento\n[2] Voltar para o Menu principal\nDigite sua Opção: '))
                if parar2 == 2:
                    print('Voltando para o Menu Principal...\n')
                    sleep(1)
                    break
                elif parar2 == 1:
                    mostrar_carrinho(carrinho)

                    # Pede confirmação do Pagamento
                    pagar = str(input('Deseja finalizar e Pagar o pedido? [S] ou [N] '))

                    # Mostra a lista de clientes cadastrados
                    if pagar in 'Ss':
                        print('-' * 37)
                        print(f'{"LISTA DE CLIENTES":^37}')
                        print('-' * 37)
                        for pos in range(len(lista_clientes)):
                            print('[{}]'.format(pos + 1), end='')
                            print(' {}'.format(lista_clientes[pos][0]))
                        print('-' * 40)

                        # Pede para Escolher quem é o Cliente
                        cliente = int(input('Informe Qual o cliente: '))

                        # Mostra a lista de vendedores cadastrados
                        print('-' * 37)
                        print(f'{"LISTA DE VENDEDORES":^37}')
                        print('-' * 37)
                        for pos in range(len(lista_vendedores)):
                            print('[{}]'.format(pos + 1), end='')
                            print(' {}'.format(lista_vendedores[pos][0]))
                        print('-' * 40)

                        # Pede para Escolher quem é o Vendedor
                        vendedor = int(input('Informe Qual o vendedor: '))

                        # Adiciona o que foi comprado à lista de compras do Cliente e à lista de vendas do vendedor
                        lista_clientes[cliente - 1][len(lista_clientes[cliente - 1])-1].extend(carrinho[:])
                        lista_vendedores[vendedor - 1][len(lista_vendedores[vendedor - 1])-1].extend(carrinho[:])

                        # Adiciona venda ao relatório de vendas
                        vendas_realizadas.append((lista_clientes[cliente - 1], lista_vendedores[vendedor - 1], carrinho[:]))

                        #print(f'Lista de compras de {lista_clientes[cliente - 1][0]}: {carrinho}') - APAGAR
                        #print(f'Lista de vendas de {lista_vendedores[vendedor - 1][0]}: {lista_vendedores[vendedor - 1][3]}') - APAGAR
                        #print(lista_vendedores) - APAGAR
                        #print(lista_clientes) - APAGAR

                        #Limpa o carrinho e confirma que a compra foi realizada com sucesso
                        carrinho.clear()
                        sleep(1)
                        print('\033[1;32m*\033[0m' * 52)
                        print('\033[1;32mCompra processada e Pagamento realizado com Sucesso!\033[0m')
                        print('\033[1;32m*\033[0m' * 52)
                        sleep(1)
                        print('')

                        #Dá a opção de voltar pra o Menu Principal ou Encerrar o programa
                        encerrar = input('Pressione \033[1;34mQUALQUER TECLA\033[0m para voltar ao \033[1;34mMENU PRINCIPAL\033[0m  ou \033[1;31mdigite 9\033[0m para \033[1;31msair\033[0m: ')
                        if encerrar == '9':
                            print('Obrigado e volte sempre!')
                            sair = True
                            break
                        else:
                            print('-' * 43)
                            print('Voltando para o Menu Principal...\n')
                            sleep(1)
                            break

                    #Já que não quer finalizar o pedido e pagar e Volta ao menu principal
                    elif parar in 'Nn':
                        print('-' * 43)
                        print('Voltando para o Menu Principal...\n')
                        sleep(1)
                        break

                    # Informa que a opção é inválida e Volta ao menu principal
                    else:
                        print('Opção Inválida')
                        print('Voltando para o Menu Principal...\n')
                        sleep(1)


    # 5 Caso Escolha Ir para Carrinho de Compras
    elif opcao == 5:
        mostrar_carrinho(carrinho)
        opcao_carrinho = input('O que deseja fazer?\n[1] Finalizar e Pagar o pedido\n[2] Remover um produto do carrinho\n[3] Voltar para o Menu Principal\nDigite sua Opção: ')
        if opcao_carrinho == '1':
            # Pede confirmação do Pagamento
            pagar = str(input('Deseja finalizar e Pagar o pedido? [S] ou [N] '))

            # Mostra a lista de clientes cadastrados
            if pagar in 'Ss':
                print('-' * 37)
                print(f'{"LISTA DE CLIENTES":^37}')
                print('-' * 37)
                print('{:<2}'.format('[0]'), end='')
                print('{}'.format(' Novo Cliente'))
                for pos in range(len(lista_clientes)):
                    print('[{}]'.format(pos + 1), end='')
                    print(' {}'.format(lista_clientes[pos][0]))
                print('-' * 40)

                # Pede para Escolher quem é o Cliente
                cliente = int(input('Informe Qual o cliente: '))

                # Mostra a lista de vendedores cadastrados
                print('-' * 37)
                print(f'{"LISTA DE VENDEDORES":^37}')
                print('-' * 37)
                print('{:<2}'.format('[0]'), end='')
                print('{}'.format(' Novo Vendedor'))
                for pos in range(len(lista_vendedores)):
                    print('[{}]'.format(pos + 1), end='')
                    print(' {}'.format(lista_vendedores[pos][0]))
                print('-' * 40)

                # Pede para Escolher quem é o Vendedor
                vendedor = int(input('Informe Qual o vendedor: '))

                # Adiciona o que foi comprado à lista de compras do Cliente e à lista de vendas do vendedor
                lista_clientes[cliente - 1][len(lista_clientes[cliente - 1]) - 1].extend(carrinho[:])
                lista_vendedores[vendedor - 1][len(lista_vendedores[vendedor - 1]) - 1].extend(carrinho[:])

                # Adiciona venda ao relatório de vendas
                vendas_realizadas.append((lista_clientes[cliente - 1], lista_vendedores[vendedor - 1], carrinho[:]))

                # print(f'Lista de compras de {lista_clientes[cliente - 1][0]}: {carrinho}') - APAGAR
                # print(f'Lista de vendas de {lista_vendedores[vendedor - 1][0]}: {lista_vendedores[vendedor - 1][3]}') - APAGAR
                # print(lista_vendedores) - APAGAR
                # print(lista_clientes) - APAGAR

                # Limpa o carrinho e confirma que a compra foi realizada com sucesso
                carrinho.clear()
                sleep(1)
                print('\033[1;32m*\033[0m' * 52)
                print('\033[1;32mCompra processada e Pagamento realizado com Sucesso!\033[0m')
                print('\033[1;32m*\033[0m' * 52)
                sleep(1)
                print('')

                # Dá a opção de voltar pra o Menu Principal ou Encerrar o programa
                encerrar = input(
                    'Pressione \033[1;34mQUALQUER TECLA\033[0m para voltar ao \033[1;34mMENU PRINCIPAL\033[0m  ou \033[1;31mdigite 9\033[0m para \033[1;31msair\033[0m: ')
                if encerrar == '9':
                    print('Obrigado e volte sempre!')
                    sair = True
                    break
                else:
                    print('-' * 43)
                    print('Voltando para o Menu Principal...\n')
                    sleep(1)

        # Caso Escolha Remover o produto do carrinho
        elif opcao_carrinho == '2':
            while True:
                remover_produto_carrinho(carrinho)
                # Dá a opção de voltar pra o Menu Principal ou continuar removendo produtos
                parar3 = int(input('O que você deseja?\n[1] Remover mais produtos do carrinho\n[2] Voltar para o Menu principal\nDigite sua Opção: '))
                if parar3 == 2:
                    print('Voltando para o Menu Principal...\n')
                    sleep(1)
                    break
                elif parar3 == 1:
                    continue
                else:
                    print('Opção Inválida.')
                    print('Voltando para o Menu Principal...\n')
                    sleep(1)




        # Caso escolha voltar ao Menu Principal
        elif opcao_carrinho == '3':
            print('Voltando para o Menu Principal...\n')
            sleep(1)

    # 6 Caso Escolha Relatório de Vendas
    elif opcao == 6:
        relatorio_vendas(vendas_realizadas)
        fechar = input(
            'Pressione \033[1;34mQUALQUER TECLA\033[0m para voltar ao \033[1;34mMENU PRINCIPAL\033[0m  ou \033[1;31mdigite 9\033[0m para \033[1;31msair\033[0m: ')
        if fechar == '9':
            print('Obrigado e volte sempre!')
            sair = True
            break
        else:
            print('-' * 43)
            print('Voltando para o Menu Principal...\n')
            sleep(1)


    # 7 Caso Escolha Sair
    elif opcao == 7:
        print('')
        print('Obrigado e volte sempre!')
        break


    # 7 Caso Escolha um número fora das opções
    else:
        print('Opção Inválida. Tente Novamente.\n')
