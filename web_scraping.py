##################################################
""" HTTP GET and POST request with standard library"""
##################################################
import urllib.request


##############################
""" Open URL with string"""
##############################
page = urllib.request.urlopen('https://www.49ers.com/') #Getting website and store it in an object called 'page'
print(page.read())


############################
"""OR prebuild the request"""
#############################
page = urllib.request.Request('https://www.49ers.com/')

page.add_header('User-Agent', 'Not Firefox')        #'add.header()' is used to 'spoof' the 'User-Agent' header value, that the browser uses.
                                                    #because some HTTP servers only allow requests from common browsers and will block scrapers

response = urllib.request.urlopen(page)             #This gets the webpage now with the new 'header' we added
print(response.read())                              #print to cmd/console the contents of page


###########################################
"""Write Page Contents to a file.txt """
###########################################
page = urllib.request.urlopen('https://www.49ers.com/')

f = open("web_contents.txt", "w")   #file that your writing to must be in same dir as script 
content = page.read()               #Storing the contents of the 'page' object into object named content
f.write(str(content))               #Must convert the object into a str and then use .write() method to write to txt file
f.close()                           #Close the file after writing to it. 



"""
#####################
General Notes
#####################

- GET() = Used for viewing something.  Ex. ==> Search page should use GET request
    - Used to retrieve data
    - Should be able to request the same URL over and over with no consequences
    - Should NOT be used for operations that cause 'side-effects' such as taking action in web applications
    - Often used by web crawlers and robots who just need need the contents of the page, and dont need to
      interact with it. 

- POST = Used for changing something Ex. ==> A form that changes your password should use POST request
    - Used to insert/update remote data.
    - Write/submit data from an HTML form to be processed by site
    - Can have side effect of using the same request several times. Browsers
      will give you warnings about this, but may also block future requests.
    - POST is NOT secure, data is included in the body of the request

- STREAMING = Send large streams or files without reading them into memory 
"""