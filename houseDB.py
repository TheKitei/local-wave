import json

# def read(user):

#    f = open('DB.json','r') 
#    data = json.load(f)
#    if user in data:
      
   
#    f.close()   

def addUserLoc(user,loc):

   f = open('DB.json')
   data = json.load(f)
   f.close()
  
   # Storing all data in a RAM is a bad idea

   if (len(data['users']) == 0 or user  not in data['users']):
      data['users'][user] = []


   
   # nasty dupl solution



   # opening file twice -__-
   for i in loc :
      data['users'][user].append(i)


   f = open('DB.json','w')

   res = []
   for i in data['users'][user]:
      if i not in res:
         res.append(i)

   if (len(data['users'][user]) != 0):

      data['users'][user] = res


   json.dump(data,f,indent=4, separators=(',', ': '))
   f.close()


def lastSongUp(song):
   return

# addUserLoc('1125','123 123 123')
