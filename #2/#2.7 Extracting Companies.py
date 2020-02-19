# anchor안에 URL이 있는 회사와 없는 회사를 if else로 나눔!
# 만약 anchor 안에 URL이 있다면 None 값이 나오지 않음.
# None 값이 나온다면 anchor 안에 URL이 없기에 else로 가서 출력이 됨. 그러나 이렇게 하면 빈칸이 너무 많이 나옴.
import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pagination = soup.find("div", {"class":"pagination"})

  links = pagination.find_all('a')
  pages = []
  for link in links[:-1]:
    pages.append(int(link.string))

  max_page = pages[-1]
  return max_page

def extract_indeed_jobs(last_page):
  jobs = []
  # for page in range(last_page):
  result = requests.get(f"{URL}start={0 * LIMIT}")
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
  for result in results:
      title = result.find("div", {"class":"title"}).find("a")["title"]
      company = result.find("span", {"class":"company"})
      company_anchor = company.find("a")
      if company_anchor is not None:
        print(str(company_anchor.string))
      else:
        print(str(company.string))
  return jobs


# if, else구문을 끝내고 string.strip() << 이용해서 빈칸을 없앰!
def extract_indeed_jobs(last_page):
  jobs = []
  # for page in range(last_page):
  result = requests.get(f"{URL}start={0 * LIMIT}")
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
  for result in results:
      title = result.find("div", {"class":"title"}).find("a")["title"]
      company = result.find("span", {"class":"company"})
      company_anchor = company.find("a")
      if company_anchor is not None:
        company = str(company_anchor.string)
      else:
        company = str(company.string)
      company = company.strip()
      print(company)
  return jobs


# 최종코드, title과 company 출력하기
import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pagination = soup.find("div", {"class":"pagination"})

  links = pagination.find_all('a')
  pages = []
  for link in links[:-1]:
    pages.append(int(link.string))

  max_page = pages[-1]
  return max_page

def extract_indeed_jobs(last_page):
  jobs = []
  # for page in range(last_page):
  result = requests.get(f"{URL}start={0 * LIMIT}")
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
  for result in results:
      title = result.find("div", {"class":"title"}).find("a")["title"]
      company = result.find("span", {"class":"company"})
      company_anchor = company.find("a")
      if company_anchor is not None:
        company = str(company_anchor.string)
      else:
        company = str(company.string)
      company = company.strip()
      print(title, company)
  return jobs