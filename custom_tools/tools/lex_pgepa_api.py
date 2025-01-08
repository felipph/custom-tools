import requests

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
            return response_json['resultados'][0]
    except requests.exceptions.RequestException as e:
        print(f"Erro realizando pesquisa no LEXPGE/PA: {e}")
    return None
    
if __name__ == "__main__":    
    resultado = pesquisa_lei_por_ano_numero(10046,2023)
    print(resultado)
    
    
    

#https://lex.pge.pa.gov.br/api/atos/busca?numero=10046&ano=2023
