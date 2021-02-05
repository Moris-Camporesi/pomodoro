import time


def countdown(t): 
    t *= 60
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
      
    print("It's time for a break!") 
  
  
# input time in seconds 
t = input("Enter the time in minutes: ") 
  
# function call 
countdown(int(t)) 

