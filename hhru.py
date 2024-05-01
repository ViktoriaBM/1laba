import requests
from bs4 import BeautifulSoup

def parseVacancies():
    url = 'https://omsk.hh.ru/search/vacancy?text=Python&from=suggest_post&salary=&ored_clusters=true&employer_id=78638&area=68&hhtmFrom=vacancy_search_list&hhtmFromLabel=vacancy_search_line'
    page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(page.text, "html.parser")
    block = soup.findAll('span', class_='serp-item__title-link-wrapper')
    vacancies = []

    for data in block:
        if data.find('a'):
            vacancies.append(data.text.strip())

    return vacancies