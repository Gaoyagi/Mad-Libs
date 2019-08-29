#Mad libs project
libs = ["occupation": "occupation", "noun0":"noun", "verb0":"verb", "adjective0":"adjective", "noun1":"noun", "verb1": "verb", "adjective1":"adjective", "noun2":"noun", "verb2":"verb", "noun3":"noun"]

#Mad libs template taken from glowwordbooks.com
madlib = """Today a %0s named %1s came to our school to talk to us about her job.
            She said the most important skill you need to know to do her job is to be able to %2s around (a) %3s %4.
            She said it was easy for her to learn her job because she loved to %5s when she was my age--and that helps a lot!
            If you're considering her profession, I hope you can be near (a) %6s %7s. That's very important!
            If you get too distracted in that situation you won't be able to
            %8s next to (a) %s9!""" %(libs["occupation"], libs["noun0"], libs["verb0"],libs["adjective0"], libs["noun1"], libs["verb1"], libs["adjective1"], libs["noun2"], libs["verb2"], libs["noun3"])

def inputs():
    for words in libs:
        temp = input("enter a ", libs[words])
        libs[words] = temp

inputs()
print madlib
