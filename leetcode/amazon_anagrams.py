def amazon_anagrams(arr):

    anagrams = {}

    for string in arr:

      # sorted_string = "".join(sorted(list(string)))  # covert the string into char array then sort it and
                                                       # then convert into string again ::[complex process]

        sorted_string = "".join(sorted(string)) # easiest way to sort the given string
        
        # if the sorted_string exists(as a key) in dictionary then append the current
        # string to it's value(which would be a list). Like, {'key': [value1, value2,....]}.
        if sorted_string in anagrams:

            anagrams[sorted_string].append(string)

        # if not, then create key as sorted_string and value as list of current string.
        else:
            anagrams[sorted_string] = [string]

    return list(anagrams.values())  # by default dict.values() retrun view whic will show dict_values([list of values])
                                    # to get list of all values we have to typecast into list.

                
# Driver Code Starts
if __name__ == "__main__":
    
    strs = [string for string in input("Enter space separated strings: ").split()]

    print(amazon_anagrams(strs))

    """
    Input: eat ate tea ant tan bat adobe abode listen silent

    Output: [['eat', 'ate', 'tea'], ['ant', 'tan'], ['bat'],
            ['adobe', 'abode'], ['listen', 'silent']]

    """