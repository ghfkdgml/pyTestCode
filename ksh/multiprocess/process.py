import multiprocessing as mp
import time

def dryer(input):
    while 1:
        dish=input.get()
        if dish=='exit':
            print("done")
            break
        print("result:",dish)
    return False

dish_queue=mp.JoinableQueue()
proc=mp.Process(target=dryer,args=(dish_queue,))
proc.daemon=True
proc.start()

dishes=['salad','bread','exit']
for x in dishes:
    dish_queue.put(x)

if dish_queue.get()=='exit':
    print("done2")
    proc.terminate()
    if not proc.is_alive():
        proc.join()       
dish_queue.join()
