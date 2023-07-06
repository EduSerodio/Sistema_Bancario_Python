# ----------------------------------INTRODUÇÃO---------------------------------------------
# Fomos contratados por um grande banco para desesenvolver o seu novo sistema. Esse banco 
# deseja modernizar suas operações e para isso escolheu a linguagem PYTHON. Para a primeira 
# versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

# OPERAÇÃO DE DEPÓSITO: Deve ser possível depositar valores positivos para a minha conta
# bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos
# preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos
# devem ser armazenados em uma variável e exibidos na operação extrato. 

# OPERAÇÃO DE SAQUE: O sistema deve permitir realizar 3 saques diários com limite máximo de
# R$ 500,00 por saque. Caso o usuário não tenha saldo em sua conta, o sistema deve exibir 
# uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos
# os saques devem ser armazenados em uma varável e exibidos na operação de extrato.

# OPERAÇÃO DE EXTRATO: Essa operação deve listar todos os depósitos e saques realizados na 
# conta. No fim da listagem deve ser exibido o saldo atual da conta.
# Os valores devem ser exibidos ultilizando o formato R$ xxx.xx, exemplo:
# 1500.45 = R$ 1500.45.

menu = """

[a] - SACAR
[b] - DEPOSITAR
[c] - EXTRATO
[d] - SAIR

=> """

saldo = 1500
limite_saque = 500
extrato = ""
numero_saques = 0
numero_limite_saques = 3


while True:

    opcao = input(menu)

    if opcao == "b":

        valor = float(input("Informe o valor de depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de: R$ {valor} Realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido")

       

    elif opcao == "a":
         
        valor_saque = float(input("Digite o valor que deseja sacar: "))
        
        excedeu_saldo = valor_saque > saldo

        excedeu_limite = valor_saque > limite_saque

        excedeu_saques = numero_saques >= numero_limite_saques

        if excedeu_saldo:
            print("Operação falhou! voçê não tem saldo suficiente!")
        
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite!")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido. ")

        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1
            print(f"Saque de: R$ {valor_saque} Realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")    
       
    elif opcao == "c":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============================")
    elif opcao == "d":
        print("Obrigado por usar nosso sistema! Até logo")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


    

            
