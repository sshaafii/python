import random



def guessing_game():
    
    num = random.randint(1,100)
    # print(num)
    # now ask user for input
    
    
    count = 0
    
    
    while True:
        
        if count == 3:
            print("number of guesses finished")
            break
        
        
        guess = int(input("Enter your guess number"))
        
        if guess == num:
            print(f'{num} is the correct number')
            break
        elif guess > num:
            count += 1
            print(f'{guess} is greater then {num}')
        elif guess < num:
            count += 1
            print("Try again. Guess is to low")
            
def guessing_game3():
    
    dictionary = {'a':}

#use variadic argument. Allows function to accept number of arguments
def mysum(*args, sumi=0):
    sum = sumi
    
    for x in args:
        sum += x    
    
    
    print(sum)
    return sum

def run_time():
    
    count = 0
    
    while True:
    
        try:
            run =  input("Enter 10km run time")
            count += 1
        except Exception as e:
            print(e)
       
       
        if not run:
           break
       
        total_time += float(run)



mysum(1,2,3,4,5,sumi=4)
# guessing_game()