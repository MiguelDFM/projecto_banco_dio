menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[z] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
      valor = float(input("Digíte o valor do depósito: "))
      
    if valor > 0:
          saldo += valor
          extrato += f'Depósito: R$ {valor: .2f}\n'
    else:
          print("Operação falhou! Valor inválido. Tente de novo!")

    if opcao == 's':

        valor = float(input("Qual o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES
      
    if excedeu_saldo:
        print("Operação falhou! Não possui saldo sufuciente.")

    elif excedeu_limite:
        print("Operação falhou! O saque excedeu o limite.")
      
    elif excedeu_saques:
        print("Operação falhou! O Número de saques foi excedido.")

    elif valor > 0:
        saldo -= valor

        extrato += f'Saque: R$ {valor: .2f}\n'

        numero_saques += 1

    else: 
        print("Operação falhou! O valor informado é inválido.")

    if opcao == "e":

        print("\n=============EXTRATO==============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("===============================")        

    elif opcao =="z":
          break
    else:
        print("Operação inválida, por favor selecione de novo uma operação possível."
