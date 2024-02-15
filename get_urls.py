from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = 'https://priority2030.ru/analytics'
driver = webdriver.Chrome()
driver.get(url)

wait = WebDriverWait(driver, 10)
button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Смотреть еще']")))

while True:
    try:
        button.click()
        wait.until_not(EC.visibility_of_element_located((By.XPATH, "//div[@class='loader']")))
    except:
        break

html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, 'html.parser')
urls = [f"https://priority2030.ru{url.get('href')[:-6]}program" for url in soup.find_all('a', class_='list-item')]

def get_urls():
    return urls
