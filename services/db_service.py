# services/db_service.py
import os
import firebase_admin
from firebase_admin import credentials, firestore

# caminho do JSON do Admin SDK (coloca o ficheiro na raiz do projeto)
SERVICE_ACCOUNT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'projeto-pap-284ca-firebase-adminsdk-fbsvc-41e8ef91e8.json')

# Inicializa o app admin apenas uma vez
if not firebase_admin._apps:
    cred = credentials.Certificate(SERVICE_ACCOUNT)
    firebase_admin.initialize_app(cred)

db = firestore.client()

def save_or_update_user_profile(user_id: str, profile_data: dict):
    """
    Guarda ou actualiza (merge) os dados pessoais no documento users/{user_id}
    profile_data é um dicionário com campos pessoais (nome, genero, data_nasc, etc.)
    """
    if not user_id:
        raise ValueError("user_id é obrigatório")
    doc_ref = db.collection('users').document(user_id)
    # merge=True para não sobrescrever campos já existentes
    doc_ref.set(profile_data, merge=True)

def save_questionario(user_id: str, data: dict):
    """
    Salva o questionário completo em collection questionarios, documento user_id
    (substitui o que lá estiver). Adiciona timestamp.
    """
    if not user_id:
        raise ValueError("user_id é obrigatório")
    # adiciona timestamp de preenchimento
    data_to_save = dict(data)
    data_to_save['preenchido_em'] = firestore.SERVER_TIMESTAMP
    doc_ref = db.collection('questionarios').document(user_id)
    doc_ref.set(data_to_save)
