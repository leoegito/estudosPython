ultimo = 10
fila = list(range(1, ultimo+1))
while True:
    print("\nExistem %d clientes na fila" % len(fila))
    print("Fila atual:", fila)
    print("Digite F para adicionar um cliente na fila, ou A para realizar o atendimento. S para sair.")
    operacao = input("Operacao (F, A, S): ")
    if operacao == "A":
        if(len(fila)) > 0:
            atendido = fila.pop(0)
            print("Cliente %d atentido" % atendido)
        else:
            print("Fila vazia. Ninguem para atender.")
    elif operacao == "F":
        ultimo += 1
        fila.append(ultimo)
    elif operacao == "S":
        break
    else:
        print("Opcao invalida.")
