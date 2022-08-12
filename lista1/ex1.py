# 1 - Crie uma função que receba como função uma lista com valores de qualquer tipo. A função deve imprimir todos os elementos da lista numerando-os.

def imprimeLista(x):
    lista=[]
    x = 1
    while len(lista) < tamanho:
        item = input("Digite o que quer adicionar na lista: ")
        lista.append(item)
        x+= 1
    for number, item in enumerate(lista):
        print(number+1, ":", item)

tamanho = int(input ("digite um tamanho para a lista: "))
imprimeLista(tamanho)
