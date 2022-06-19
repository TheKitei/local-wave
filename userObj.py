import houseDB
import events

class User:
    RemindTime = "12:00:00"
    
    
    def __init__(self, userID):
        self.id = str(userID)
        

        # self.data = {"Locations":self.Locations,"RemindTime":self.RemindTime}
        
    def addLoc(self,userLoc):
        self.Locations = userLoc
        houseDB.addUserLoc(self)

    def sendEvents(self):
        return events.recive(self.id)
        

# me = User(4111,['Riga','Cesis','Liepaja'])
