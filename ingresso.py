from assento import Assento
class Ingresso(Assento):
    def _init__(self, numero, fila):
        return super()._init__(numero, fila)
    
from sessao import Sessao
class Ingrresso(Sessao):
    def __init__(self, sala, horario, duracao, quantidadeAssentos):
        super().__init__(sala, horario, duracao, quantidadeAssentos)

from filme import Filme
class Ingresso(Filme):
    def __init__(self, titulo, sinopse, genero, classificacao, elenco):
        super().__init__(titulo, sinopse, genero, classificacao, elenco)

from user import User
class Ingreso(User):
    def __init__(self, nome, cpf, email, telefone, endereco, dataNascimento):
        super().__init__(nome, cpf, email, telefone, endereco, dataNascimento)

class Ingresso:
    def __init__(self, serial, valor, Assento, Sessao, Filme, User):
        self.serial = serial
        self.valor = valor
        self.assento = Assento
        self.sessao = Sessao
        self.filme = Filme
        self.user = User
            
    def comprar(self):
        print(self.user, self.filme, self.sessao, self.assento, self.valor, self.serial)
    
    
    