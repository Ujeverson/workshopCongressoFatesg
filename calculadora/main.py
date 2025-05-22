from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operacao = request.form["operacao"]

        if operacao == "soma":
            resultado = num1 + num2
        elif operacao == "subtracao":
            resultado = num1 - num2
        elif operacao == "multiplicacao":
            resultado = num1 * num2
        elif operacao == "divisao":
            resultado = num1 / num2 if num2 != 0 else "Erro: Divisão por zero!"
        elif operacao == "potencia":
            resultado = num1 ** num2
        elif operacao == "raiz":
            resultado = num1 ** 0.5 if num1 >= 0 else "Erro: Raiz de número negativo!"

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True) 