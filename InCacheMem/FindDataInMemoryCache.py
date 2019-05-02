from collections import deque


class InMemoryCache() :

    def __init__(self , range=2) :
        self.range = range
        self.fixedArray = [None] * range
        self.tail = 0
        self.head = 0
        self.inMemoryStorage = deque()

    def push(self , val):
        if self.tail < self.range:
            self.fixedArray[self.tail] = val
            self.tail += 1
        elif self.head > 0:
            self.fixedArray[0] = val
            self.tail = 1
        else :
            self.inMemoryStorage.append(val)

    def pop(self):
        value = 0

        if self.head >= self.range:
            self.head = 0

        value = self.fixedArray[self.head]
        if value :
            # Fill up the gap
            if len(self.inMemoryStorage) > 0 :
                validData = self.inMemoryStorage.popleft()
                if validData:
                    self.fixedArray[self.head] = validData
            else :
                self.fixedArray[self.head] = None
            # increase head
            self.head += 1

        return value

    # Report
    def printReport(self , statement ,seperator):
        print(seperator.join(statement))

def main():
    range = int(input())
    inMob = InMemoryDB(range)

    while True:
        try :
            print("Enter: Negetive to Pop and Zero to exit")
            swipeIn = int(input())
            if swipeIn == 0 :
                break
            elif swipeIn < 0 :
                popedVal = inMob.pop()
                if popedVal :
                    print(popedVal) # Swipe-out transaction
                else :
                    print("No data")
            else :
                inMob.push(swipeIn)
        except Exception as e: print(e)
            # print("Try Again !!")


if __name__ == '__main__':
    main()
