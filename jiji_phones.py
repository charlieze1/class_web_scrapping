import requests
from bs4 import BeautifulSoup

url = requests.get("https://jiji.ng/mobile-phones").text
with open("index.html", 'w', encoding='utf-8') as file:
    file.writelines(url)
    
scrape = BeautifulSoup(url, 'html')

print(scrape)

products = scrape.find_all('div', class_="h-dflex h-flex-cross-center h-flex-space-between h-pv-10")

for product in products:
    link_tag = product.find('a')
    if link_tag:
        link_url = link_tag.get('href')
    else:
        link_url = "No link URL available"
    image_tag = product.find('img')
    if image_tag:
        image_url = image_tag['src']
    else:
        image_url = "No image URL available"
    name_tag = product.find('h3')
    if name_tag:
        name = name_tag.text.strip()
    else:
        name = "No product name available"
    description_tag = product.find('div')
    if description_tag:
        description = description_tag.text.strip()
    else:
        description = "No product description available"
    price_tag = product.find('div', class_="price")
    if price_tag:
        price = price_tag.text.strip()
    else:
        price = "No product price available"

    print("Product Image URL:", image_url)
    print("Product Link URL:", link_url)
    print("Product Name:", name)
    print("Product Description:", description)
    print("Product Price:", price)
    print()