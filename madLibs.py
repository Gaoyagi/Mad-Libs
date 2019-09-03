#Mad libs project
#George Aoyagi
#player plays madlibs with a preset template

import random
import sys
from termcolor import colored, cprint

#dictionary that holds all of the users inputs
# nouns:4, occupation:1, verb:3 adjective:2;    total:10
libs = {'job': ["occupation"],
        'noun': ["noun", "noun", "noun", "noun"],
        'verb': ["verb", "verb", "verb"],
        'adj': ["adjective", "adjective"]}

#prompts users to input eitehr a  noun, adjective, verb, or an occupation and then fills in a dictionary accordingly, afterwards it returns the template with all the blanks filled in
def inserts():
    for words in libs:
        for terms in range(len(libs[words])):
            temp = input("enter a(n) " + libs[words][terms] + ": ")
            libs[words][terms] = temp

def fill_in():
    random.shuffle(libs['noun'])
    random.shuffle(libs['verb'])
    random.shuffle(libs['adj'])
    return f"""    Today a {libs['job'][0]} named {libs['noun'][0]} came to our school to talk to us about her job.
    She said the most important skill you need to know to do her job is to be able to {libs['verb'][0]} around (a) {libs['adj'][0]} {libs['noun'][1]}.
    She said it was easy for her to learn her job because she loved to {libs['verb'][1]} when she was my age--and that helps a lot!
    If you're considering her profession, I hope you can be near (a) {libs['adj'][1]} {libs['noun'][2]}. That's very important!
    If you get too distracted in that situation you won't be able to {libs['verb'][2]} next to (a) {libs['noun'][3]}"""



#random.shuffle(list)

#runs program
inserts()
madlib = fill_in()
print(madlib)


#python3 madLibs.py
