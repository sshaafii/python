
def pig_latin(word : str):
    
    if word[0] in 'aeiou':
        return f'{word}way'
    else:
        return f'{word[1:]}{word[0]}ay'
      
    


print(pig_latin("python"))
    
        
    
    
    
   