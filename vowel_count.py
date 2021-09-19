#Return the number (count) of vowels in the given string.

#We will consider a, e, i, o, u as vowels for this Kata (but not y).

#The input string will only consist of lower case letters and/or spaces.

# function predefined courtesy of code wars
def get_count(sentence):
  #declaring vowels
    vowels = "aeiou"
    #declaring count at 0 this will tell us how many vowels we have.
    count= 0
    # this iterates though each part of the sentence
    for x in sentence:
    # this checks if the letter from sentence is a vowel
        if x in vowels:
        #if the x is a vowel it adds 1 for each time a vowel is found
            count += 1
    return count