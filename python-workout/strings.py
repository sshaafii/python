import string
def pig_latin(word : str):


    punc = ''

    if word[-1] in string.punctuation:
        punc = word[-1]
        word = word[:-1]


    

    
    if word[0] in 'aeiou':
        return f'{word}way'
    else:
        return f'{word[1].capitalize()}{word[2:]}{word[0]}ay{punc}'
    



def pl_sentence(sentence):

    words = sentence.split()

    new_words = []



    for word in words:
        temp = pig_latin(word)
        new_words.append(temp)

    

    return ' '.join(new_words)


def nonsensicalSentence(file):


    ans = []


    with open(file='python-workout/text.txt') as reader:

        for n,line in enumerate(reader.readlines(10)):

            words = line.split()

            if len(words) == 0:
                break

            if n >= len(words):
                ans.append(words[-1])
            else:
                ans.append(words[n])



    return ' '.join(words)


def ubbi_dubbi(word : str) -> str:

    ch = [ _ for _ in word]

    output = []

    for c in ch:

        if c in ['a','e','i','o','u']:
            output.append('ub')
        

        output.append(c)

    

    return ''.join(output)


def removeNames(article: str,names):

    for name in names:

        if name in article:
            article.replace(name,'_')




def str_sort(string : str):

    ans = sorted(string)

    return ''.join(ans)











print(ubbi_dubbi('program'))





            



# print(nonsensicalSentence('text.txt'))











      
    


# print(pig_latin("bob!"))

#print(pl_sentence('hi my name is shaafi working at fiserv today patrol'))




    
        
    
    
    
   