import requests
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup

MAIN_LINK = 'https://datos.cdmx.gob.mx/dataset/afluencia-diaria-de-metrobus-cdmx'


def download_data(link_path: str = "www.google.com", i: int = 0) -> str:
    """Downloads data from the given link and saves it to a file.

    Args:
        link_path (str, optional): The path to the link to download the data from. Defaults to "www.google.com".
        i (int, optional): The file number.. Defaults to 0.

    Returns:
        str: A string "Ok".
    """
    download_link = link_path.get('href')
    print(download_link)
    parsed_url = urlparse(download_link)
    path = parsed_url.path
    file_name = Path(path).name

    print(f"Downloading file number {i+1}: {download_link}")

    # Get response object for link
    response = requests.get(download_link)

    # Write content in pdf file
    with open(f"{file_name}", 'wb') as csv:
        csv.write(response.content)

    print(f"File {i+1}: {file_name} downloaded")

    return "Ok"


if __name__ == "__main__":

    # Making a GET request
    r = requests.get(MAIN_LINK)

    soup = BeautifulSoup(r.text, 'html.parser')

    # Find all hyperlinks present on the webpage
    links = soup.find_all('a')

    i = 0

    # Check for CSV and JSON links
    for link in links:
        if ('.csv' in link.get('href', [])):
            result = download_data(link_path=link, i=i)
            if result == "Ok":
                i += 1
                print("CSV Downloaded")
            else:
                print("Error in CSV")

        if ('.json' in link.get('href', [])):
            download_data(link_path=link, i=i)
            if result == "Ok":
                i += 1
                print("JSON Downloaded")
            else:
                print("Error in JSON")
