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
    
    for link in table:
        url_link = link.attrs['href']
        return_soup = open_a_link(url= url_link)
        
        title = return_soup.find("td", {"class": "bold l pu"}).select("a:nth-of-type("+str(4)+")")[0].text
        print(title)
        heading =return_soup.find("td", {"class": "bold l pu"}).text
        body = return_soup.find("blockquote").text
        
        f = open(title.replace("?","")+".txt", 'a', encoding='utf-8')
        f.write(str(heading))
        f.write("\n")
        f.write(str(body))
        f.close()
        


    
    # f = open("data.txt", 'a', encoding='utf-8')
    # for tab in table:
    #     f.write(str(tab.text))
    #     f.write("\n")
        
    # f.close()

def open_a_link(url):
    raw_html = requests.get(url,headers=header)
    soup = BeautifulSoup(raw_html.text,"html.parser")
    return soup

    

scraping(url)
print("done")