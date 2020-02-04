import requests
from bs4 import BeautifulSoup


indeed_result = requests.get("https://www.indeed.com/jobs?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&as_src=&salary=&radius=25&l=&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class":"pagination"})

links = pagination.find_all('a')
pages = []
for link in links[:-1]:
  pages.append(int(link.string))

max_page = pages[-1]