from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return render_template("pagina_inicial.html")

@app.route('/contato')
def contato():
    return render_template("contato.html")

@app.route('/msgenviada')
def msgenviada():
    return render_template("msgenviada.html")

@app.route('/rota_filha')
def rotafilha():
    return render_template("rota_filha.html")