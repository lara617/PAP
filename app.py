# app.py
from flask import Flask, render_template, request, jsonify, url_for
# importa as funções do db_service
from services.db_service import save_or_update_user_profile, save_questionario
# importa gerar_profissoes se ainda precisares da IA
from services.ai_service import gerar_profissoes

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('index.html')

@app.route("/questionario")
def questionario():
    return render_template("questionario.html")

@app.route("/save_questionario", methods=["POST"])
def save_questionario_route():
    data = request.get_json()
    user_id = data.get("user_id")
    answers = data.get("answers")
    if user_id and answers:
        save_questionario(user_id, answers)
        return jsonify({"status": "ok"}), 200
    return jsonify({"status": "error"}), 400


@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

# API que recebe o questionário em JSON
@app.route('/api/questionario', methods=['POST'])
def api_questionario():
    payload = request.get_json()
    if not payload:
        return jsonify({'error': 'JSON body required'}), 400

    user_id = payload.get('user_id') or payload.get('uid')
    if not user_id:
        return jsonify({'error': 'user_id missing'}), 400

    # Extrai informações pessoais (nome, genero, data_nasc, etc.) se existirem
    personal_keys = [
        'nome', 'genero', 'data_nasc', 'idade', 'formacao', 'email',
        'telefone', 'objetivo_profissional', 'preferencia_geografica'
    ]
    profile_data = {k: payload[k] for k in personal_keys if k in payload and payload[k] not in (None, '')}

    try:
        # Guarda/atualiza perfil (merge)
        if profile_data:
            save_or_update_user_profile(user_id, profile_data)

        # Guarda questionário completo
        save_questionario(user_id, payload)

        # Opcional: gerar profissões com AI (se quiseres usar já)
        # resultado = gerar_profissoes(payload)  # se a função espera o payload
        # podes guardar resultado também se quiseres

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'status': 'ok', 'redirect': url_for('chat')}), 200


if __name__ == '__main__':
    app.run(debug=True)
