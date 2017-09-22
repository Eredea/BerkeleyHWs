import wget

berk_url = "https://inst.eecs.berkeley.edu/~cs61a/sp15/"
filename ="BerkeleyHomePage.txt"
file = wget.download(berk_url, filename)

with open(filename) as file:
    bigstring = file.read()
    words = bigstring.split()
    print(words)