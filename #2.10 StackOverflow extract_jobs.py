# indeed.py와 동일하게 extract_jobs을 가져오고
# range는 int(정수)안에서만 기능하기에 
# return int(last_page)로 str을 int로 바꿔줌
import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python&sort=i"


def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("div", {"class":"s-pagination"}).find_all("a")
  last_page = pages[-2].get_text(strip=True)
  return int(last_page)


def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(page)


def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs


# 두 번째 정의 수정하기
# result를 추가함 (page + 1) 해준 것은
# 숫자가 0부터 시작하는 것을 1로 바꾸기 위함!
def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{URL}&pg={page + 1}")
    print(result.status_code)