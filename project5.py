#pip install requests beautifulsoup4 pandas

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://ecommerce-website.com/products'

response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    
    soup = BeautifulSoup(html_content, 'html.parser')

    products = soup.find_all('div', class_='product')
     
    product_names = []
    product_prices = []
    product_ratings = []
    
   
    for product in products:
        name = product.find('h2', class_='product-name').text
        price = product.find('span', class_='product-price').text
        rating = product.find('span', class_='product-rating').text
        
        product_names.append(name)
        product_prices.append(price)
        product_ratings.append(rating)
    

    df = pd.DataFrame({
        'Product Name': product_names,
        'Price': product_prices,
        'Rating': product_ratings
    })
    
    df.to_csv('products.csv', index=False)
    
    print('Product information has been saved to products.csv')
else:
    print('Failed to retrieve the web page. Status code:', response.status_code)
