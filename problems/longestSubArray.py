from re import S


class solution:
  def lengthOfLongestSubString(self , s :str):

# if length of string = 0 return 0
    if len(s) == 0 :
      return 0

    # we take a dictionary with name map
    map = {}
    # max_lenth and start both point at 0
    max_length = start = 0

    for i in range(len(s)):
      if S[i] in map