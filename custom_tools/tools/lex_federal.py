import re
import requests
from web_to_markdown import convert_to_markdown


def get_lei_federal(ano,numero,tipo):
    try:
        session = requests.session()
        #pesquisa lei e pega o id do documento
        response = session.get(f"https://legis.senado.leg.br/dadosabertos/legislacao/lista.json?tipo={tipo}&ano={ano}&numero={numero}")
        response.raise_for_status()
        
        docs = response.json().get("ListaDocumento").get("documentos").get("documento")
        if type(docs) is list:
            doc = docs[0]
        else:
            doc = docs
        
        id_documento = doc.get("@id")
        
        #pega os dados do documento
        response = session.get(f"https://legis.senado.leg.br/dadosabertos/legislacao/{id_documento}.json")
        response.raise_for_status()
        
        #pega a url do documento e extrai a urn
        url_documento = response.json().get("DetalheDocumento").get("documentos").get("documento").get("identificacao").get("urlDocumento")
        regex = r"https://normas\.leg\.br/\?urn=(.*)"
        matches = re.findall(regex, url_documento, re.MULTILINE)
        urn = matches[0]     
        
        #agora pegando o link para o conteudo completo
        response = session.get(f"https://normas.leg.br/api/normas?urn={urn}&tipo_documento=maior-detalhe")
        response.raise_for_status()
        #pega o corpo e converte para markdown
        response = session.get(response.json().get("encoding")[0].get("contentUrl"))
        response.raise_for_status()   
        return convert_to_markdown(response.content.decode("utf-8"))

        
    except Exception as e:
        print(f"Erro obtendo lei federal")
        return None
if __name__ == "__main__":
    print(get_lei_federal("1993","78",""))

# tipos_conhecidos = [
#     {"LCP": "Lei Complementar"},
#     {"LEI": "Lei"}
# ]

# tipo = "LCP"
# ano  = "1993"
# numero = "78"
# session = requests.session()
# response = session.get(f"https://legis.senado.leg.br/dadosabertos/legislacao/lista.json?tipo={tipo}&ano={ano}&numero={numero}")
# response.raise_for_status()
# id_documento = response.json().get("ListaDocumento").get("documentos").get("documento").get("@id")

# #https://legis.senado.leg.br/dadosabertos/legislacao/550606.json

# response = session.get(f"https://legis.senado.leg.br/dadosabertos/legislacao/{id_documento}.json")
# response.raise_for_status()

# print(response)

# url_documento = response.json().get("DetalheDocumento").get("documentos").get("documento").get("identificacao").get("urlDocumento")



# #buscando a urn


# regex = r"https://normas\.leg\.br/\?urn=(.*)"


# matches = re.findall(regex, url_documento, re.MULTILINE)

# urn = matches[0]

# #agora pegando o link para o conteudo completo
# #https://normas.leg.br/api/normas?urn=urn:lex:br:federal:lei:1993-11-10;8730&tipo_documento=maior-detalhe

# response = session.get(f"https://normas.leg.br/api/normas?urn={urn}&tipo_documento=maior-detalhe")
# response.raise_for_status()

# response = session.get(response.json().get("encoding")[0].get("contentUrl"))
# response.raise_for_status()



# print(convert_to_markdown(response.content.decode("utf-8")))

