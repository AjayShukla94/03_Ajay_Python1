#Given the attached CSV data file, write a function find_open_restaurants(csv_filename, search_datetime) which take as parameters a filename #and a Python datetime object and returns a list of restaurant names which are open on that date and time.

import csv
import datetime
import re

#For day
#Mon - 0
#Tue - 1
#Wed - 2
#Thu - 3
#Fri - 4
#Sat - 5
#Sun - 6


#convert day into number
def day(string): 
 switcher = { 
  "Mon" : 0, 
  "Tue" : 1,
  "Wed" : 2,
  "Thu" : 3,
  "Fri" : 4,
  "Sat" : 5,
  "Sun" : 6,
 }  
 #if default value also required then use swither.get(string,7)
 return switcher.get(string)

#update a variable for opening days
def updateOpen(string):
 var = string.split("-")
 n = len(var)
 if n==1:
  openShop[day(var[0])] = 1
 else:
  for i in range(day((var[0])),day(var[1])+1):
   openShop[i] = 1


# Function to convert the date format into opening and closing time in form of integer
def time24(str):
 lis = re.split('[: |  ]',str)
 #length of list
 l = len(lis)	
 if l==3:
  if lis[l-1]=="pm":
   return (int(lis[0])+12)*60+int(lis[1])
  else:
   return int(lis[0])*60+int(lis[1])
 else:
  if lis[l-1]=="pm":
   return (int(lis[0])+12)*60
  else:
   return int(lis[0])*60


#for current day and time
x=datetime.datetime.now()
#Weekday as a decimal number [0(Sunday),6].
currentday = int(x.strftime("%w"))
#Locale’s appropriate time representation.
currentTime = time24(x.strftime("%X"))	


#Driving code
#regex for time selection
regexTime = '[0-9][0-9]?:?[0-9]?[0-9]? [a,p]m'			
#regex for day selection
regexDay = '[MTWFS][ouehra][neduit]-?[MTWFS]?[ouehra]?[neduit]?'
with open('restaurant.csv','r') as csv_file:
 rea = csv.reader(csv_file)
 for line in rea:
  entry = line[1].split("/")
  #variable showing lenth of list when string split by /
  n = len(entry)
  for i in range(n):
   #variable showing opening of shop
   openShop = [0,0,0,0,0,0,0]
   dayList = re.findall(regexDay,entry[i])
   for l in dayList:
    updateOpen(l)
    if openShop[currentday] == 1:
     timeList = re.findall(regexTime,entry[i])
     o = time24(timeList[0])
     c = time24(timeList[1])
     if o<=currentTime and c>=currentTime:
      print(line[0])

	
     


