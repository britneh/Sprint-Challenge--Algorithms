'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
#Understand -- So we have some string of any length of character and we want to count 
#how many times th appears in said word.  Looking at the test for a reference, this would 
#case must be lower but it can anywhere within the word
#how do we keep it moving once found? -- search if in the beginning first.. the first 2 indices

# Plan -- If the word is just a space, we wouldn't need to run a count, or even if 
#is just a single character, so we need to include that as an edge case
#If we've determined the length long enough to hold at leat one of the substrings, 
#We can search through it; 
def count_th(word):
    #case matters so we are specifically looking for
    target = 'th'

    #Edge case - th is a two letter word so anything less than that won't even apply
    if len(word) < 2:
        return 0
    #Now we have a searchable word
    #we first check if the beginning is the substring, then recurse to find others
    if target in word[:2]:
        return 1 + count_th(word[2:])
    #if beginning is not substring we can just search the remainder first and then recurse to find others
    else:
        return 0 + count_th(word[1:])
