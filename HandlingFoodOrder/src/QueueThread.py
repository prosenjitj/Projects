import threading
import time
from src.ThreadStruct import ThreadStruct

# Persist Data for Transformation the Existing CART
class QueueThread(ThreadStruct):
    def __init__(self, numOfParallel, dataQueue):
        self.numOfParallel = numOfParallel
        self.dataQueue = dataQueue

    def run(self):
        try:
            # Process Streaming and collect Threads
            processes = []
            for indx in range(self.numOfParallel):
                processes.append(
                    threading.Thread(target=self.processAllDataFromQueue, args=(self.dataQueue[indx], indx)))

            # Start All Threads
            for proc in processes:
                proc.start()

            # wait until threads are completely executed
            for proc in processes:
                proc.join()
        except:
            print("Error : Exception in Thread processing")

    # Thread Function
    def processAllDataFromQueue(self, cartInQueue, indx):
        # Get the orders from Queue and execute
        while cartInQueue:
            p = cartInQueue.popleft()
            # Execute the Order
            print(indx, '--> CART: ', p)
            time.sleep(1)
