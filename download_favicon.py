import argparse
from urllib.parse import urlparse
import requests
from favicon import FaviconExtractor


def main():
    parser = argparse.ArgumentParser(description="Download a website's favicon.")
    parser.add_argument("url", help="URL of the website")
    
    args = parser.parse_args()
    url = args.url.strip('/')
    
    # Используем FaviconExtractor для поиска иконки
    extractor = FaviconExtractor(url)
    icons = extractor.get_favicons()
    
    if len(icons) > 0:
        icon_url = icons[0].url
        
        response = requests.get(icon_url)
        if response.status_code == 200:
            domain_name = urlparse(url).netloc.split('.')[-2]
            
            with open(f"{domain_name}_favicon.{icon_url.split('.')[-1]}", 'wb') as f:
                f.write(response.content)
                
            print(f"Favicon downloaded successfully for {url}")
        else:
            print(f"Failed to download favicon from {icon_url}. Status code: {response.status_code}")
    else:
        print(f"No favicon found on {url}")

if __name__ == "__main__":
    main()
