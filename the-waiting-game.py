import random
import time

def waiting_game():
    target_time=random.randint(2,4)
    print(f"\n Your target time is {target_time} seconds")
    input("----Press Enter to Begin----")
    # for measuring very small time counts
    start=time.perf_counter()

    input(f"\n---Press Enter again after {target_time} seconds---")
    elapsed_time=time.perf_counter()-start

    print(f"\n Elapsed time: {elapsed_time:.3f} seconds")
    if elapsed_time==target_time:
        print("Unbelievable! Perfect timing")
    elif elapsed_time<target_time:
        print(f"{target_time-elapsed_time: .3f} seconds too fast")
    else:
        print(f"{elapsed_time-target_time: .3f} seconds too slow")        


waiting_game()        