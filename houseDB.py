import json
import os

def addUserLoc(user):


   f = open('DB.json','r')
   try:
      data = json.load(f)
   except:
      f.close()
      f.open('DB.json','w')
      template = {"users":{}}
      json.dump(template,f)
      f.close()
      f = open('DB.json','r')
      data = json.load(f)

   f.close()
   
  
   # Storing all data in a RAM is a bad idea

   if (len(data['users']) == 0 or not(user.id in data['users'])):
         data['users'][user.id] = user.Locations
   else :
      data['users'][user.id] = data['users'][user.id] + user.Locations

   f = open('DB.json','w')


   # nasty dupl solution

   res = []
   for i in data['users'][user.id]:
      if i not in res:
         res.append(i)

   if (len(data['users'][user.id]) != 0):

      data['users'][user.id] = res


   json.dump(data,f,indent=4, separators=(',', ': '))
   f.close()


def getUserLoc(user):
      f = open('DB.json')
      data = json.load(f)
      f.close()

      return data['users'][user]['Locations']


# def lastSongUp(song):
#    return


# print(getUserLoc('1125'))
# addUserLoc('1125','123 123 123')
