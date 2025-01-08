from bs4 import BeautifulSoup
from fastapi import FastAPI, Query
from fastapi.responses import PlainTextResponse
from pond import PooledObject
import pond
from tools.web_to_markdown import convert_to_markdown, fetch_web_page, convert_api_data_to_markdown
from tools.lex_pgepa_api import fetch_article, pesquisa_lei_por_ano_numero
from core.pooled_driver import build_driver_pool, web_driver_factory
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

app = FastAPI()

@app.get("/convert-url-to-markdown", response_class=PlainTextResponse)
def convert_url_to_markdown(url: str = Query(..., description="URL of the web page to convert")):
    """API endpoint to convert URL content to Markdown using a GET request."""
    html_content = fetch_web_page(url)
    
    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    main_content = soup.body if soup.body else soup
    
    markdown_content = convert_to_markdown(str(main_content))
    return markdown_content

@app.get("/convert-article-to-markdown", response_class=PlainTextResponse)
def convert_article_to_markdown(article_id: str = Query(..., description="Article ID to convert")):
    """API endpoint to convert article content from API to Markdown using a GET request."""
    api_data = fetch_article(article_id)
    
    if api_data:
        markdown_content = convert_api_data_to_markdown(api_data)
        if markdown_content:
            return markdown_content
        else:
            return "Failed to convert API data to Markdown"
    else:
        return "Failed to fetch article data from API"

@app.get("/lexpge-pa-pesquisar", response_class=PlainTextResponse)
def pesquisa_legx_pge(numero: str = Query(..., description="numero"), ano: str = Query(..., description="Ano da legislacao")):
    """API endpoint to convert article content from API to Markdown using a GET request."""
    api_data = pesquisa_lei_por_ano_numero(numero, ano)
    
    if api_data:
        markdown_content = convert_api_data_to_markdown(api_data)
        if markdown_content:
            return markdown_content
        else:
            return "Failed to convert API data to Markdown"
    else:
        return "Failed to fetch article data from API"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3001)

# if __name__ == "__main__":
#     # factory = PooledDogFactory(pooled_maxsize=10, least_one=False)
#     driver_pool = build_driver_pool()
#     pooled_object: PooledObject = driver_pool.borrow(web_driver_factory)

#     for i in range(0, 20):
#         driver = pooled_object.use()
#         driver.get("http://lex.pge.pa.gov.br/atos/view/2290")
#         body = driver.find_element(By.TAG_NAME, "body")
#         print(body.text)
#         driver_pool.recycle(driver, web_driver_factory)

#     driver_pool.clear(factory=web_driver_factory)
