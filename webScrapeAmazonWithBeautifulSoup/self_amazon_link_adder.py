# Importing the WebScraper Class
from amazon_web_scraper import WebScraper

# Runs the Program if the Program is ran
if __name__ == "__main__":
    while True:
        # Asks User What Link Do you want to Search
        input_link = input("Enter Product URL Here or 'q' to Exit: ")

        # Exits the Program
        if input_link.lower() == "q":
            break

        try:
            # WebScraper Initialization
            ws = WebScraper(input_link)
            ws.get_product_details()

            # Prints Out the Result
            print("\n Product Info: ")
            print(f"  Name: {ws.product_details["title"]}")
            print(f"  Price: ${ws.product_details["price"]}")

        except:
            continue