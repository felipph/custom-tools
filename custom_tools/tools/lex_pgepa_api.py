import requests
from models.legislacao import Legislacao
from web_to_markdown import convert_to_markdown

def fetch_article(article_id):
    """Fetch article data from the API"""
    url = f"https://lex.pge.pa.gov.br/api/atos/{article_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching article {article_id}: {e}")
        return None
    
def pesquisa_lei_por_ano_numero(numero, ano):
    """Fetch article data from the API"""
    url = f"https://lex.pge.pa.gov.br/api/atos/busca?numero={numero}&ano={ano}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        response_json = response.json()
        if len(response_json['resultados']) > 0 :
            data = response_json['resultados'][0];
            record = Legislacao()
            record.identificador = data['id']
            record.origem = "LEXPGE_PA"
            record.palavras_chaves = data['descritores']            
            record.nome_alternativo = data['numero_formatado']+"/"+ano
            record.ementa = data['ementa']
            record.data_publicacao = data['id']
            record.tipo_legislacao = data['tipo_id']
            record.titulo = data['titulo']            
            record.conteudo = convert_to_markdown(data['conteudo'])
            return record
    except requests.exceptions.RequestException as e:
        print(f"Erro realizando pesquisa no LEXPGE/PA: {e}")
    return None
    
if __name__ == "__main__":    
    resultado = pesquisa_lei_por_ano_numero(10046,2023)
    print(resultado)
    
    
    

#https://lex.pge.pa.gov.br/api/atos/busca?numero=10046&ano=2023
