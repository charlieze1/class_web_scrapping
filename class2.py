import requests
from bs4 import BeautifulSoup


header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
}

url = "https://nairaland.com"
raw_html = requests.get(url,headers=header)
soup = BeautifulSoup(raw_html.text,"html.parser")
def scraping(link):
    raw_html = requests.get(url,headers=header)
    soup = BeautifulSoup(raw_html.text,"html.parser")
    table = soup.find("td", class_="featured w").findAll("a")
    
    
    f = open("data.txt", 'a', encoding='utf-8')
    for tab in table:
        f.write(str(tab.text))
        f.write("\n") 
        # print(type(str(tab.text)))
        
        # print(tab.text)
    # print(table)
    f.close()
    

# f = open("data.txt", "a")
# f.write("hello")
# f.close()



scraping(url)
print("done")