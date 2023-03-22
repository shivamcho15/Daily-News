from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from Headlines import Headline

def getLinks():
    results=[]

    options = Options()
    options.add_experimental_option("detach",True)
    options.add_argument("--headless")


    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)


    totalHeadlines=1
    maxHeadlines=3


    driver.get("https://www.wsj.com/")



    mainHeadline = driver.find_element("xpath","//div[@class='WSJTheme--headline--7VCzo7Ay ']")
    # mainHeadlineLink = mainHeadline.find_element("xpath","/a")
    print(mainHeadline.get_attribute("innerHTML"),"HI")

getLinks()