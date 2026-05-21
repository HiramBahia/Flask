class Student:
    
    def __init__(self, nome, email, idade, sexo, matricula, cpf):
        self.nome = nome
        self.email = email
        self.idade = idade
        self.sexo = sexo
        self.matricula = matricula
        self.cpf = cpf
    
    def to_dict(self):
        return {
            'nome': self.nome,
            'email': self.email,
            'idade': self.idade,
            'sexo': self.sexo,
            'matricula': self.matricula,
            'cpf': self.cpf
        }
    
    def __str__(self):
        return f"Student(nome={self.nome}, email={self.email}, matricula={self.matricula})"
