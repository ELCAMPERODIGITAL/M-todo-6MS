from flask import Flask, request, jsonify
import openai
import pdfkit

app = Flask(_name_)

# Configurar sua chave da OpenAI
openai.api_key = "SUA_CHAVE_API_OPENAI"

@app.route('/')
def index():
    return "API do Método 6MS funcionando!"

@app.route('/gerar_plano', methods=['POST'])
def gerar_plano():
    dados = request.json
    ideia = dados.get("ideia", "")
    localizacao = dados.get("localizacao", "")
    produto = dados.get("produto", "")
    distribuicao = dados.get("distribuicao", "")

    prompt = f"""
    Crie um plano de negócios completo para o seguinte empreendimento:

    - Ideia de negócio: {ideia}
    - Localização: {localizacao}
    - Tipo de produto: {produto}
    - Modelo de distribuição: {distribuicao}

    Inclua análise de mercado, concorrência, viabilidade financeira e estratégias de sucesso.
    """

    resposta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    plano = resposta["choices"][0]["message"]["content"]

    # Criar PDF do plano de negócios
    pdf_path = "/tmp/plano_de_negocios.pdf"
    pdfkit.from_string(plano, pdf_path)

    return jsonify({"plano": plano, "pdf": pdf_path})

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=10000)