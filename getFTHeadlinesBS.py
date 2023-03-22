from bs4 import BeautifulSoup
import requests
from Headlines import Headline

def getLinks():
    results = []
    url = "https://www.ft.com"


    request = requests.get(url)
    doc = BeautifulSoup(request.text,"html.parser")
    maxLines = 5

    # mainheadline = doc.find("div",class_="story-group-stacked__primary-story")
    #
    # mainlink =mainheadline.find_all("a")[1]
    # href = url + mainlink["href"]
    # mainHeadlineText = mainlink.text
    # mainHeadlineDesc = mainheadline.find("p").text


    headLines = doc.find_all("div",class_="story-group__article story-group__article--lead")
    lines = 0
    # print(len(headLines))
    for sideLine in headLines:
        # print("###########################################################")
        mainArea = sideLine.find("div",class_="primary-story__teaser")
        links = mainArea.find_all("a")
        try:
            mainHeadline = links[1].text
        except:
            continue
        lines +=1
        if(maxLines<lines):
            break
        href = links[1]["href"]
        if href[0:5] != "https":
            href = url + href
        #
        # print(href)
            results.append(Headline("Financial Times",href,mainHeadline))
    return results