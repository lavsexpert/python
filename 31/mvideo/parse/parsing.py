import os
import time
from sys import platform
from selenium import webdriver
from mvideo import settings
from parse.models import Comp


def parse_comp():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(
        executable_path=get_chrome_driver_path(),
        options=options)
    driver.set_window_size(1120, 1000)
    url = 'https://www.mvideo.ru/komputernaya-tehnika-4107/sistemnye-bloki-80'
    driver.get(url)

    count = 10
    comps = []
    print('parsing...')
    time.sleep(2)
    blocks = driver.find_elements_by_class_name("product-grid-card")
    i = 0
    for block in blocks:
        i += 1
        image = block.find_element_by_class_name("product-picture__picture").get_attribute("src")
        name = block.find_element_by_class_name("product-title").text
        price_text = block.find_element_by_class_name("price-block__price").text
        price = int(str.replace(str.replace(price_text, "¤", "")," ", ""))
        comps.append(Comp(image=image, name=name, price=price))
        print ('#',str(i),'/',str(count))
        print('picture',image)
        print('name',name)
        print('price_text',price)
        if (len(comps) >= count):
            break

    print('Parsing finished.')
    return comps



def get_chrome_driver_path():
    if platform == "linux" or platform == "linux2":
        # linux chromedriver
        return os.path.join(settings.BASE_DIR, 'chromedriver_linux64')
    elif platform == "darwin":
        # OS X chromedriver
        return os.path.join(settings.BASE_DIR, 'chromedriver_mac64')
    elif platform == "win32":
        # Windows chromedriver
        return os.path.join(settings.BASE_DIR, 'chromedriver_win32.exe')
        #return os.path.join(settings.BASE_DIR, 'msedgedriver.exe')