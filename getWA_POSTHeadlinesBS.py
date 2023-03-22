from bs4 import BeautifulSoup
import requests

from Headlines import Headline

def getLinks():
    results = []
    url = "https://www.washingtonpost.com/"

    request = requests.get(url)
    doc = BeautifulSoup(request.text,"html.parser")

    headlines = doc.find_all("div",{"data-feature-id":"homepage/story"})

    for headline in headlines:
        # print("TEXT: ################################################")
        try:
            headlinetext = headline.find("h2").text
            links = headline.find_all("a")
            link = links[0]["href"]

            by = headline.find("div", class_="byline gray-dark font-xxxxs pb-xs").text

            # print(by)
            results.append(Headline("Washington Post", link, headlinetext,author = by))

        except:
            continue
    return results

