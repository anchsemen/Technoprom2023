from get_urls import get_urls
from data_scraper import data
from excel_manager import write_data

data_projects, urls = [], get_urls()
for url in urls:
    data_projects.extend(data(url))
write_data(data_projects)
