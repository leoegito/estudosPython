livro = 5
pilha = list(range(1, livro+1))
while True:
    print("\nExistem %d pratos na pilha" % len(pilha))
    print("Pilha atual:", pilha)
    print("Digite E para empilhar, D para desempilhar ou S para sair.")
    operacao = input("Operacao: E, D ou S\n")
    if operacao == "D":
        if(len(pilha)) > 0:
            desempilhado = pilha.pop(-1)
            livro -= 1
            print("Livro %d empilhado" % desempilhado)
    elif operacao == "E":
        livro += 1
        pilha.append(livro)
        # code
    elif operacao == "S":
        break
    else:
        print("Escolha uma operacao valida.")
