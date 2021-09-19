#this my solution to this code wars problem
#Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

#Examples
#"This is an example!" ==> "sihT si na !elpmaxe"
#"double  spaces"      ==> "elbuod  secaps"

#predefined function courtesy of codewars.
def reverse_words(text):
  # An empty string to put our final list into.
    string = " "
    #an empty list to put our reversed words into
    li =[]
    # a for loop to iterate through our input, while splitting each word into a list.
    for x in text.split(' '):
      # This appends the reverse word to our empty list.
        li.append(x[::-1])
    # this returns the new list joined together into a new string, using our empty string.
    return string.join(li)