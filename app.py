from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    resultado = None

    if request.method == 'POST':

        try:
            conta = float(request.form['conta'])
            consumo = float(request.form['consumo'])
            custo_sistema = float(request.form['custo'])

            # Economia fixa de 90%
            economia = 90

            economia_mensal = conta * (economia / 100)
            economia_anual = economia_mensal * 12

            retorno_anos = custo_sistema / economia_anual

            resultado = {
                'economia_mensal': round(economia_mensal, 2),
                'economia_anual': round(economia_anual, 2),
                'retorno_anos': round(retorno_anos, 1)
            }

        except:
            resultado = 'Erro ao calcular.'

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)