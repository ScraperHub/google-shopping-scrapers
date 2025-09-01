<a href="https://crawlbase.com/signup?utm_source=github&utm_medium=readme&utm_campaign=crawling_api_banner" target="_blank">
  <img src="https://github.com/user-attachments/assets/afa4f6e7-25fb-442c-af2f-b4ddcfd62ab2" 
       alt="crawling-api-cta" 
       style="max-width: 100%; border: 0;">
</a>

# 🛍️ Google Shopping Scraper with Python (Crawlbase API)

## 📝 Description

This project includes two Python-based scrapers that use the [Crawlbase Crawling API]() to extract product data from Google Shopping:

- A SERP scraper to collect multiple products from the shopping search results.
- A product page scraper to extract detailed info from individual product listings.

📖 Read the full blog post here: [How to Scrape Google Shopping Data](https://crawlbase.com/blog/scrape-google-shopping-data/)

## ⚙️ Tech Stack

- [Crawlbase Crawling API](https://crawlbase.com/crawling-api/)
- requests handled internally by the SDK
- BeautifulSoup for HTML parsing
- json for structured data output

## 📦 Installation

Install the required dependencies:

```bash
pip install crawlbase beautifulsoup4
```

## 🔑 Setup

Update the script(s) with your Crawlbase token:

```python
crawling_api = CrawlingAPI({'token': 'YOUR_CRAWLBASE_TOKEN'})
```

## 🛒 Scraper 1: Google Shopping SERP Scraper (`google_shopping_serp_scraper.py`)

### ✅ What It Does

- Scrapes multiple pages of Google Shopping search results.
- Extracts:
  - **Product Title**
  - **Price**
  - **Image URL**
  - **Retailer**
  - **Product URL**

### 🧠 Pagination Strategy

Uses the `start` parameter to paginate (20 products per page).

### ▶️ How to Run

```bash
python google_shopping_serp_scraper.py
```

### 📁 Output

Saves results to:

```bash
products.json
```

#### 🧪 Sample Output

```json
[
  {
    "title": "Louis Vuitton Neverfull MM",
    "price": "$2,030.00",
    "image": "https://example.com/image.jpg",
    "retailer": "Louis Vuitton",
    "product_url": "https://www.google.com/shopping/product/123456789"
  },
  ...
]
```

## 📄 Scraper 2: Product Page Scraper (`google_shopping_product_scraper.py`)

### ✅ What It Does

Extracts detailed info from a single Google Shopping product page:

- **Title**
- **Price**
- **Description**
- **Image URLs**

### ▶️ How to Run

Update the product_url in the script, then:

```bash
python google_shopping_product_scraper.py
```

### 📁 Output

Saves details to:

```bash
product_details.json
```

#### 🧪 Sample Output

```json
{
	"title": "Louis Vuitton Neverfull MM",
	"price": "$2,030.00",
	"description": "Iconic Louis Vuitton tote with a timeless design...",
	"images": ["https://example.com/image1.jpg", "https://example.com/image2.jpg"]
}
```

## 🔒 Note on Anti-Bot Measures

Google Shopping employs strict bot protection. Using Crawlbase Crawling API ensures:

- IP rotation
- JavaScript rendering
- User-Agent spoofing
- Geo-targeting support

## ✅ To-Do

- Add CLI support for dynamic search terms and product links
- Combine both scrapers into a single flow
- Output data in CSV
