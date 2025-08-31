import textwrap
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional

# ========== ENTIDADES BÁSICAS ==========
class Cliente(ABC):
    """Classe base para todo cliente."""
    def __init__(self, endereco: str):
        self.endereco = endereco
        self.contas: List["Conta"] = []

    def realizar_transacao(self, conta: "Conta", transacao: "Transacao") -> None:
        transacao.registrar(conta)

    def adicionar_conta(self, conta: "Conta") -> None:
        self.contas.append(conta)

    def __str__(self):
        return f"Cliente(endereco={self.endereco}, contas={len(self.contas)})"

class PessoaFisica(Cliente):
    """Cliente pessoa física."""
    def __init__(self, nome: str, data_nascimento: str, cpf: str, endereco: str):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

    def __str__(self):
        return f"PessoaFisica(nome={self.nome}, cpf={self.cpf})"

# ========== CONTA E HISTÓRICO ==========

class Historico:
    """Armazena as transações realizadas na conta."""
    def __init__(self):
        self._transacoes: List[dict] = []

    @property
    def transacoes(self) -> List[dict]:
        return self._transacoes

    def adicionar_transacao(self, transacao: "Transacao"):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

class Conta(ABC):
    """Classe base de conta bancária."""
    def __init__(self, numero: int, cliente: Cliente):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente: Cliente, numero: int) -> "Conta":
        conta = cls(numero, cliente)
        cliente.adicionar_conta(conta)
        return conta

    @property
    def saldo(self) -> float:
        return self._saldo

    @property
    def numero(self) -> int:
        return self._numero

    @property
    def agencia(self) -> str:
        return self._agencia

    @property
    def cliente(self) -> Cliente:
        return self._cliente

    @property
    def historico(self) -> Historico:
        return self._historico

    @abstractmethod
    def sacar(self, valor: float) -> bool:
        pass

    def depositar(self, valor: float) -> bool:
        if valor > 0:
            self._saldo += valor
            print("\n✅ Depósito realizado com sucesso!")
            return True
        print("\n❌ Operação falhou! O valor informado é inválido.")
        return False

    def __str__(self):
        return (
            f"Agência: {self.agencia}\n"
            f"C/C:     {self.numero}\n"
            f"Titular: {self.cliente.nome}"
        )

class ContaCorrente(Conta):
    """Conta corrente, com limite de saque."""
    LIMITE_PADRAO = 500
    SAQUES_LIMITE_PADRAO = 3

    def __init__(self, numero: int, cliente: Cliente, limite: float = LIMITE_PADRAO, limite_saques: int = SAQUES_LIMITE_PADRAO):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor: float) -> bool:
        numero_saques = len([
            t for t in self.historico.transacoes
            if t["tipo"] == "Saque"
        ])
        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques
        excedeu_saldo = valor > self.saldo
        if excedeu_limite:
            print("\n❌ Operação falhou! O valor do saque excede o limite da conta.")
        elif excedeu_saques:
            print("\n❌ Operação falhou! Número máximo de saques excedido.")
        elif excedeu_saldo:
            print("\n❌ Operação falhou! Saldo insuficiente.")
        elif valor > 0:
            self._saldo -= valor
            print("\n✅ Saque realizado com sucesso!")
            return True
        else:
            print("\n❌ Operação falhou! O valor informado é inválido.")
        return False

# ========== ABSTRAÇÃO DE TRANSAÇÃO ==========
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta: Conta):
        pass

class Saque(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta: Conta):
        sucesso = conta.sacar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta: Conta):
        sucesso = conta.depositar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)

# ========== FUNÇÕES DE UI E GERENCIAMENTO ==========

def menu():
    menu = """\n
    ================ MENU ================
    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q]  Sair
    => """
    return input(textwrap.dedent(menu))

def filtrar_cliente(cpf: str, clientes: List[Cliente]) -> Optional[PessoaFisica]:
    for cliente in clientes:
        if isinstance(cliente, PessoaFisica) and cliente.cpf == cpf:
            return cliente
    return None

def escolher_conta(cliente: Cliente) -> Optional[Conta]:
    if not cliente.contas:
        print("\n❗ Este cliente não possui contas.")
        return None
    if len(cliente.contas) == 1:
        return cliente.contas[0]
    print("\nEste cliente possui múltiplas contas:")
    for i, conta in enumerate(cliente.contas, 1):
        print(f"{i}: {conta}")
    while True:
        try:
            escolha = int(input("Informe o número da conta desejada: "))
            if 1 <= escolha <= len(cliente.contas):
                return cliente.contas[escolha - 1]
            else:
                print("Escolha inválida!")
        except ValueError:
            print("Entrada inválida, tente novamente.")

def depositar(clientes: List[Cliente]):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n❌ Cliente não encontrado!")
        return
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)
    conta = escolher_conta(cliente)
    if not conta:
        return
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes: List[Cliente]):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n❌ Cliente não encontrado!")
        return
    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)
    conta = escolher_conta(cliente)
    if not conta:
        return
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes: List[Cliente]):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n❌ Cliente não encontrado!")
        return
    conta = escolher_conta(cliente)
    if not conta:
        return
    print("\n================ EXTRATO ================")
    extrato = ""
    transacoes = conta.historico.transacoes
    if not transacoes:
        extrato += "Nenhuma movimentação registrada."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['data']} - {transacao['tipo']}: R$ {transacao['valor']:.2f}"
    print(extrato)
    print(f"\nSaldo atual: R$ {conta.saldo:.2f}")
    print("==========================================")

def criar_cliente(clientes: List[Cliente]):
    cpf = input("Informe o CPF (somente números): ")
    if not cpf.isdigit() or len(cpf) != 11:
        print("\n❌ CPF inválido! Deve conter 11 dígitos numéricos.")
        return
    if filtrar_cliente(cpf, clientes):
        print("\n❌ Já existe cliente com esse CPF!")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    cliente = PessoaFisica(nome, data_nascimento, cpf, endereco)
    clientes.append(cliente)
    print("\n✅ Cliente criado com sucesso!")

def criar_conta(numero_conta: int, clientes: List[Cliente], contas: List[Conta]):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n❌ Cliente não encontrado. Encerrando criação de conta.")
        return
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    print("\n✅ Conta criada com sucesso!")

def listar_contas(contas: List[Conta]):
    if not contas:
        print("\n⚠️ Nenhuma conta cadastrada até o momento.")
    for conta in contas:
        print("=" * 50)
        print(conta)

# ------------- Main Loop -------------
def main():
    clientes: List[Cliente] = []
    contas: List[Conta] = []
    while True:
        opcao = menu()
        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            print("\n👋 Obrigado por utilizar nosso sistema! Até a próxima.")
            break
        else:
            print("\n❗ Operação inválida, tente novamente.")

if __name__ == "__main__":
    main()
