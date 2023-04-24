class Filme:
    def __init__(self, titulo, sinopse, genero, classificacao, elenco):
        self.titulo = titulo
        self.sinopse = sinopse
        self.genero = genero
        self.classificacao = classificacao
        self.elenco = elenco
        
    def consultar(self):
        print(self.titulo, self.genero, self.classificacao)
