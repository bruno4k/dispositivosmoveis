# 4 - Crie uma classe que defina um quadrado. O atributo a ser informado é o tamanho do lado e os métodos são mudar valor do lado, retornar valor do lado e calcular área.

class Quadrado:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def getLado(self):
        return self.largura

    def setLado(self, largura):
        self.largura = largura

    def calcularArea(self):
        self.area = self.altura*self.largura
        return self.area

if __name__ == "__main__":
    quadrado1 = Quadrado(30, 10)
    print(quadrado1.getLado())
    print(quadrado1.calcularArea())
