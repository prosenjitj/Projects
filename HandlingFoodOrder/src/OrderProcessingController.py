import json
import pandas as pd
from collections import deque

from src.OrderCart import Cart
from src.Graph import Graph
from src.ThreadImpl import QueueThread


class OrderProcessingController:
    def __init__(self,
                 menuTxtFile=None,
                 orderTxtFile=None,
                 tempFolder=None,
                 numOfParallel=0):
        self.itemTxtFile = menuTxtFile
        self.orderTxtFile = orderTxtFile
        self.tempFolder = tempFolder
        self.numOfParallel = numOfParallel

    def dataProcessing(self):
        # Get Constant Data
        itemsFromMenu = self.getItems ()
        if len(itemsFromMenu)  == 0 :
            print('Items are missing')
            return

        # Get All orders
        queue , dataframe = self.getOrders (itemsFromMenu)
        if len(itemsFromMenu)  == 0 :
            print('Orders are missing')
            return

        if not queue or dataframe.size == 0 :
            print('Queue / Data Table not found')
            return

        # Run all Threads
        print('\n#Thread Id\t#Order Id\t Priority\t\tItem(Same Orders)\t\t\tQuantity\tWait Time\tService Name')
        print('-' * 150)
        QueueThread(self.numOfParallel , queue).run()

        # Get Report for Data Processing
        graph = Graph(self.numOfParallel , dataframe)
        print("Please select below options :\n1. Order-Cost Graph ")
        print("2. Oreder-Wait Time Graph\n3. Close")
        switcher = {
            1: graph.totalCostBasedOnService,
            2: graph.totalWaitingTimeBasedOnService
        }

        while True :
            try :
                select = int(input().strip())
                print('Input ::' , select)
                func = switcher.get(select, "nothing")
                graph.closeAll()

                if select == 3 :
                    break
                elif func == "nothing" :
                    print("Doesn't match , try again !!")
                else :
                    # Execute the function
                    func()
            except :
                print("Wrong Entry !!")



    # Get items
    def getItems(self):
        itemsFromMenu = {}
        # Build Item as constant
        with open(self.itemTxtFile, 'r') as json_file:
            data = json.load(json_file)
            for p in data:
                itemsFromMenu.update([(p['name'], p['cook_time'])])
        return itemsFromMenu



    # Get Orders in Stream
    # Break Orders into small pieces based on items
    # Add to Queue
    def getOrders(self, itemsFromMenu):
        cartListFromOrderHistory = []
        # Get Json in Chunk
        fileQueue = [deque()] * self.numOfParallel
        print('#Order Id\t\tCustomer Name\t\tService Name \t\tCost\t\tWait Time')
        print('-' * 150)

        with open(self.orderTxtFile, 'r') as json_file:
            data = json.load(json_file)
            count = 1
            try :
                for p in data:
                    cart = Cart(p, count)
                    # Create Task as per request - Lazy loading
                    tasks = cart.splitMore(itemsFromMenu , self.numOfParallel)
                    # Display Order Details
                    print(cart.orderId, " \t ", cart.name, " \t\t ", cart.service, "\t\t", cart.totalCost,
                          "\t\t", cart.totalWaitTime)
                    count += 1
                    ind = 0
                    while tasks:
                        # Popup Task one by One and Add in Queue
                        fileQueue[ind].append(tasks.popleft())
                        ind += 1
                        if ind >= self.numOfParallel:
                            ind = 0
                    # End of While

                    # Prepare Cart Data for Persist
                    cartListFromOrderHistory.append(
                        [cart.orderId, cart.name, cart.service, cart.totalCost, cart.totalWaitTime])

                    # Persist for later used
                    cart.persistIn(cart , self.tempFolder + '/' + str(cart.orderId))

                    # For Testing
                    # if count > 100:
                    #     break
            except :
                print('Exception in adding data to queue')

            if len(cartListFromOrderHistory) > 0 :
                dataframe = pd.DataFrame(cartListFromOrderHistory,
                                     columns=['OrderId', 'Name', 'Service', 'TotalCost', 'Total Wait-Time'])

        return fileQueue, dataframe
