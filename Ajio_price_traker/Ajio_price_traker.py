import requests
from urllib.parse import urlparse
from config import *
from time import sleep


def get_ajio_product_info(product_url):
    product_id = urlparse(product_url).path.split("/p/")[1]
    url = base_url + "api/p/" + product_id
    response = requests.get(url)
    data = response.json()
    if data:
        return data, product_id
    else:
        print("Product Not Found")
        raise Exception("Product Not Found")

def send_message(telegram_token, chat_id, message):
    telegram_bot_url = f"https://api.telegram.org/{telegram_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message
    }
    telegram_data = requests.get(telegram_bot_url, params)
    if telegram_data.status_code == 200:
        print("Success")
        exit(0)
    else:
        print("Error")
        exit(1)


def Ajio_tracker(time=1*60*60):
    """time: default tracker for every One Hour"""

    url = input("Enter Ajio Product URL:")
    expected_price = int(input("Enter Expected Price: "))

    while True:
        data, product_id = get_ajio_product_info(url)
        name = data.get("name")
        price = data.get("price", {}).get("value")

        if expected_price < price:
            print(f"Current Price {price}, Price is yet to Decrease!")
            sleep(time)
            continue

        discount = data.get("price", {}).get("discountValue")
        variant_options = data.get("variantOptions", [])
        size_list = []
        for options in variant_options:
            size = options.get("scDisplaySize")
            size_list.append(size)

        message = f"""
        URL : {base_url + product_id},
        Name : {name},
        Price : INR {price},
        Discount at : {discount}%,
        Available Size : {",".join(size_list)}
        """
        send_message(telegram_token=telegram_token,
                     chat_id=chat_id, message=message)
        

if __name__ == '__main__':
    Ajio_tracker(60) # Check for every 1 min
