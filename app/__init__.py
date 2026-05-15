from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua-chave-secreta-desenvolvimento'

from app.routes import homepage