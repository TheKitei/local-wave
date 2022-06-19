import json


# def read(user.id):

#    f = open('DB.json','r') 
#    data = json.load(f)
#    if user.id in data:
      
   
#    f.close()   

def addUserLoc(user):

   f = open('DB.json')
   data = json.load(f)
   f.close()
  
   # Storing all data in a RAM is a bad idea

   if (len(data['users']) == 0 or user.id not in data['users']):
         data['users'][user.id] = user.data
   else :
      data['users'][user.id]['Locations'] = data['users'][user.id]['Locations'] + ((user.Locations))

   # opening file twice -__-
   f = open('DB.json','w')


   # nasty dupl solution

   res = []
   for i in data['users'][user.id]['Locations']:
      if i not in res:
         res.append(i)

   if (len(data['users'][user.id]) != 0):

      data['users'][user.id]['Locations'] = res


   json.dump(data,f,indent=4, separators=(',', ': '))
   f.close()


def getUserLoc(user):
      f = open('DB.json')
      data = json.load(f)
      f.close()

      return data['users'][user]['Locations']


def lastSongUp(song):
   return


# print(getUserLoc('1125'))
# addUserLoc('1125','123 123 123')
