# your code goes here!
def countdown(count):
    for i in range(count, 0, -1):                      #count is the starting number, 
        print(f'{i} SECOND(S)!')                       #0 is the end of the range, itself not included
    print("HAPPY NEW YEAR!")                           #-1 is the decrement after each iteration


def countdown_with_sleep(count):                            
    for i in range(count, 0, -1):                      
        print(f'{i} SECOND(S)!')                       
    print("HAPPY NEW YEAR!")
