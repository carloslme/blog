from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests
from pathlib import Path
import json


MAIN_LINK = 'https://datos.cdmx.gob.mx/dataset/inmuebles-catalogados'

r = requests.get(MAIN_LINK)

soup = BeautifulSoup(r.text, 'html.parser')

all_links = soup.find_all('a')

i = 0
  
for link in all_links:
    if ('.csv' in link.get('href', [])):
        
        download_link = link.get('href')
        print(download_link)
        parsed_url = urlparse(download_link)
        path = parsed_url.path
        file_name = Path(path).name
        
        print(f"Downloading file number {i+1}: {download_link}")
        
        response = requests.get(download_link)

        with open(f"{file_name}", 'wb') as csv:
            csv.write(response.content)

        print(f"File {i+1}: {file_name} downloaded")
        
        i += 1

    if ('.json' in link.get('href', [])):
        
        download_link = link.get('href')
        print(download_link)
        parsed_url = urlparse(download_link)
        path = parsed_url.path
        file_name = Path(path).name
        
        print(f"Downloading file number {i+1}: {download_link}")
        
        response = requests.get(download_link)

        with open(f"{file_name}", 'wb') as csv:
            csv.write(response.content)

        print(f"File {i+1}: {file_name} downloaded")
        
        i += 1
