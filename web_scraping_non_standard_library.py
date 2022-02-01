######################################################
"""How to GET AND POST with non standard library"""
######################################################


#######################
"""Import modules"""    #requests module is not native to python and must be installed via pip or pip3
########################
import requests



##################################
"""GET info from website"""
#################################
response = requests.get('https://www.devdungeon.com/archive')
print(response.text)
print(response.status_code)
print(response.headers)



#############################
"""POST info to website"""
#############################
response = requests.post('https://httpbin.org/anything',
                        files ={'file': 'The file contents'},          #info must be passed as a dictionary
                        data ={'form_field_name': 'form_value'},
                        params={'q': 5, 'action':'delete'}     
                        )
print(response.text)


###############################
"""STREAM data in upload"""
###############################
with open('large_file.txt', 'rb') as file_contents:
    response = requests.post('https://httpbin.org/anything', data = file_contents)
    print(response)










"""SEE 'web_scraping.py' for more information about post and get"""