class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco


class Conta:
    def __init__(self, usuario, saldo, contas=[], agencia="001"):
        self._agencia = agencia
        self._numero = len(contas) + 1
        for conta in contas:
            if conta._usuario.cpf == usuario.cpf:
                print("Usuário já possui uma conta cadastrada")
                return
        self._usuario = usuario
        self._saldo = saldo
        self.MAX_SAQUES = 3
        self._saques_realizados = 0
        self._operacoes = []

    def deposito(self, valor, /):
        self._saldo += valor
        self._operacoes.append(("Depósito", valor))

    def saque(self, *, valor):
        if self._saques_realizados == self.MAX_SAQUES:
            print("Limite de saques diários atingido")
        if self._saldo < valor:
            print("Saldo insuficiente")
        else:
            self._saldo -= valor
            self._saques_realizados += 1
            self._operacoes.append(("Saque", valor))

    def extrato(self, operacoes, /, *, usuario):
        print("\n--------------EXTRATO--------------")
        print(
            f"Extrato de {usuario.nome}, Agencia, {self._agencia}, Conta nº{self._numero} - Saldo: R$ {self._saldo}\n")
        if len(operacoes) == 0:
            print("Não foram realizadas movimentações.")
        else:
            for operacao in operacoes:
                print(f"{operacao[0]} de R$ {operacao[1]:.2f}")

    def menuConta(self):
        while True:
            print(f"\nBem vindo, {self._usuario.nome}")
            print("1 - Depositar dinheiro")
            print("2 - Sacar dinheiro")
            print("3 - Ver extrato")
            print("0 - Sair da conta")
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                quantidade = float(input("Digite o valor a ser depositado: "))
                self.deposito(quantidade)
            elif opcao == 2:
                quantidade = float(input("Digite o valor a ser sacado: "))
                self.saque(valor=quantidade)
            elif opcao == 3:
                self.extrato(self._operacoes, usuario=self._usuario)
            elif opcao == 0:
                print("Saindo da conta...")
                break
            else:
                print("Opção inválida")


def main():
    contasCadastradas = []  # Lista de contas
    usuario1 = Usuario("Usuário 1", "1/11/2000", 123456,
                       "Rua Abc - 123 - Bairro X - Cidade BH - Estado MG")
    contasCadastradas.append(Conta(usuario1, 500, contas=contasCadastradas))

    while True:
        print("1 - Criar conta")
        print("2 - Acessar conta")
        print("0 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            nome = input("Digite o nome do usuário: ")
            data_nascimento = input("Digite a data de nascimento do usuário: ")
            cpf = int(input("Digite o CPF do usuário, apenas os números: "))
            endereco = input(
                "Digite o endereço do usuário, separando por '-': ")
            usuario = Usuario(nome, data_nascimento, cpf, endereco)
            saldo = float(input("Digite o saldo inicial da conta: "))
            contasCadastradas.append(
                Conta(usuario, saldo, contas=contasCadastradas))
        elif opcao == 2:
            cpf = int(input("Digite o CPF do usuário, apenas os números: "))
            for conta in contasCadastradas:
                if conta._usuario.cpf == cpf:
                    conta.menuConta()
                    break
            else:
                print("Usuário não encontrado")
        elif opcao == 0:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida")


main()
