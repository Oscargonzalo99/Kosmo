from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)

@app.route('/ner', methods=['POST'])
def ner_extraction():
    # Cargar el modelo de spaCy para español
    nlp = spacy.load('es_core_news_sm')

    # Obtener las oraciones del JSON de la petición POST
    data = request.get_json()
    oraciones = data['oraciones']

    # Lista para almacenar las entidades nombradas identificadas en cada oración
    entidades_nombradas = []

    # Procesar cada oración
    for oracion in oraciones:
        doc = nlp(oracion)
        entidades_en_oracion = []
        for entidad in doc.ents:
            entidades_en_oracion.append((entidad.text, entidad.label_))
        entidades_nombradas.append(entidades_en_oracion)

    # Devolver la lista de entidades nombradas identificadas en cada oración
    return jsonify({'entidades_nombradas': entidades_nombradas})

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
