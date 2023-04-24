class User:
    
    def __init__(self, nome, cpf, email, telefone, endereco, dataNascimento):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.dataNascimento = dataNascimento
    
    def consultar(self):
        print("Nome:" ,self.nome, "CPF:" ,self.cpf,"e-mail: ", self.email, "Fone: ", self.telefone, "Endereco ", self.endereco,"D.N: ", self.dataNascimento)
    