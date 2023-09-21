menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))
        
        if valor > 0:
            saldo += valor
            extrato += "Deposito: R$ {:.2f} \n".format(valor)
            
        else:
            print("Operação falhou ! O valor informado é inválido. ")
    elif (opcao == "s"):
        valor = float(input("Informe o valor do saque : "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saque = numero_saques >= limite_saques
        
        if excedeu_saldo:
            print("Operação falhou ! Você não tem saldo suficiente.")
            
        elif excedeu_limite:
            print("Operação falhou ! O valor do saque excede o limite.")
            
        elif excedeu_saque:
            print("Operação falhou ! Número máximo de saques excedido.")
            
        elif valor > 0:
            saldo -= valor
            extrato += "Saque R${:.2f}\n".format(valor)
            
        else:
            print("Operação falhou ! O valor informado é inválido.")
            
    elif opcao == "e":
        print("\n EXTRATO \n")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print("Saldo R${:.2f}".format(saldo))
        
    elif opcao == "q":
        break
    
    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")