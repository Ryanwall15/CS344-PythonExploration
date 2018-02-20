import string #Library for string
import random  #Library for getting random number

#I knew how to make list and access the contents from this source:
#https://swcarpentry.github.io/python-novice-inflammation/03-lists/
FileNames = [
      'Kashyyyk',
      'Endor',
      'Jakku'
      ]

#I figured out how to get random letter in lowercase and make it into a function from this source
#https://codereview.stackexchange.com/questions/48417/generating-a-random-string-of-characters-and-symbols
#https://www.digitalocean.com/community/tutorials/an-introduction-to-working-with-strings-in-python-3
def RandomLetters():
   RandomLetter = ""
   for i in range(10):
      RandomLetter += (random.choice(string.ascii_lowercase))
   return RandomLetter

#Learned how to write to a text file from this source
#http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
for i in range(3):
   #print(FileNames[i])
   f = open(FileNames[i],"w")
   f.write(RandomLetters());
   f.close()

for i in range(3):
   f = open(FileNames[i],"r")
   print f.read()
   f.close()


#I got my information on how to do this from these sources
#https://www.pythoncentral.io/how-to-generate-a-random-number-in-python/
#https://stackoverflow.com/questions/14381091/how-do-i-assign-a-random-number-to-a-variable
x = random.randint(1,43) #Range is 1 to 42
y = random.randint(1,43)
z = x * y #Get product of the two random numbers

print(x)
print(y)
print(z)


