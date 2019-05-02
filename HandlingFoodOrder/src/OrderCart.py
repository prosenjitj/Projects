import math
from collections import deque
import time
import pickle
from src.StandardCart import StandardCart

# Persist Data for Transform Existing CART
class Cart(StandardCart) :

    def __init__(self, order , seq) :
        self.name = order['name']
        self.service = order['service']
        self.orderItems = order['items']
        self.seq_id = seq
        self.orderId = math.ceil(time.time() * 1000) + seq
        self.totalCost = 0
        self.totalWaitTime = 0

    # Transform and Load Queue as per request
    def splitMore(self , itemsFromMenu , numOfParallelProcess):
        tasks = deque()
        # Loop through Each Items
        for item in self.orderItems :
            try :
                processTime = itemsFromMenu[item['name']]
                self.totalCost += item['price_per_unit'] * item['quantity']
                self.totalWaitTime += int(processTime * item['quantity'] / numOfParallelProcess)
                # Based on Quatity again split Orders in mutiple Pieces
                for _ in range(item['quantity']) :
                    tasks.append(str(self.orderId) + '\t' + str(self.seq_id) + "\t" + item['name'] + '\t\t\t' + str(item['quantity']) + '\t'+ str(processTime) + '\t' + self.service)
            except :
                print('Data is not correct', item)
        return tasks

    def __len__(self):
        return len(self.self.tasks)

    def __contains__(self, member):
        return member in self.__members

    def persistIn(self, object, filePath):
        # open a file, where you ant to store the data
        with open(filePath, 'wb') as file:
            # dump information to that file
            pickle.dump(object, file)

