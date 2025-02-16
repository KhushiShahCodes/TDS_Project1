import os
import requests
from fastapi import HTTPException
from bs4 import BeautifulSoup

def scrape_website(url: str, base_url: str = "http://example.com"):
    """Scrapes data from the website, ensuring it's within the allowed domain."""
    # Ensure the URL is within the allowed base URL domain
    if not url.startswith(base_url):
        raise HTTPException(status_code=403, detail=f"Access to this URL {url} is forbidden")

    try:
        # Make the HTTP request to fetch the content of the website
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Example: Extract all the links (anchor tags) from the page
        links = soup.find_all('a', href=True)  # Finds all <a> tags with href attribute
        extracted_data = []
        for link in links:
            extracted_data.append(link['href'])

        return extracted_data
    
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching or parsing data: {e}")


