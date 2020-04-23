import os
import time
from sys import platform
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from mvideo import settings
from parse.models import Comp


def parse_comp(count):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(
        executable_path=get_chrome_driver_path(),
        options=options)
    driver.set_window_size(1120, 1000)

    url = 'https://www.mvideo.ru/komputernaya-tehnika-4107/sistemnye-bloki-80'
    driver.get(url)
    time.sleep(2)

    last_button_group = driver.find_elements_by_class_name('pagination__btn-group')[1]
    last_button = last_button_group.find_element_by_class_name("button")
    last_a = last_button.find_element_by_class_name('pagination__link')
    page_count = int(str.replace(last_a.text," ",""))
    print("Всего страниц:", page_count)

    comps = []
    print('parsing...')
    time.sleep(2)
    if count == 0:
        count = page_count * 12

    for page in range(1,page_count+1):
        print("Страница: ", page, '/', page_count)
        if page > 2:
            url = 'https://www.mvideo.ru/komputernaya-tehnika-4107/sistemnye-bloki-80?page='+str(page)
            driver.get(url)
            time.sleep(2)

        blocks = driver.find_elements_by_class_name("product-grid-card")
        i = (page - 1) * 12
        for block in blocks:
            i += 1
            time.sleep(3)

            image = block.find_element_by_class_name("product-picture__picture").get_attribute("src")
            name = block.find_element_by_class_name("product-title").text
            price_text = block.find_element_by_class_name("price-block__price").text
            try:
                price = int(str.replace(str.replace(price_text, "¤", "")," ", ""))
            except NoSuchElementException:
                price = 0

            comps.append(Comp(image=image, name=name, price=price))
            print ('#',str(i),'/',str(count))
            print('picture',image)
            print('name',name)
            print('price',price)
            if (len(comps) >= count):
                break
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