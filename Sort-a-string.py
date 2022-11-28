# Sort a string 
# Test Case: "I love my FAMILY"
# Ans: "FAMILY I love my"

def sortString(phrase):
    phrase_list=phrase.split()
    phrase_list=[w.lower()+ w for w in phrase_list]
    phrase_list.sort()
    phrase_list=[w[len(w)//2:] for w in phrase_list]
    return " ".join(phrase_list)   


# One Liner Approach
# def OneLinerApproach(phrase):
#     return " ".join(sorted(phrase.split(),key=str.casefold()))

phrase="HELLO dear sir"
print(sortString(phrase))