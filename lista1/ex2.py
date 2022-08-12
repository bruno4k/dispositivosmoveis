# 2 - Crie uma função que recebe uma lista de valores e retorna a média dos valores.

def imprimeMedia (x):
    lista=[]
    soma = 0
    media = 0.0
    while len(lista) < tamanho:
        numero = int(input("Digite o numero que quer adicionar na lista: "))
        lista.append(numero)
        soma += numero
    media = soma/tamanho
    print(soma)
    print(media)

tamanho = int(input ("digite um tamanho para a lista: "))
imprimeMedia (tamanho)
