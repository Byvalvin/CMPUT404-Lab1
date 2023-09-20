import os
import requests as requ


#1) show requests
print(1)
#a cmd from a python script
os.system("pip show requests")
print('\n')

#Can also do
print(requ.__version__)

#2) GET Google homepage
print(2)

URL = "http://www.google.com/"

request = requ.get(URL) #GET request
print(request.status_code) #check if worked
print(request.text) #show the gibberish
print('\n')





####References
#geeksforgeeks.org/get-post-requests-using-python/
#datacamp.com/tutorial/making-http-requests-in-python
#w3schools.com/python/ref_requests_response.asp


#cURL Notes
#-i: include http headers
#-d: send data
#-X POST: to do a POST request