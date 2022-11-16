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

#######################################################################
def minimumCharactersForWords(words):
    res={}
    for word in words:
        char_occur_times = numberOcureTimes(word)
        updateRes(char_occur_times, res)
    return generate_array(res)

def numberOcureTimes(string):
    res = {}
    for char in string:
        if char not in res:
            res[char] = 0
        res[char] +=1
    return res        

def updateRes(char_occur_times, res):
    for char in char_occur_times:
        occur_times =  char_occur_times[char]
        if char in res:
            res[char]=max(occur_times, res[char])
        else:
            res[char] = occur_times    

def generate_array(res):
    chars=[]
    for char in res:
        occur=res[char]
        for _ in range(occur):
            chars.append(char)
    return chars        
#################################################################

def longestSubstringWithoutDuplication(string):
    res = [0,1]
    startInd = 0
    lastPosition = {}
    for i ,char, in enumerate(string):
        if char in lastPosition:
            startInd = max(startInd, lastPosition[char]+1)
        if res[1]-res[0]< i+1 -startInd:
            res = [startInd, i+1]
        lastPosition[char] = i
    return string[res[0]:res[1]]            

################################################################
def underscorifySubstring(string, substring):
    ##find location
    ##find joined loccation - merge in the join array
    ##add the underscores
    print(locate(string, substring))
    locarions = mergeSubstring(locate(string, substring))
    return underscore(string,locarions)

def locate(string, substring):    
    locations = []
    startInd = 0
    nextInd =0 
    while startInd < len(string) :
        nextInd = string.find(substring, startInd)
        if nextInd == -1:
            break
        locations.append([nextInd, nextInd + len(substring)])
        startInd = nextInd+1
    
    return locations        


def mergeSubstring(array_substrings):
    if not len(array_substrings):
        return array_substrings
    res =[array_substrings[0]] 
    prev = array_substrings[0]   
    for i in range(1, len(array_substrings)):
        current = array_substrings[i]
        if current[0] <= prev[1]:
            prev[1]=current[1]
        else: 
            res.append(array_substrings[i]) 
            prev = current   
    return res    


def underscore(string,locations):
    locationsInd = 0
    stringIndex = 0
    res = []
    i=0
    added = False
    while stringIndex < len(string) and locationsInd < len(locations):
        if stringIndex == locations[locationsInd][i]:
            res.append("_")
            added =not added
            if not added:
                locationsInd+=1
            i = 0  if i==1 else 1  
        res.append(string[stringIndex])
        stringIndex += 1
    if locationsInd < len(locations): res.append("_")
    elif stringIndex < len(string): res.append(string[stringIndex:])
    return "".join(res)        


#print(underscorifySubstring("testthis is a testtest to see if testestest it works", "test"))
###############################################################
def patternMatcher2(pattern, string):
    res={}
    res["x"] = string[0]
    res["y"] = string[1]
    string=[]
    for i in range(len(pattern)):
        string.append(res[pattern[i]])
    return "".join(string)

#print(patternMatcher("xxyxx", ["go", "do"]))


##############################################################
def patternMatcher(pattern, string):
    if len(pattern)>len(string):
        return []
    current_pattern = getPattern(pattern)
    switched = current_pattern[0] != pattern[0]
    pattern_count = {"x": 0 , "y": 0}
    get_y = getlengthYposition(current_pattern,pattern_count)
    if pattern_count["y"] !=0:
        for lenX in range(1,len(string)):
            lenY = (len(string)-lenX * pattern_count["x"]) / pattern_count["y"]
            if lenY<=0 or lenY % 1 !=0:
                continue
            lenY = int(lenY)
            yInd = get_y * lenX
            print(yInd)
            x = string[:lenX]
            y = string[yInd:yInd+lenY]
            pattern_match = map(lambda char: x if char == "x" else y,  current_pattern)
            if string == "".join(pattern_match):
                return [x,y] if not switched else [y,x]
    else: 
        lenX = len(string) / pattern_count["x"]
        if lenX % 1 == 0:
            lenX = int(lenX)
            x = string[:lenX]
            pattern_match = map(lambda char: x, current_pattern)
            return [x, ""] if not switched else ["",x]
    return []        


def getlengthYposition(pattern,pattern_count):
    firstY = None
    for i, char in enumerate(pattern):
        pattern_count[char] += 1
        if char == 'y' and firstY == None:
            firstY = i
    return firstY        

def getPattern(pattern_string):
    pattern = list(pattern_string)
    if pattern[0]=="x": 
        return pattern
    else:
        return list(map(lambda char: "x" if char=='y' else 'y', pattern))    

print(patternMatcher("xxyy", "gogototo"))

