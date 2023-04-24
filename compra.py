from ingresso import Ingresso

class Compra(Ingresso):
    def __init__(self, serial, valor):
        super().__init__(serial, valor)

class Compra:
    def __init__(self, tipo, quantidadeIngresso, valorTotal, Ingresso):
        self.tipo = tipo
        self.quantidadeIngresso = quantidadeIngresso
        self.valorTotal = valorTotal
        self.ingresso = Ingresso
    
    def venda(self):
        print (self.ingresso, self.valorTotal, self.tipo)
        
        