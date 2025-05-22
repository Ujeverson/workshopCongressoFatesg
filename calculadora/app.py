from flask import Flask, render_template, request
from operacoes.soma import soma
from operacoes.subtracao import subtracao
from operacoes.multiplicacao import multiplicacao
from operacoes.divisao import divisao
from operacoes.potencia import potencia
from operacoes.raiz_quadrada import raiz_quadrada
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    erro = None
    if request.method == 'POST':
        operacao = request.form.get('operacao')
        try:
            a = float(request.form.get('a'))
            b = request.form.get('b')
            b = float(b) if b else None
            if operacao == 'soma':
                resultado = soma(a, b)
            elif operacao == 'subtracao':
                resultado = subtracao(a, b)
            elif operacao == 'multiplicacao':
                resultado = multiplicacao(a, b)
            elif operacao == 'divisao':
                resultado = divisao(a, b)
            elif operacao == 'potencia':
                resultado = potencia(a, b)
            elif operacao == 'raiz_quadrada':
                resultado = raiz_quadrada(a)
        except Exception as e:
            erro = str(e)
    return render_template('index.html', resultado=resultado, erro=erro)

if __name__ == '__main__':
    app.run(debug=True)
