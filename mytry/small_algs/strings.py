#O(n) time O(n) space
from turtle import st


def caesarCipherEncryptor(string, key):
    newLetters =[]
    newKey = key %26
    for letter in string:
        newLetters.append(getNewLetter(letter, newKey))
    return "".join(newLetters)    

def getNewLetter(letter,key):  
    newLetterCode = ord(letter) + key
    return chr(newLetterCode) if newLetterCode <=122 else chr(96 + newLetterCode %122)

########################################################################

def runLengthEncoding(string):
    chars = []
    length = 1
    for i in range(1,len(string)):
        if string[i] != string[i-1] or length==9:
            chars.append(str(length)) 
            chars.append(string[i-1])
            length =0
     
        length +=1
  
    chars.append(str(length))
    chars.append(string[len(string)-1])        
    return "".join(chars)
#print(runLengthEncoding("AAAAASSSSGGh"))
########################################################################
def generateDocument(characters, document):
    chars_map_count = {}

    for char in characters:
        if char not in chars_map_count:
            chars_map_count[char] = 0
        chars_map_count[char]+=1

    for char in document:
        if char not in chars_map_count or chars_map_count[char] == 0:
            return False

        chars_map_count[char]-=1
    return True                



#print(generateDocument("AlgoExpert is the Best!", "Bste!hetsi ogEAxpelrt x "))

def firstRepeatingCharacter(string):
    count_char = {}
    for i in range(len(string)):
        if string[i] in count_char.keys():
            return count_char[string[i]]
        else: 
            count_char[string[i]]=i

    return -1            
    
#print(firstNonRepeatingCharacter("abcdcaf"))

def firstNonRepeatingCharacter(string):
    count_char = {}
    for char in string:
        count_char[char] = count_char.get(char,0) + 1
    for i in range(len(string)):
        if count_char[string[i]] == 1:
            return i
    return -1            

#######################################################################
def longestPalindromicSubstring(string):
    polindrome = [0,0] ##I am assuming it can be a case I do not have any polindrom in the string 
    for i in range(1,len(string)):
        odd = getLongestPolindromFrom(string, i-1, i+1)
        even = getLongestPolindromFrom(string, i-1, i)
        longest = max(odd,even, key=lambda x :x[1]-x[0])
        polindrome = max(longest, polindrome, key = lambda x:x[1]-x[0])

    return string[polindrome[0]:polindrome[1]+1]    

def getLongestPolindromFrom(string, leftI, rightI):
    while leftI>=0 and rightI<len(string):
        if string[leftI]!=string[rightI]:
            break
        leftI -= 1
        rightI+=1
    return [leftI+1, rightI-1]    

#######################################################################
def groupAnagrams(words):
    res = {}
    for word in words:
        word_sorted = "".join(sorted(word))
        if word_sorted in res:
            res[word_sorted].append(word)
        else:
            res[word_sorted] = [word] 
    return list(res.values())  

#######################################################################
###valid ip address -> validate length -> validate substring
#min(len(string) - to avoid index error
def validIPAddresses(string):
    res =[]
    for i in range(1,min(len(string),4)):
        current = ['','','','']
        current[0] = string[:i]
        if not validateStr(current[0]): continue
        for j in range(i +1, i+min(len(string)-i, 4)):
            current[1] = string[i:j]
            if not validateStr(current[1]):continue
            for k in range(j+1, j+min(len(string)-j,4)):
                current[2] = string[j:k]
                current[3] = string[k:]
                if  validateStr(current[2]) and validateStr(current[3]): res.append('.'.join(current))

    return res

def validateStr(string):
    str_int = int(string)
    return len(string) == len(str(str_int)) if str_int <= 255  else False

#print(validIPAddresses("00010")) 

#######################################################################
def reverseWordsInString(string):
    res=[]
    start_W=0
    for i in range(len(string)):
        ch = string[i]
        if ch == " ": 
            res.append(string[start_W:i])
            start_W = i
        elif string[start_W] == " ":   
            res.append(" ")
            start_W = i 
    res.append(string[start_W:])
    reverseList(res)
    return "".join(res)

def reverseList(list):
    start, end =0 , len(list)-1
    while start<end:
        list[start], list[end]=list[end], list[start]
        start +=1
        end -=1


