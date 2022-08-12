# 3 - Crie uma função que defina uma pessoa. Os atributos da classes são: nome, idade e endereço. Os métodos são mostrar endereço e alterar endereço

class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def getEndereco(self):
        return self.endereco

    def setEndereco(self, endereco):
        self.endereco = endereco


if __name__ == "__main__":
    pessoa1 = Pessoa("japones","22", "perto de casa")
    print(pessoa1.getEndereco())
    pessoa1.setEndereco("longe de casa")
    print(pessoa1.getEndereco())
