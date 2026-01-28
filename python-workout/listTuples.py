


def firstLast(sequence):


    



    pass



def evenOddSums(seq):


    evenSum = sum(seq[::2])
    oddSum = sum(seq[1::2])

    return [evenSum,oddSum]


def plus_minus(seq):

    sum = seq[0]

    for i in range(1,len(seq)):

        if i % 2 == 0:
            sum -= seq[i]
        else:
            sum += seq[i]

    
    return sum


# print(plus_minus([10,20,30,40,50,60]))





def fake_zip(*args):

    ans = []
    for i in range(len(args[0])):

        ans.append(tuple( a[i] for a in args ))

    


    return ans



def mysum(*args):


    sum = args[0]

    for i in range(1,len(args)):
        sum+= args[i]

    return sum



def mysum_bigger_than(threshold,*args):

    sum = args[0]

    for i in args[1:]:

        if i < threshold:
            continue

        sum += i


    return sum



def sum_numeric(*args):

    sum = 0

    for i in args:

        try:      

            sum += int(i)

        except Exception as e:

            pass
        
    return sum


def combineDicts(dicts):





    pass


import operator


COUNTRIES = [
{'name': 'Canada', 'size': 9984670, 'population': 38250000},
{'name': 'Italy', 'size': 301340, 'population': 59110000},
{'name': 'United Kingdom', 'size': 242495, 'population': 67220000},
{'name': 'France', 'size': 551695, 'population': 67390000},
{'name': 'Germany', 'size': 357022, 'population': 83200000},
{'name': 'Japan', 'size': 377975, 'population': 125700000},
{'name': 'United States', 'size': 9833517, 'population': 331900000}]


f = operator.itemgetter('name')



seq = [-1,-2,5,2,3,-4,-10,7,8]

sorted(seq,key=abs)
print(seq)


def vowelCount(word):
    total = 0 

    for i in word:
        if i in 'aeiou':
            total +=1
    

    return total

words = ['hello','because','globe','mansion','dinosaur']



#sorted(words,key=vowelCount)
#print(words)

#sorted(COUNTRIES,key= f)
#print(COUNTRIES)



    
#combineDicts([{'a': ['alpha','apple','add']}])
#print(sum_numeric(10,20,'a','30',50))

import collections
from collections import Counter



def most_repeating_letter(word):

    cnt = Counter(word)
    return cnt.most_common(1)


def most_repeating_words(wordss):

    return max(wordss,key=most_repeating_letter)

print(most_repeating_words(words))


def most_repeated_vowels(word):
    pass



















#print(mysum([1,2,3],[4,5,6]))








#print(fake_zip([10,20,30],'abc'))







# print(evenOddSums([10,20,30,40,50,60]))