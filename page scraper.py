import requests
from bs4 import BeautifulSoup
import os

def fetch_html(url):
    response = requests.get(url)
    response.raise_for_status()  # Will raise an HTTPError for bad responses
    return response.text

def extract_links_and_images(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = set()  # Use a set to avoid duplicates
    images = set()  # Use a set to avoid duplicates

    for link in soup.find_all('a', href=True):
        links.add(link['href'])

    for img in soup.find_all('img', src=True):
        images.add(img['src'])

    return list(links), list(images)

def save_to_file(data, filename):
    with open(filename, 'w') as file:
        for item in data:
            file.write(f"{item}\n")

def main(url):
    print(f"Fetching content from {url}")
    html = fetch_html(url)
    
    print("Extracting links and images")
    links, images = extract_links_and_images(html)

    print(f"Found {len(links)} links and {len(images)} images")
    
    # Save to files
    save_to_file(links, 'links.txt')
    save_to_file(images, 'images.txt')

    print("Saved links to links.txt and images to images.txt")

if __name__ == "__main__":
    # Replace 'http://example.com' with the URL you want to scrape
    main('http://example.com')
