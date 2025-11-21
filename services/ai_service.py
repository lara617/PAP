import csv
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # lê o .env
openai.api_key = os.getenv("OPENAI_API_KEY")

def carregar_profissoes(area):
    caminho = f"data/profissoes_{area.lower()}.csv"
    profissoes = []
    try:
        with open(caminho, encoding="utf-8") as f:
            leitor = csv.DictReader(f, delimiter=";")
            for linha in leitor:
                profissoes.append(linha)
    except FileNotFoundError:
        print(f"Arquivo {caminho} não encontrado.")
    return profissoes

def gerar_profissoes(respostas, area=None):
    profissoes = carregar_profissoes(area) if area else []
    profissoes_texto = "\n".join([f"{p['Profissao']} ({p['Genero_Menos_Representado']}): {p['Descricao']}" for p in profissoes])
    prompt = f"""
    És um orientador profissional inclusivo.
    Perfil do utilizador: {respostas}
    Lista de profissões: {profissoes_texto}
    Sugere até 3 profissões mais compatíveis.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-mini",
            messages=[
                {"role": "system", "content": "Tu és um orientador de carreiras inclusivo."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=600
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print("Erro ao gerar profissões:", e)
        return "Erro ao gerar profissões."
