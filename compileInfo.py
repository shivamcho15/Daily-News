import getFTHeadlinesBS
import getNYTHeadlinesBS
import getSFCHeadlinesBS
import getWA_POSTHeadlinesBS
# import getWSJHeadlines
from bs4 import BeautifulSoup


def getEmail():
    letters = {"a": getFTHeadlinesBS.getLinks(), "b": getNYTHeadlinesBS.getLinks(), "c": getSFCHeadlinesBS.getLinks(),
               "d": getWA_POSTHeadlinesBS.getLinks()}

    with open("index.html", "r") as f:
        doc = BeautifulSoup(f, "html.parser")

        for letter in "abcd":
            for number in "12345":
                # print(len(letters[letter]))
                headline = letters[letter][int(number) - 1]

                h3 = doc.find(class_=f"{letter}{number}")

                h3.string = headline.mainLine +( " 🕓 " + headline.time_to_read if headline.time_to_read else "")

                h3.find_parent()["href"] = headline.link

        with open("test.html", "w") as test:
            test.write(doc.prettify())


