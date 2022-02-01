
from urllib.parse import urlparse, urlunparse

#######################
"""Parsing a URL"""     #AKA getting a url and breaking it down
#######################
parsed_url = urlparse('https://www.49ers.com/playoffs/')

#Print the whole parsed URL ==> ParseResult(scheme='https', netloc='www.49ers.com', path='/playoffs/', params='', query='', fragment='')
print(parsed_url)
#Print just the scheme  
print(parsed_url.scheme)
#Print just the netloct  
print(parsed_url.netloc)
#Print just the path
print(parsed_url.path)
#Print the params
print(parsed_url.params)
#Print the query
print(parsed_url.query)
#Print the fragments
print(parsed_url.fragment)


######################################
"""Unparsing a URL / Create a URL """    #(AKA Putting info back together to form a complete URL
######################################
new_url = urlunparse(('https',  #Scheme we want to use
    'www.devdungeon.com',       #Netloc we want to use
    '/archive',                 #Path
    None,                       #Params
    'q=5&x=that',               #Query
    'test_fragment' ))          #Fragment

print(new_url)           #Prints out url we just created 
                         #==> https://www.devdungeon.com/archive?q=5&x=that#test_fragment