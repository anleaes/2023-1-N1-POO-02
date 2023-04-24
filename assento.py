class Assento:
    def _init__(self, numero, fila):
        self.numero = numero
        self.fila = fila
        
    def consultar(self):
        print(self.numero, self.fila)