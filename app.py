from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    resultado = None

    if request.method == "POST":

        consumo = float(request.form["consumo"])
        conta = float(request.form["conta"])

        # quantidade de placas
        placas = math.ceil(consumo / 50)

        # custo médio
        custo = placas * 3000

        # economia máxima
        economia_mensal = conta * 0.90

        # economia anual
        economia_anual = economia_mensal * 12

        # retorno do investimento
        retorno = custo / economia_anual

        resultado = {
            "placas": placas,
            "custo": round(custo, 2),
            "economia_mensal": round(economia_mensal, 2),
            "economia_anual": round(economia_anual, 2),
            "retorno": round(retorno, 1)
        }

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)