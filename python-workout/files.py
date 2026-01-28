


def get_final_line(filename):

    f = open(filename,'r')

    lines = list(f)

    f.close()

    return lines[-1]



def sumWords(filename):

    sum = 0

    with open(filename,'r') as f:
        for line in f:
            for word in line.split():
                if word.isdigit():

                    sum+= int(word)
    

    return sum


def vowelCount(filename):

    vowels = dict.fromkeys('aieou',0)


    with open(filename,'r') as f:
        for line in f:
            for ch in line.lower():
                if ch in vowels:
                    vowels[ch] +=1
    

    return vowels

def passwd_to_dict(filename):


    output = {}

    with open(filename,'r') as f:

        for line in f:
            line = line.split(':')
            
            output[line[0]] = int(line[2])

    

    return output


def wordCount(filename: str):
    charCount = 0
    wc = 0
    lineCount = 0
    uniqueCount = 0

    st = set()

    with open(filename, 'r') as f:

        for line in f:
            charCount += len(line)
            wc += len(line.split())
            lineCount += 1
            st.update([words for words in line.split()])

        uniqueCount = len(st)
    
    print("This is a test file.")
    print(f'it contains {wc} words and {uniqueCount} unique words')
    print(f'it contains {charCount} charachters')
    print(f'it also contains {lineCount} lines')
    print('It is also self referential')




from collections import defaultdict
import glob
import os

filesize = {filename : os.stat(filename).st_size for filename in glob.glob('python-workout/*.txt')}

print(filesize)

import glob
from collections import Counter

def countletters(directory):

    c = Counter()

    

    for filename in glob.glob(f'{directory}/*.txt'):
        with open(filename,'r') as f:

            for line in filename:
                c.update(line.lower())

    

    return c.most_common(5)


import glob
from collections import Counter

import hashlib 


def find_longest_word(fileName : str):


    longestWord = ''

    m = hashlib.md5()
    m.update(fileName.encode())
    m.hexdigest()
    
    with open(fileName, 'r') as f:

        for line in f:
            for word in line.split():
                if len(word) > len(longestWord):
                    longestWord = word

    
    return longestWord
            

def find_all_longest_words(directory : str):

        output = { filename : find_longest_word(filename) for filename in glob.glob(f'{directory}/*.txt')}

        return output


def summariseReq(filename):

    output = {}

    with open(filename,'r') as f:
        for line in f:
            print(line.split()[8])
            code = line.split()[8]
            output[code] = output.get(code,0) + 1
    
    for key,val in output.items():
        print(f'Response code {key} had {val} requests')






summariseReq('python-workout/mini-access-log.txt')


#print(find_all_longest_words('python-workout'))
            

    
#print(countletters('python-workout'))
            






#wordCount('python-workout/wcfile.txt')

#print(passwd_to_dict('python-workout/text.txt'))







#print(vowelCount('python-workout/text.txt'))




#rint(get_final_line('python-workout/text.txt'))



#print(sumWords('python-workout/text.txt'))