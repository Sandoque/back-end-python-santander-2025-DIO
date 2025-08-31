import datetime
import textwrap

def exibir_menu():
    print("\n" + "="*40)
    print("      BANCO PYTHON v1.0".center(40))
    print("="*40)
    print("[d] Depositar")
    print("[s] Sacar")
    print("[e] Extrato")
    print("[nu] Novo usuário")
    print("[nc] Nova conta")
    print("[lc] Listar contas")
    print("[q] Sair")
    print("="*40)

def obter_opcao():
    return input("Selecione a opção desejada: ").strip().lower()

def depositar(saldo, transacoes):
    try:
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            transacoes.append({
                "tipo": "Depósito",
                "valor": valor,
                "data": datetime.datetime.now()
            })
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! Valor deve ser positivo.")
    except ValueError:
        print("Entrada inválida! Digite um valor numérico.")
    return saldo

def sacar(saldo, transacoes, numero_saques, limite, LIMITE_SAQUES):
    try:
        if numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
            return saldo, numero_saques
        valor = float(input("Informe o valor do saque: R$ "))
        if valor <= 0:
            print("Operação falhou! Valor de saque inválido.")
        elif valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > limite:
            print("Operação falhou! O valor excede o limite de R$ 500.00.")
        else:
            saldo -= valor
            transacoes.append({
                "tipo": "Saque",
                "valor": valor,
                "data": datetime.datetime.now()
            })
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    except ValueError:
        print("Entrada inválida! Digite um valor numérico.")
    return saldo, numero_saques

def exibir_extrato(transacoes, saldo):
    print("\n========== EXTRATO ==========")
    if not transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in transacoes:
            data = transacao["data"].strftime("%d/%m/%Y %H:%M")
            print(f"{data} - {transacao['tipo']}: R$ {transacao['valor']:.2f}")
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("=============================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ").strip()
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    nome = input("Informe o nome completo: ").strip()
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ").strip()
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ").strip()
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("\n=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ").strip()
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        contas.append(conta)
    else:
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    if not contas:
        print("\nNenhuma conta cadastrada.")
        return
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 40)
        print(textwrap.dedent(linha))

def main():
    saldo = 0
    limite = 500
    transacoes = []
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []
    print("="*40)
    print("Bem-vindo ao Banco Python!".center(40))
    print("="*40)
    while True:
        exibir_menu()
        opcao = obter_opcao()
        if opcao == "d":
            saldo = depositar(saldo, transacoes)
        elif opcao == "s":
            saldo, numero_saques = sacar(saldo, transacoes, numero_saques, limite, LIMITE_SAQUES)
        elif opcao == "e":
            exibir_extrato(transacoes, saldo)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(AGENCIA, numero_conta, usuarios, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            print("\nObrigado por usar o Banco Python. Até logo!")
            break
        else:
            print("Operação inválida! Tente novamente.")

if __name__ == "__main__":
    main()
