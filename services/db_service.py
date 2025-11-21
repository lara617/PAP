# services/db_service.py
import firebase_admin
from firebase_admin import credentials, firestore

# Caminho para o teu Firebase Admin SDK JSON
cred = credentials.Certificate("path/to/your/firebase-adminsdk.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def save_questionario(user_id, data):
    """
    Salva os dados do questionário no Firestore
    """
    doc_ref = db.collection("usuarios").document(user_id)
    doc_ref.set(data)
