from app import app
from flask import render_template, request, redirect, url_for, flash
from app.form import CadastroAlunoForm
from app.controllerAluno import AlunoController

@app.route('/')
@app.route('/index')
def homepage():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/cadastro-alunos', methods=['GET', 'POST'])
def cadastro_alunos():
    """Rota para cadastro de alunos - Recebe GET e POST"""
    form = CadastroAlunoForm()
    mensagem = None
    
    if form.validate_on_submit():
        # Adiciona o aluno através do controlador
        AlunoController.adicionar_aluno(
            nome=form.nome.data,
            email=form.email.data,
            idade=form.idade.data,
            sexo=form.sexo.data,
            matricula=form.matricula.data,
            cpf=form.cpf.data
        )
        
        mensagem = f"Aluno {form.nome.data} cadastrado com sucesso!"
        form = CadastroAlunoForm()  # Limpa o formulário
    
    return render_template('cadastro_alunos.html', form=form, mensagem=mensagem)

@app.route('/listagem-alunos')
def listagem_alunos():
    """Rota para listagem de alunos cadastrados"""
    alunos = AlunoController.obter_alunos_como_dicionario()
    return render_template('listagem_alunos.html', alunos=alunos)