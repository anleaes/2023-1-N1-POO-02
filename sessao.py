class Sessao:
    def __init__(self, sala, horario, duracao, quantidadeAssentos):
        self.sala = sala
        self.horario = horario
        self.duracao = duracao
        self.quantidadeAssentos = quantidadeAssentos
    
    def consultar (self):
        print(self.sala, self.horario, self.duracao)

    def cadastrar(sala, horario, duracao):
        sala = sala
        horario = horario
        duracao = duracao