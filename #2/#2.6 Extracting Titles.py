# 2번째 def인 extract_indeed_jobs(last_page)에 soup = BeautifulSoup(result.text, "html.parser")을 추가해주고 results를 만들어서 soup.find_all을 통해 jobsearch를 해줌!
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
  for page in range(last_page):
    result = requests.get(f"{URL}start={page * LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
    print(results)
  return jobs


# <for 새로운 변수명(result) in 활요하고자 하는 변수명(results)> 을 활용해서 anchor 안에있는 title을 뽑아냄!
def extract_indeed_jobs(last_page):
  jobs = []
  # for page in range(last_page):
  result = requests.get(f"{URL}start={0 * LIMIT}")
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
  for result in results:
      title = result.find("div", {"class":"title"}).find("a")["title"]
      print(title)
  return jobs