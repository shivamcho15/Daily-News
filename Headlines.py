class Headline:
    def __init__(self,site,link,mainLine,description ="",time_to_read="",author="" ):
        self.site,self.link,self.mainLine,self.description,self.time_to_read,self.author = site,link,mainLine,description,time_to_read,author
    def __str__(self):
        return f"{self.site} : {self.mainLine}"

