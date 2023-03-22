from bs4 import BeautifulSoup
import requests
from Headlines import Headline


def getLinks():
    results = []

    url = "https://www.nytimes.com/"

    request = requests.get(url)
    doc = BeautifulSoup(request.text, "html.parser")

    maxHeadlines = 5
    headlines = 0

    links = []
    url = "https://www.ft.com"
    headlineSections = doc.find_all("a",class_="css-9mylee")
    for i in range(len(headlineSections)):
        if(maxHeadlines<=headlines):
            break
        headline = headlineSections[i]
        head = headline.find("h3")

        if head==None:
            continue
        headlines+=1
        head=head.text
        href = headline.attrs["href"]
        paragraphs=headline.find_all("p")
        description = None
        time=None
        for paragraph in paragraphs:
            if "summary-class" in paragraph.attrs["class"]:
                description = paragraph.text
            else:
                time = paragraph.text
        results.append(Headline("New York Times", href, head,description,time))
    return results
    
