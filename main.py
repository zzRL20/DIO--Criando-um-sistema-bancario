menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 1000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 5

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Quanto você quer depositar? \n"))

        if valor > 0: 
            saldo += valor 
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: \n"))

        excedeu_saldo = valor > saldo

        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        excedeu_limite = valor > limite

        if excedeu_saldo:
            print("Operação falhou! \nVocê não possui saldo suficiente.")

        elif excedeu_saques:
            print("Operação falhou! \nNúmero máximo de saques excedido.")
            
        elif excedeu_limite:
            print("Operação falhou! \nO valor do saque superou o limite.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n=============================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione umas das operações que deseja.")