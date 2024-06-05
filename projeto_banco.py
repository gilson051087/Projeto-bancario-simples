menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    
 """

saldo = 0
limite = 500
extrato= ""
numeros_saques = 0
LImite_saques = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))


        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou o valor informado é invalido. ")

    elif opcao =="s":
        valor = float(input("Informe o valor do saque"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numeros_saques >= LImite_saques

        if excedeu_saque:
            print("operação falhou! Você não tem saldo suficiente. ")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite. ")


        elif excedeu_saque:
            print("Operação falhou! Número máximo de saques excedido. ")


        elif valor > 0:
            saldo += valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numeros_saques += 1

        else:
            print("Operação falhou! O valor informado é invalido. ")

    elif opcao == "e":
        print("\n=============== EXTRATO ===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("=========================================")

    elif opcao =="q":
        break

    else:
        print("operação invalida. por favor selecione novamente a operação desejada. ")