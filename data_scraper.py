from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os


def data(url):
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        wait = WebDriverWait(driver, 20)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h2.constructor-title._visually-h3.program-wrapper-item__component')))
        html = driver.page_source
        driver.quit()
    except:
        driver = webdriver.Chrome()
        driver.get(url)
        wait = WebDriverWait(driver, 20)
        wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'h2.constructor-title._visually-h3.program-wrapper-item__component')))
        html = driver.page_source
        driver.quit()

    soup = BeautifulSoup(html, 'html.parser')

    university = soup.find('div', class_='organization-program__name').text.strip()
    elements_1 = soup.find_all('div', class_='program-wrapper-item')

    first_element, second_element = '', ''
    for element in elements_1:
        if 'Стратегические проекты, направленные на достижение целевой модели' in str(element):
            first_element = element
        elif 'Описание консорциума' in str(element):
            second_element = element
            break

    siblings = first_element.find_next_siblings(until=second_element)
    fragment = [sibling for sibling in siblings if sibling != second_element]

    unique_texts = set()
    unique_fragments = []
    for sub_fragment in fragment:
        text = sub_fragment.text
        if text not in unique_texts:
            unique_texts.add(text)
            unique_fragments.append(sub_fragment)

    file_path = 'fragment.html'

    with open(file_path, 'w', encoding='utf-8') as file:
        for sub_fragment in unique_fragments:
            file.write(sub_fragment.prettify())

    with open(file_path, 'r', encoding='utf-8') as file:
        html_1 = file.read()

    soup = BeautifulSoup(html_1, 'html.parser')
    header_elements = soup.find_all('div', class_='program-wrapper-item__head')
    title_elements = [header.find('div', class_='program-wrapper-item__title _visually-h4').text.strip() for header in
                      header_elements if header.find('div', class_='program-wrapper-item__title _visually-h4')]

    description_elements, target_elements, task_elements, exp_res_elements = [], [], [], []
    temp_el = soup.find_all('div', class_='program-wrapper-item')
    for el in temp_el:
        head = el.find('div', class_='program-wrapper-item__title').text.strip()
        content = el.find('div', class_='program-wrapper-item__component html-content constructor-content').get_text(
            strip=True)
        if head == 'Цель стратегического проекта':
            target_elements.append(content)
        elif head == 'Задачи стратегического проекта':
            task_elements.append(content)
        elif head == 'Ожидаемые результаты стратегических проектов':
            exp_res_elements.append(content)
        elif head == 'Описание стратегического проекта':
            description_elements.append(content)

    data_university = [(university if i == 0 else '', url if i == 0 else '', title_elements[i], description_elements[i],
                        target_elements[i], task_elements[i], exp_res_elements[i]) for i in range(len(title_elements))]

    return data_university
