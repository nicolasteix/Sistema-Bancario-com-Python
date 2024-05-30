def menu():
    return """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

def cadastrar_usuario(nome):
    return f"Usuário cadastrado: {nome}"

def cadastrar_conta_bancaria(saldo_inicial=0, limite_inicial=500):
    return f"Conta bancária criada com saldo inicial de R$ {saldo_inicial} e limite de saque de R$ {limite_inicial}"

def depositar(saldo, valor):
    if valor > 0:
        saldo += valor
        return saldo, f"Depósito: R$ {valor:.2f}"
    else:
        return saldo, "Operação falhou O valor informado é inválido."

def sacar(saldo, limite, saques, valor):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = saques >= 3

    if excedeu_saldo:
        return saldo, "Operação falhou Você não tem saldo suficiente."
    elif excedeu_limite:
        return saldo, "Operação falhou O valor do saque excede o limite."
    elif excedeu_saques:
        return saldo, "Operação falhou Número máximo de saques excedido."
    elif valor > 0:
        saldo -= valor
        saques += 1
        return saldo, f"Saque: R$ {valor:.2f}", saques
    else:
        return saldo, "Operação falhou O valor informado é inválido."

def extrato(saldo, extrato):
    return "\n================ EXTRATO ================\n" + (extrato if extrato else "Não foram realizadas movimentações.\n") + f"\nSaldo: R$ {saldo:.2f}\n========================================="

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu())

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, mensagem = depositar(saldo, valor)
            extrato += mensagem + "\n"

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, mensagem, numero_saques = sacar(saldo, limite, numero_saques, valor)
            extrato += mensagem + "\n"

        elif opcao == "e":
            print(extrato)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    print(cadastrar_usuario("João"))
    print(cadastrar_conta_bancaria())
    main()
