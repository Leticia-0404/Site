from flask import Flask, render_template
from flask import request
from flask import flash
from flask import redirect

meuapp = Flask(__name__, template_folder='templates')

@meuapp.route("/")
@meuapp.route("/login")
def login():
    return render_template("login.html")


@meuapp.route("/cadastro", methods=["GET", "POST"])
def cadastro():
  return render_template("cadastro.html")



@meuapp.route("/autenticar", methods=['GET', 'POST'])
def autenticar():
    if request.method == 'POST':
        nome_usuario = request.form.get('nome_completo')
        senha = request.form.get('senha')

        # Verifica se o nome e a senha do formulário de autenticação correspondem ao nome e senha do formulário de cadastro
        if nome_usuario == nome_usuario and senha == senha:
            
            # O usuário está autenticado, então redirecionar para a página principal
            return redirect('/')
        else:
            # O usuário não está autenticado, então retornar uma mensagem de erro
            flash('Dados inválidos')
            flash('Login ou senha inválidos')
            return redirect('/login')
   

if __name__ == "__main__":
    meuapp.run(port = 8080)