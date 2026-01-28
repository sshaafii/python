


def resteraunt():

    menu = {'apple':1,'cake': 4,'oreo':5, 'bread': 3}

    total = 0

    while True:

        item = input("Enter the item: ")

        if item in menu:
              total += menu[item]
              print(f'{item} costs {menu[item]}, total is {total}')
        elif item != '' and item not in menu:
             print("Enter an item on the menu")
        elif item == '':
             print(f'your total is {total}')
             break
        
# dicts can be created in different ways


import datetime
from datetime import date

def age_calc():

     dob = {'shaafi':date(2001,7,1),'john':date(1989,9,4),'sally':date(1976,6,23)}

     while True:


        
          name = input("Enter name: ")

          if not name:
               break
          
          dob1 = input("Enter date like '20191204': ")

          today = date.today()

          if name in dob:
               print(f'{name} is {(today - dob[name]).days}')
          else:
               print("not in system")




age_calc()









        

    


#resteraunt()
