import os
import requests as requ


#1) show requests
print("M1")
##############################################################
#a cmd from a python script
# os.system("pip show requests")

#Can also do
print(requ.__version__)
print('\n')
##############################################################

#2) GET Google homepage
print("M2")
##############################################################
URL = "http://www.google.com/"

request = requ.get(URL) #GET request
print(request.status_code) #check if worked
# print(request.text) #show the gibberish
print('\n')
##############################################################

#3) Download Source code from GitHub using GET
print("M3")
##############################################################
#get raw data for my source code
URL2 = "https://raw.githubusercontent.com/Byvalvin/CMPUT404-Lab1/master/lab1.py"
request2 = requ.get(URL2) #GET request
# print(request2.content)

#write my source code to another file and save it
filename = "code.py"
with open(filename, mode="wb") as file:
	file.write(request2.content)
print("\n")
##############################################################

#4) Show Source code in terminal
print("M4")
##############################################################
f = open(filename,'r')
for line in f.readlines():
	print(line)

f.close()
##############################################################

####References
#geeksforgeeks.org/get-post-requests-using-python/
#datacamp.com/tutorial/making-http-requests-in-python
#w3schools.com/python/ref_requests_response.asp
#https://www.datacamp.com/tutorial/git-push-pull
#https://realpython.com/python-download-file-from-url/

#cURL Notes
#-i: include http headers
#-d: send data
#-X POST: to do a POST request