from bs4 import BeautifulSoup
import requests
from Headlines import Headline

def getLinks():
    results = []

    mainLink = "https://www.sfchronicle.com"
    url = mainLink

    request = requests.get(url)
    doc = BeautifulSoup(request.text,"html.parser")

    headlines = doc.find_all("li",class_="coreHeadlineList--item card")
    mainheadline = doc.find("li",class_="coreHeadlineList--item card first")

    #headlines=[mainheadline,*headlines]
    # print(len(headlines))

    otherHeadlineTopic = doc.find("div",class_="centerpiece-tab--main-kicker hideKicker")
    otherHeadline = doc.find("div",class_="centerpiece-tab--main-headline badge")
    otherHeadlineHREF = mainLink + otherHeadline.find("a")["href"]
    otherHeadlineDesc = doc.find("div",class_="centerpiece-tab--main-blurb")
    # print(otherHeadlineHREF)

    for headline in headlines:
        link = headline.find("a")
        headlineText = link.text
        time = headline.find("span")
        if(time!=None):
            time = time.text
            # print(time)
        href = mainLink+link["href"]

        # print(href)
        if time==None:
            results.append(Headline("San Francisco Chronicles", href, headlineText  ))
        else:
            results.append(Headline("San Francisco Chronicles", href, headlineText,))
    return results