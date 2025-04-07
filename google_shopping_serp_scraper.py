from crawlbase import CrawlingAPI
from bs4 import BeautifulSoup
import json

# Initialize CrawlingAPI with your access token
crawling_api = CrawlingAPI({'token': 'CRAWLBASE_TOKEN'})

options = {
    'country': 'US',  # Adjust the country code as needed
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    'page_wait': 5000
}

def scrape_google_shopping(url):
    response = crawling_api.get(url, options)
    if response['headers']['pc_status'] == '200':
        html_content = response['body'].decode('utf-8')
        soup = BeautifulSoup(html_content, 'html.parser')

        products = []
        for item in soup.select('.sh-dgr__grid-result'):
            title = item.select_one('h3.tAxDx').text.strip() if item.select_one('h3.tAxDx') else None
            price = item.select_one('span.a8Pemb.OFFNJ').text.strip() if item.select_one('span.a8Pemb.OFFNJ') else None
            image = item.select_one('div.FM6uVc > div.ArOc1c > img')['src'] if item.select_one('div.FM6uVc > div.ArOc1c > img') else None
            retailer = item.select_one('.aULzUe.IuHnof').text.strip() if item.select_one('.aULzUe.IuHnof') else None
            product_url = 'https://www.google.com' + item.select_one('a.Lq5OHe')['href'] if item.select_one('a.Lq5OHe') else None

            products.append({
                'title': title,
                'price': price,
                'image': image,
                'retailer': retailer,
                'product_url': product_url
            })
        return products
    else:
        print(f"Failed to fetch the page. Status code: {response['headers']['pc_status']}")
        return []

def scrape_multiple_pages(base_url, pages=3):
    all_products = []
    for page in range(pages):
        start_index = page * 20
        paginated_url = f"{base_url}&start={start_index}"
        products = scrape_google_shopping(paginated_url)
        all_products.extend(products)
    return all_products

def save_to_json(data, filename='products.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

url = 'https://www.google.com/search?q=louis+vuitton+bags&tbm=shop&num=20'
all_products = scrape_multiple_pages(url, pages=3)

if all_products:
  save_to_json(all_products)