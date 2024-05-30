class Cliente:
    def __init__(self, nome):
        self.nome = nome

    def cadastrar(self):
        return f"Usuário cadastrado: {self.nome}"

class ContaBancaria:
    def __init__(self, saldo_inicial=0, limite_inicial=500):
        self.saldo = saldo_inicial
        self.limite = limite_inicial
        self.saques = 0
        self.extrato = ""

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            return self.saldo, self.extrato
        else:
            return self.saldo, "Operação falhou O valor informado é inválido."

    def sacar(self, valor):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.saques >= 3

        if excedeu_saldo:
            return self.saldo, "Operação falhou Você não tem saldo suficiente."
        elif excedeu_limite:
            return self.saldo, "Operação falhou O valor do saque excede o limite."
        elif excedeu_saques:
            return self.saldo, "Operação falhou Número máximo de saques excedido."
        elif valor > 0:
            self.saldo -= valor
            self.saques += 1
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            return self.saldo, self.extrato
        else:
            return self.saldo, "Operação falhou O valor informado é inválido."

    def extrato(self):
        return "\n================ EXTRATO ================\n" + self.extrato + f"\nSaldo: R$ {self.saldo:.2f}\n========================================="

def menu():
    return """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

def main():
    cliente = Cliente("João")
    conta = ContaBancaria()

    while True:
        print(cliente.cadastrar())
        print(conta.cadastrar_conta_bancaria())

        opcao = input(menu())

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, mensagem = conta.depositar(valor)
            print(mensagem)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, mensagem, _ = conta.sacar(valor)
            print(mensagem)

        elif opcao == "e":
            print(conta.extrato())

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
