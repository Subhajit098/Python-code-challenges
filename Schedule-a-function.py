# Write a function to schedule another given function to execute at a specified time.

# The function has three inputs event time,function,any number of arguments

import sched
import time

def schedule_function(event_time,function,*args):
    schedular=sched.scheduler(time.time,time.sleep)
    schedular.enterabs(event_time,1,function,argument=args)
    print(f"{function.__name__}() scheduled for {time.asctime(time.localtime(event_time))}")
    schedular.run()

schedule_function(time.time()+1,print,"Hello World!")    
