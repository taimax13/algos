#O(n) time O(n) space
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

#    

