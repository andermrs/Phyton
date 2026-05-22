
from flask import Flask, render_template
import jinja2

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/alunos")
def alunos():
    lista_alunos = [
        {"nome": "Ana", "idade": 16, "nota": 5 },
        {"nome": "André", "idade": 17, "nota": 7},
        {"nome": "Bernardo", "idade": 18, "nota": 8}
    ]
    return render_template('base.html', alunos=lista_alunos)


if __name__ == "__main__":
    app.run(debug=True)
