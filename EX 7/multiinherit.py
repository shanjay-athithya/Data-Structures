class d:
    def __init__(self,title):
        self.title = title
    
class f:
    def __init__(self,page,words):
        self.page = page   
        self.words = words
class e(d,f):
    def __init__(self,title,page,words,results):
        d.__init__(self,title)
        f.__init__(self,page,words)
        self.results = results
        self.items = [self.title,self.words,self.results,self.page]
    def display(self):
        for i in self.items:
            print(i)
q = e('harrypotter',1234,90000,"sold")
q.display()