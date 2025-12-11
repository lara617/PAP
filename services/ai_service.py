# services/ai_service.py
from collections import defaultdict

def analisar_respostas(respostas, questions_list):
    """
    respostas: dict {id_pergunta: valor_selecionado (1-4 ou texto)}
    questions_list: lista de todas as perguntas (com id e dimensão)
    """
    area_soma = defaultdict(int)
    area_total = defaultdict(int)

    # Percorre cada pergunta respondida
    for q in questions_list:
        qid = str(q['id'])
        valor = respostas.get(qid)
        if valor is None:
            continue  # pergunta não respondida
        dim = q['dimension']

        # Se for escala (1-4), somamos para a dimensão correspondente
        if q['type'] == "scale":
            area_soma[dim] += valor
            area_total[dim] += 4  # máximo possível para normalizar

        # Se for select ou texto, podemos ignorar para percentagem ou tratar separadamente
        # aqui só focamos nas escalas

    # Calcula percentagens
    percentagens = {}
    for dim in area_soma:
        percentagens[dim] = round((area_soma[dim] / area_total[dim]) * 100, 2)

    # Determina área de maior destaque
    top_area = max(percentagens, key=lambda k: percentagens[k])

    return {
        "percentagens": percentagens,
        "top_area": top_area
    }
