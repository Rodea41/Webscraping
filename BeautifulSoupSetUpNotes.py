###################
"""Installing BeautifulSoup"""
#############################
> pip3 install beautifulsoup4

##############################
"""Importing BeautifulSoup"""
##############################
from bs4 import BeautifulSoup

#Optional imports to use with bs4

requests: Performs the URL request and fetches the website's HTML
            # must be installed via > pip3 install requests
            
time: limits how many times we scrape the page at once

csv: helps us export our scraped data to a CSV file

re: allows us to write regular expressions that will come in
    handy for picking text based on its pattern







################################
"""Using bs4 with files"""
################################
"""The HTML file doc.html needs to be prepared. This is done by passing the
file to the BeautifulSoup constructor"""

with open("index.html") as fp:
    soup = BeautifulSoup(fp, "html.parser") #Second arg is optional

    ### OR ###

soup = BeautifulSoup(html_doc, 'html.parser')



#############################
"""Navigate the structure"""
#############################

soup.title  #==> <title>The Dormouse's story</title>

soup.title.name #==> u'title'

soup.title.string #==> u'The Dormouse's story'

soup.title.parent.name #==> u'head'

soup.p #==> <p class="title"><b>The Dormouse's story</b></p>

soup.p['class'] #==> u'title'

soup.a #==> <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find_all("a", limit=25)  # ==> Limits search results to 25
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

# .find_all() ==> returns an empty list if nothing can be found

soup.find(id="link3") # Can use name=, attrs=, string=
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

# .find() ==> returns None if nothing can be found

#######################################
"""Parsing only part of a document"""
#######################################
"""
Let’s say you want to use Beautiful Soup look at a document’s <a> tags. It’s a waste of time and memory to parse the entire
document and then go over it again looking for <a> tags.It would be much faster to ignore everything that wasn’t an <a> tag in
the first place. The SoupStrainer class allows you to choose which parts of an incoming document are parsed. You just create a
SoupStrainer and pass it in to the BeautifulSoup constructor as the parse_only argument.
"""

from bs4 import SoupStrainer

only_a_tags = SoupStrainer("a")

only_tags_with_id_link2 = SoupStrainer(id="link2")

def is_short_string(string):
    return len(string) < 10

only_short_strings = SoupStrainer(string=is_short_string)





########################################################
"""Extracting the URL found within a page's <a> tags:"""
########################################################
soup.find_all('a')
for link in soup.find_all('a'):
    print(link.get('href'))
# http://example.com/elsie
# http://example.com/lacie
# http://example.com/tillie


#########################################
"""Extracting all the text from a page with
get_text() and .stripped_strings    """
#########################################
"""If you only want the text part of a document or tag, you can use the get_text() method.
It returns all the text in a document or beneath a tag, as a single Unicode string: """

markup = '<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>'
soup = BeautifulSoup(markup)
just_the_text = soup.get_text()
print(just_the_text)

#Changes this ==> u'\nI linked to example.com\n'
#To this ==> u'example.com'

soup.get_text(",") ==> Joins each result with a comma

soup.get_text(",", strip=True) ==> strips whitespace from the start/end of each bit

.stripped_strings generator
    [text for text in soup.stripped_strings] ==> [u'I linked to', u'example.com']
    

##########################################
"""Navigating upwards through elements"""
##########################################
"""You can iterate over all of an element’s parents with .parents. This example uses .parents to
travel from an <a> tag buried deep within the document, to the very top of the document: """

link = soup.a
link
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
for parent in link.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
# p
# body
# html
# [document]
# None


#############
"""Notes"""
#############
"""
- Calling a 'tag' is like calling find_all() 
    These two lines of code are equivalent:
        - soup.find_all("a")
        - soup("a")
    They both will return ALL of the 'a' tags in the HTML

- Pretty-printing
    Using prettify() method will turn a bs4 parse tree into a nicely
    formated Unicode string, with seperate lines for each tag and string
        ex. markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
            soup = BeautifulSoup(markup)
            soup.prettify()
            print(soup.prettify())




"""

