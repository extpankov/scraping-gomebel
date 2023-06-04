import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

PRINTS = True

def collect_categories(driver):
    driver.get("https://gomebel.com/shop/catalog/0/")
    soup = BeautifulSoup(driver.page_source, 'lxml')
    els = soup.find_all("li", class_=["item-with-label", "item-label-primary"])
    links = ["https://gomebel.com" + el.find("a").get("href") for el in els]
    return links

def collect_products(driver, links_categories):
    for l in range(len(links_categories)):
        driver.get(links_categories[l])
        soup = BeautifulSoup(driver.page_source, 'lxml')
        els = [el.get("href") for el in soup.find_all("a", class_=["product-image-link"])]
        with open('links.txt', 'a') as f:
            for el in els:
                f.write("https://gomebel.com" + el + "\n")

        if PRINTS:
            print(f"[+] Processed {l + 1}/{len(links_categories)} categories")

def main():
    service = Service("chromedriver/chromedriver")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service = service, options = options)
    links_categories = collect_categories(driver)
    
    start_time = time.time()
    links_products = collect_products(driver, links_categories)
    execution_time = time.time() - start_time
    print(f"Execution time: {execution_time:.6f} seconds")

    driver.close()
    driver.quit()

if __name__ == '__main__':
    main()