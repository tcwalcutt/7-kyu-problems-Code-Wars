#this is my solution to a challenge/kata on codewars


# You are given an odd-length array of integers, in which all of them are the same, except for one single number.

#Complete the method which accepts such an array, and returns that single different number.

#The input array will always be valid! (odd-length >= 3)

#Examples
#[1, 1, 2] ==> 2
#[17, 17, 3, 17, 17, 17, 17] ==> 3

#codewars predefined function
def stray(arr):
  #looping through each individual number
  for i in arr:
    #checking how many times each number appears
    if arr.count(i) == 1:
      #if number appears only once, we return it!
      return i
