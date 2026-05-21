from app.models import Student


class AlunoController:
    
    # Atributo de classe para armazenar todos os alunos
    _alunos = []
    
    @classmethod
    def adicionar_aluno(cls, nome, email, idade, sexo, matricula, cpf):
        """
        Adiciona um novo aluno à lista
        
        Args:
            nome (str): Nome do aluno
            email (str): Email do aluno
            idade (int): Idade do aluno
            sexo (str): Sexo do aluno
            matricula (str): Número de matrícula do aluno
            cpf (str): CPF do aluno
            
        Returns:
            Student: Objeto aluno criado
        """
        novo_aluno = Student(nome, email, idade, sexo, matricula, cpf)
        cls._alunos.append(novo_aluno)
        return novo_aluno
    
    @classmethod
    def obter_todos_alunos(cls):
        """
        Retorna todos os alunos cadastrados
        
        Returns:
            list: Lista com todos os alunos
        """
        return cls._alunos
    
    @classmethod
    def obter_alunos_como_dicionario(cls):
        """
        Retorna todos os alunos como lista de dicionários
        
        Returns:
            list: Lista de dicionários com dados dos alunos
        """
        return [aluno.to_dict() for aluno in cls._alunos]
    
    @classmethod
    def limpar_alunos(cls):
        """Limpa a lista de alunos"""
        cls._alunos = []
    
    @classmethod
    def contar_alunos(cls):
        """
        Retorna a quantidade de alunos cadastrados
        
        Returns:
            int: Quantidade de alunos
        """
        return len(cls._alunos)
