from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange


class CadastroAlunoForm(FlaskForm):
    
    nome = StringField('Nome', validators=[DataRequired(message='Nome é obrigatório')])
    
    email = StringField('Email', validators=[
        DataRequired(message='Email é obrigatório'),
        Email(message='Email inválido')
    ])
    
    idade = IntegerField('Idade', validators=[
        DataRequired(message='Idade é obrigatória'),
        NumberRange(min=0, message='Idade não pode ser negativa')
    ])
    
    sexo = SelectField('Sexo', choices=[
        ('', 'Selecione'),
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('Outro', 'Outro')
    ], validators=[DataRequired(message='Sexo é obrigatório')])
    
    matricula = StringField('Matrícula', validators=[DataRequired(message='Matrícula é obrigatória')])
    
    cpf = StringField('CPF', validators=[DataRequired(message='CPF é obrigatório')])
    
    submit = SubmitField('Cadastrar')
