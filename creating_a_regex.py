
#########################
""""Import re module"""
########################
import re


#Specify what file, string you want to search for
file_to_look_through = 'askhfkasdhfhdsfhdshfasdklfhkhsd<script src ="asfd">java\nsc\nri\npt\n</script>ajsfljdlfjljfladsjfljdl;djlf'

#Specify what the re 'filter' you want to use
regex_to_use = '<script(.|\n)*</script>'

#Assign the results to an var object
re_match = re.search(regex_to_use, file_to_look_through)

#Assign the first match to a var
matching_text = re_match.group(0)

#print out the first match in the re object
print(matching_text)
