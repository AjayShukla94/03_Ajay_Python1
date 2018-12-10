#name:        restaurant_search
#description: It search a open restaurant name according to user given date and time
#input:       data, time and csv file nameby user	(date like 12/07/2018 and time 22:10 am|pm)
#output:      List of open restaurant
#usage:       Use by any user and get open restaurant at specific date
#example:     Zomato

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
		for i in range(day(var[0]),day(var[1])+1):
		openShop[i] = 1


# Function to convert the date format into opening and closing time in form of integer
def time24(str):
	lis = re.split('[: |  ]',str)
	#length of list
	l = len(lis)	
	if l==3:
		if lis[l-1]=="pm" and lis[0]==12:
			return int(lis[0])*60+int(lis[1])
		elif lis[l-1]=="pm" and lis[0]!=12:
			return (int(lis[0])+12)*60+int(lis[1])
		elif lis[l-1]=="am" and lis[0]==12:
			return int(lis[1])
		else:
			return int(lis[0])*60+int(lis[1])
	else:
		if lis[l-1]=="pm" and lis[0]==12:
			return int(lis[0])*60
		elif lis[l-1]=="pm" and lis[0]!=12:
			return (int(lis[0])+12)*60
		elif lis[l-1]=="am" and lis[0]==12:
			return int(0)
		else:
			return int(lis[0])*60	

#function to check validation of date
def validate_date(day,month,year):
    try:
        ans = datetime.date(year, month, day)
    except Exception:
        print("Please give a valid date")



#function to check validation of time
def validate_time(hour,minute):
    try:
        datetime.time(hour,minute)
    except Exception:
        print("Please give a valid time")

#function to validate file 
def validate_file(file_name)
	    try:
			fh = open('file_name', 'r')
        # Store configuration file values
    except FileNotFoundError:
        print(please give a real file name)

#Driving code


#regex for date selection
regexDate = '[0-9][0-9]?/[01]?[0-9]/[0-9]{4}'
#regex for time selection
regexTime = '[0-9][0-9]?:?[0-9]?[0-9]? [a,p]m'			
#regex for day selection
regexDay = '[MTWFS][ouehra][neduit]-?[MTWFS]?[ouehra]?[neduit]?'
#regex for file selection
regexFile = '\W.csv'

print("From which file you want selection :")
fileName = input("file name :")
if re.fullmatch(regexFile,fileName) != None:
	validate_file(fileName)
	print("At what time you want resturent : please give date like 12/05/2007 and time 22:14 am|pm")
	currDate = input("give date :")
	if re.fullmatch(regexDate, currDate) != None:
		Day, month, year = (int(x) for x in currDate.split('/'))    
		validate_date(Day,month,year)
		ans = datetime.date(year, month, Day)
		currTime = input("give time :")
		if re.fullmatch(regexTime,currTime) != None:
			hour, minute, meating= (y for y in re.split('[: |  ]',currTime))
			validate_time(int(hour),int(minute))
			currentday = int(ans.strftime("%w"))
			currentTime = time24(currTime)
		else:
		print("give time is not in specified formate")
	else:
		print("give date in specified maner")
		
with open('fileName','r') as csv_file:
	rea = csv.reader(csv_file)
	for line in rea:
		entry = line[1].split("/")
		#variable showing lenth of list when string split by /
		n = len(entry)
		for i in range(n):
			#variable showing opening of shop
			openShop = [0,0,0,0,0,0,0]
			dayList = re.findall(regexDay,entry[i])
			for p in dayList:
			updateOpen(p)
			if openShop[currentday] == 1:
				timeList = re.findall(regexTime,entry[i])
				o = time24(timeList[0])
				c = time24(timeList[1])
				if o<=currentTime and c>=currentTime:
					print(line[0])

	
     


