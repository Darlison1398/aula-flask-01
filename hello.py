from flask import Flask, render_template

app = Flask(__name__)



# passando um parâmetro na rota
@app.route("/nome/<nome>")
def nome(nome):
    return f"<h1>Olá {nome}! Seja bem-vindo</h1>"


# rota do código. as de cima eram apenas testes
@app.route("/")
def home():
    conteudo="Hello, jinja!"
    return render_template("home.html", conteudo=conteudo, x=4)
    



# comando para rodar uma aplicação flask
if __name__ == "__main__":
    app.run(debug=True)