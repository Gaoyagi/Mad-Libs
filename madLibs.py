#Mad libs project
#George Aoyagi
#player plays madlibs with a preset template

#dictionary that holds all of the users inputs
# nouns:4, occupation:1, verb:3 adjective:2;    total:10
libs = {'job': "occupation", 'noun0': "noun", 'verb0': "verb", 'adj0': "adjective", 'noun1': "noun",
        'verb1': "verb", 'adj1': "adjective", 'noun2': "noun", 'verb2': "verb", 'noun3': "noun"}


#prompts users to input eitehr a  noun, adjective, verb, or an occupation and then fills in a dictionary accordingly, afterwards it returns the template with all the blanks filled in
def inserts():
    for words in libs:
        temp = input("enter a(n) " + libs[words] + ": ")
        libs[words] = temp
    return """Today a %0s named %1s came to our school to talk to us about her job.
            She said the most important skill you need to know to do her job is to be able to %2s around (a) %3s %4s.
            She said it was easy for her to learn her job because she loved to %5s when she was my age--and that helps a lot!
            If you're considering her profession, I hope you can be near (a) %6s %7s. That's very important!
            If you get too distracted in that situation you won't be able to%8s next to (a) %9s!""" %(libs['job'], libs['noun0'], libs['verb0'], libs['adj0'], libs['noun1'], libs['verb1'], libs['adj1'], libs['noun2'], libs['verb2'], libs['noun3'])


#runs program
madlib = inserts()
print(madlib)


#python3 madLibs.py
