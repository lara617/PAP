from flask import Flask, render_template, request, redirect, url_for
from services.ai_service import gerar_profissoes
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# 🔥 Inicializar Firebase Admin
cred = credentials.Certificate('projeto-pap-284ca-firebase-adminsdk-fbsvc-41e8ef91e8.json')
firebase_admin.initialize_app(cred)
db = firestore.client()


app = Flask(__name__)

# ------------------------
# Rotas principais
# ------------------------

@app.route('/')
def landing():
    return render_template('index.html')


@app.route("/perfil")
def perfil():
    return render_template("perfil.html")


@app.route('/questionario', methods=['GET', 'POST'])
def questionario():
    if request.method == 'POST':

        # Recebe dados do form
        data = request.form.to_dict(flat=False)
        user_id = data.pop('user_id', [None])[0]

        # Salvar no Firestore
        db.collection('questionarios').document(user_id).set(data)

        return redirect(url_for('chat'))

    return render_template('questionario.html')


@app.route('/chat')
def chat():
    return render_template("chat.html")


@app.route('/chat_process', methods=['POST'])
def chat_process():
    respostas = request.form.to_dict(flat=False)
    uid = respostas.get('user_id', [None])[0]

    resultado = gerar_profissoes(
        respostas, 
        area=respostas.get('area', [None])[0]
    )

    return render_template('chat.html', resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)
