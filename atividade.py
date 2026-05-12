from flask import Flask

app = Flask(__name__)


@app.route("/")
def decorate():
    return "HI!!!"


@app.route("/decorator")
def decorator():
    return "No contexto do framework web Flask (Python), os decorators são ferramentas fundamentais utilizadas para modificar o comportamento de funções, especificamente para definir rotas (URLs) que a aplicação irá atender. O uso mais comum é o @app.route(), que associa uma URL específica a uma função de visualização (view function)."


if __name__ == "__main__":
    app.run(debug=True)
