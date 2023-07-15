class conta:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
        self.MAX_SAQUES = 3
        self.saques_realizados = 0
        self.operacoes = []

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(("Depósito", valor))

    def saque(self, valor):
        if self.saques_realizados == self.MAX_SAQUES:
            print("Limite de saques diários atingido")
        if self.saldo < valor:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            self.saques_realizados += 1
            self.operacoes.append(("Saque", valor))

    def extrato(self):
        print("\n--------------EXTRATO--------------")
        if len(self.operacoes) == 0:
            print("Não foram realizadas movimentações.")
        else:
            print(f"Extrato de {self.nome} - Saldo: {self.saldo}")
            for operacao in self.operacoes:
                print(f"{operacao[0]} de R$ {operacao[1]:.2f}")


def main():
    conta1 = conta("Usuário 1", 500)
    while True:
        print(f"\nBem vindo, {conta1.nome}")
        print("1 - Depositar dinheiro")
        print("2 - Sacar dinheiro")
        print("3 - Ver extrato")
        print("0 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            valor = float(input("Digite o valor a ser depositado: "))
            conta1.deposito(valor)
        elif opcao == 2:
            valor = float(input("Digite o valor a ser sacado: "))
            conta1.saque(valor)
        elif opcao == 3:
            conta1.extrato()
        elif opcao == 0:
            print("Saindo do sistema...")
            break


main()
