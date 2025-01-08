import markdownify as md
import cloudscraper
from bs4 import BeautifulSoup
from markdownify import markdownify as md

import re


def fetch_web_page(url):
    """Fetch web page content"""
    scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
    # Or: scraper = cloudscraper.CloudScraper()  # CloudScraper inherits from requests.Session
    return clear_text(scraper.get(url).text) 

def convert_to_markdown(html_content):
    """Convert HTML content to Markdown"""
    try:
        return clear_text(md(html_content))
    except Exception as e:
        print(f"Error converting HTML to Markdown: {e}")
        return None

def save_to_file(content, filename):
    """Save Markdown content to a file"""
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Content saved to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")

def convert_api_data_to_markdown(api_data):
    """Convert API data to Markdown"""
    if 'conteudo' in api_data:
        markdown_content = convert_to_markdown(api_data['conteudo'])
        if markdown_content:
            return markdown_content
        else:
            print("Failed to convert API data to Markdown")
            return None
    else:
        print("No 'content' field found in API data")
        return None

def clear_text(text):
    text = re.sub(r'\n\n+', "\n", text, flags=re.DOTALL)
    text = re.sub(r'\n\r+', "\n", text, flags=re.DOTALL)
    text = re.sub(r' +', ' ', text, flags=re.DOTALL)
    text = re.sub(r'\r', '', text, flags=re.DOTALL)
    text = re.sub(r'\t', '', text, flags=re.DOTALL)
    return re.sub(r'\\.?', '', text, flags=re.DOTALL)
