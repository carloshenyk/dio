import textwrap

def menu():
    menu = """\n
    ##################### MENU ######################
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [n]\tNova Conta
    [l]\tListar Contas
    [u]\tNovo Usuario
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, historico_extrato, /):
    if valor > 0:
        saldo += valor
        historico_extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! Informe um número válido.")
    return saldo, historico_extrato

def sacar(*, saldo, valor, historico_extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        historico_extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, historico_extrato, numero_saques

def mostrar_extrato(saldo, /, *, historico_extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not historico_extrato else historico_extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtra_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return
    nome = input("Informe nome Completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço: ")

    usuarios.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})

def filtra_usuario(cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtra_usuario(cpf, usuarios)

    if usuario:
        print("\n###### Conta Criada com sucesso! ######")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\nUsuário não encontrado.")

def lista_contas(contas):
    for conta in contas:
        linha = f"""\
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
                """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    historico_extrato = ""
    numero_saques = 0
    usuarios = []  # Lista para armazenar usuários
    contas = []    # Lista para armazenar contas

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, historico_extrato = depositar(saldo, valor, historico_extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, historico_extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                historico_extrato=historico_extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            mostrar_extrato(saldo, historico_extrato=historico_extrato)

        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "n":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "l":
            lista_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
