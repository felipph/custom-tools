from bs4 import BeautifulSoup
from fastapi import FastAPI, Query
from fastapi.responses import PlainTextResponse
from tools.web_to_markdown import convert_to_markdown,  fetch_web_page

app = FastAPI()
@app.get("/convert-url-to-markdown", response_class=PlainTextResponse )
def convert_url_to_markdown(url: str = Query(..., description="URL of the web page to convert")):
    """API endpoint to convert URL content to Markdown using a GET request."""
    html_content = fetch_web_page(url)
    
    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    main_content = soup.body if soup.body else soup
    
    markdown_content = convert_to_markdown(str(main_content))
    return markdown_content

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3001)