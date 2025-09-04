# Importing the Required Libraries
import requests
from bs4 import BeautifulSoup

# Creating a Webscraping Bot Class
class WebScraper:

    # Initialization Class
    def __init__(self, link):
        self.link = link
        
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.5'
        }

        # Creating an Empty Product Details Dictionary
        self.product_details = {}
    
    # A method that gets the product details of the website
    def get_product_details(self) -> dict:        

        # Gets the Product Page Content and Create a Soup
        page = requests.get(self.link, headers=self.headers)
        soup = BeautifulSoup(page.content, features='lxml')

        try:
            # Getting the Title of the Page
            title = soup.find('span', attrs={"id": "productTitle"}).get_text().strip()

            # Getting the Price of the Product
            price = soup.find('span', attrs={'class' : 'a-price-whole'}).get_text().strip() + soup.find('span', attrs={'class' : 'a-price-fraction'}).get_text().strip()

            # Adding the Info to Dictionary
            self.product_details["title"] = title
            self.product_details["price"] = price
        
        except Exception as e:
            print('Could not fetch product details')
            print(f'Failed with exception: {e}')

# Runs the Program if the Name is Main
if __name__ == "__main__":

    print()
    with open("links.txt") as file:
        links = file.readlines()
        for link in links:
            scraper = WebScraper(link=link)
            scraper.get_product_details()

            print("Product Info: ")
            print(f"  Name: {scraper.product_details["title"]}")
            print(f"  Price: ${scraper.product_details["price"]}")
            print()