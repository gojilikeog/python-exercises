import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=software-engineer-intern&where=Bay-Area'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='SearchResults')
# print(results.prettify()) # formats HTML code
job_elems = results.find_all('section', class_='card-content')

for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    #days_elem = job_elem.find('div', class_='meta flex-col')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print('{}'.format(company_elem.text.strip()))
    print('{}'.format(location_elem.text.strip()))
    #print('      {}'.format(days_elem.text.strip()))
    link_elem = job_elem.find('a')['href']
    print("Apply here: {}".format(link_elem))
    print()

#python_jobs = results.find_all('h2', string=lambda text:'python' in text.lower())
