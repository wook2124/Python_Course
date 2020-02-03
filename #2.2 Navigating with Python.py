# requests에 대해서!
https://github.com/psf/requests


# requests를 package로 설치하고
# r(rename) = requests.get("url") 한 뒤
# html을 text로 부르는데까지 성공!
import requests

indeed_result = requests.get("https://www.indeed.com/jobs?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&as_src=&salary=&radius=25&l=&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch")

print(indeed_result.text)

# 추가로 beautifulsoup4까지 설치완료!