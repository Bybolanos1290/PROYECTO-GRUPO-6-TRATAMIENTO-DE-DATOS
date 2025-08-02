from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route('/')
def home():
    return jsonify({"mensaje": "API Detector de Amenazas activa"})
@app.route('/detectar', methods=['POST'])
def detectar():
    datos = request.get_json()
    texto = datos.get('texto', '')

    if texto == 'Malware':
        return jsonify({
            "mensaje": "Puertos a bloquear son: 10176,6871,19250,30804"
        })
    elif texto == 'DDOs':
        return jsonify({
            "mensaje": "Puertos a bloquear son: 12585,38787"
        })
    elif texto == 'Intrusion':
        return jsonify({
            "mensaje": "Puertos a bloquear son: 7508,34217,5094,15150,34294"
        })
    else:
        return jsonify({
            "mensaje": "Amenaza desconocida",
            "datos": datos
        })
if __name__ == '__main__':
    app.run(debug=True)