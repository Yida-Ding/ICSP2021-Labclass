class Event:
    def __init__(self,name,date,time,location):
        self.name=name
        self.time=time
        self.date=date
        self.location=location
class calender:
    def __init__(self):
        self.li=[]
    def NewEvent(self,a):
        self.li.append(a)
    def FindEvent(self,b):
        for i in range(len(self.li)):
            if b==self.li[i].date:
                print(self.li[i].name)
mycalender=calender()
boyaclass=Event("boyaclass","10/5","9am","D1120")
mycalender.NewEvent(boyaclass)
mycalender.FindEvent("10/5")

    