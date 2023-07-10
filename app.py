from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form1.html')

@app.route('/process-dados', methods=['POST'])
def process():
    
    # Recebe os dados do formulario
    name = request.form.get('name')
    email = request.form.get('email')
    rg = request.form.get('rg')
    cpf = request.form.get('cpf')
    ra = request.form.get('ra')

    # Processa os dados
    result = {'name': name, 'email': email, 'rg': rg, 'cpf': cpf, 'ra': ra}
    
    dados = []

    # Retorna os resultados como um objeto JSON
    return jsonify(result)

if __name__ == '_main_':
    app.run(debug=True)