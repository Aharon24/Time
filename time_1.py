import time



def alltime() :
    while True :
        try :   
            hour , minute, second = map(int,input("Insert time to count down (h:m:s)").split(":"))
            a  = (hour * 3600) +(60 * minute) + (second)
            return a 
        except ValueError :
            print("Invalid input. Please enter the time in the format 'h:m:s'")
        else:
             hour , minute, second = map(int,input("Insert time to count down (h:m:s)").split(":"))

def convert_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def caunt(seconds):
    while seconds > 0 :
        print(f"Time remaining: {convert_time(seconds)}")
        time.sleep(1)
        seconds -= 1
    print("finish")

secondd = alltime()
caunt(secondd)





