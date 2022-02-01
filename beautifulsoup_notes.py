from urllib import response
import requests
from bs4 import BeautifulSoup


#Set which website you want to scrape
response = requests.get('https://www.devdungeon.com/')

#set to object
soup = BeautifulSoup(response.text)

#Different formatiing 
print(soup.prettify())  #Print the webpage contents with indentation
print(soup.title) #Prints title with tags ==> <title>DevDungeon | Virtual Hackerspace</title>
print(soup.title.string) #Prints just title ==> DevDungeon | Virtual Hackerspace

########################################################
"""Grabbing HTML tags and ways to iterate through them"""
########################################################
for a in soup.find_all('a'): #Gets all the links AND tags and prints them 1 by 1 
    print(a)                 #Example ==> <a href="https://www.devdungeon.com/content/taking-command-line-arguments-python">Taking Command Line Arguments in Python</a> 

for a in soup.find_all('a'): #Gets all the NAME of the links and prints them 1 by 1 
    print(a.string)          #Example ==> "Skip to main menu"

for a in soup.find_all('a'): #Gets all the links , but filters out the '<a' tag
    print(a.get('href'))     #Example ==> https://www.devdungeon.com/content/2-minute-intro-p5js

for a in soup.find_all('a'): #Gets both the title and the link 
    print(a.string)          #Example ==> about me
    print(a.get('href'))     #Example ==> https://www.devdungeon.com/content/about-me



