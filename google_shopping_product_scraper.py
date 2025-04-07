from crawlbase import CrawlingAPI
from bs4 import BeautifulSoup
import json

# Initialize CrawlingAPI with your access token
crawling_api = CrawlingAPI({'token': 'CRAWLBASE_TOKEN'})

options = {
    'country': 'FR',
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"
}

def scrape_product_page(url):
    response = crawling_api.get(url, options)
    if response['headers']['pc_status'] == '200':
        html_content = response['body'].decode('utf-8')
        soup = BeautifulSoup(html_content, 'html.parser')

        title = soup.select_one('span.sh-t__title-pdp.sh-t__title').text.strip() if soup.select_one('span.sh-t__title-pdp.sh-t__title') else None
        price = soup.select_one('span.g9WBQb').text.strip() if soup.select_one('span.g9WBQb') else None
        description = soup.select_one('p.sh-ds__desc').text.strip() if soup.select_one('p.sh-ds__desc') else None
        images = [img['src'] for img in soup.select('div.main-image > img')]

        product_details = {
            'title': title,
            'price': price,
            'description': description,
            'images': images
        }
        return product_details
    else:
        print(f"Failed to fetch the page. Status code: {response['headers']['pc_status']}")
        return None

def save_to_json(data, filename='product_details.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

product_url = 'https://www.google.com/shopping/product/10571198764600207275'
product_details = scrape_product_page(product_url)

if product_details:
    save_to_json(product_details)