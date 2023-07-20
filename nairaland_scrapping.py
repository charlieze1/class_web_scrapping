import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs"
raw_html = requests.get(url)
# print("raw_html",raw_html)

soup = BeautifulSoup(raw_html.text,"html.parser")
# print("soup",soup)

div = soup.findAll('h1')
# print("div", div)
obi = soup.find(id="ResultsContainer")
print("get by id", id)

ada = obi.findAll("h2", {"class":"title is-5"})
# for i in ada:
#     print(i.text)
# print(ada)

python_jobs = soup.find_all("h2", string=lambda text: "officer" in text.lower())
# for i in python_jobs:
#     print(i.text)
    
footer = obi.find("footer").findAll("a")

# print(python_jobs)