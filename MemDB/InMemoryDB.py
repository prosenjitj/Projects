import sched, time, threading


class InMemoryDB():
    def __init__(self, range=2, timeOut=200):
        self.range = range
        self.timeOut = timeOut
        self.inMemoryStorage = {}  # Usage as DB Table
        self.lastAccessIndex = {}
        self.nameIndex = {}
        self.ageIndex = {}

    def getCurrentTime(self):
        return int(round(time.time() * 1000))

    # Patient Object  -----------
    class Patient():
        def __init__(self, parent=None, seq_id=0, patient=None, age=None, cancer=None):
            self.parent = parent
            self.lastAccessed = parent.getCurrentTime()
            self.seq_id = seq_id
            self.patient = patient
            self.age = age
            self.cancer = cancer

        def updateLastRead(self):
            self.lastAccessed = self.parent.getCurrentTime()
            return self.lastAccessed

        def getSeqId(self):
            return self.seq_id
            # ------- Class End ------

    def readData(self, seqIds=[]):
        # readData(self , seqIds=[])
        output = []
        # Read from buffer
        if len(seqIds) > 0 :
            seqCopy = []
            for key in seqIds :
                if key in self.inMemoryStorage :
                    p = self.inMemoryStorage[key]
                    if int(p.lastAccessed) in self.lastAccessIndex :
                        del self.lastAccessIndex[int(p.lastAccessed)]
                    self.lastAccessIndex[int(p.updateLastRead())] = key # which will save from early delete
                    output.append([str(p.seq_id), p.patient, str(p.age), p.cancer])
                else :
                    seqCopy.append(key)
            # Nothing left to read , Exit
            if len(seqCopy) == 0 :
                return output
            else :
                seqIds = seqCopy


        # Read from File Again
        with open('/Users/prosenjitdas/Desktop/orderdata/csv/2.csv', 'r') as csvFile:
            lineNumber = 0
            for line in csvFile:  ## Read line one by one
                valArr = line.strip().split(',')

                # If requested sequence Id is present , it will ignore others
                if lineNumber == 0:
                    lineNumber += 1
                    continue

                if len(seqIds) > 0 and lineNumber not in seqIds:
                    lineNumber += 1
                    continue

                p = None
                # Load data if it is not present
                if lineNumber not in self.inMemoryStorage.keys():
                    # Add Each Row
                    p = self.Patient(self, lineNumber, valArr[0], valArr[1], valArr[2])
                    self.inMemoryStorage[lineNumber] = p
                    self.lastAccessIndex[int(p.lastAccessed)] = lineNumber

                    # Add Name Index
                    if p.patient in self.nameIndex:
                        if lineNumber not in self.nameIndex[p.patient]:
                            self.nameIndex[p.patient].append(lineNumber)
                    else:
                        self.nameIndex[p.patient] = [lineNumber]

                    # Add Age Index
                    if p.age in self.ageIndex:
                        if lineNumber not in self.ageIndex[p.age]:
                            self.ageIndex[p.age].append(lineNumber)
                    else:
                        self.ageIndex[p.age] = [lineNumber]

                else:
                    p = self.inMemoryStorage[lineNumber]
                    if int(p.lastAccessed) in self.lastAccessIndex :
                        del self.lastAccessIndex[int(p.lastAccessed)]
                    self.lastAccessIndex[int(p.updateLastRead())] =  lineNumber # which will save from early delete

                output.append([str(p.seq_id), p.patient, str(p.age), p.cancer])
                # interrupt the storage for limited memory
                if self.range != -1 and lineNumber >= self.range:
                    break
                lineNumber += 1

            return output

    def cleanUpData(self):
        # Find the assignment which was not used for last 4 min
        currentTime = self.getCurrentTime() - (4 * 60 * 1000)
        if len(self.lastAccessIndex) > 0:
            lastAccessArr = list(self.lastAccessIndex.keys()).sort()
            offset = self.binarySearch(lastAccessArr, currentTime)
            # Delete all records right side of Offset
            for patIndx in lastAccessArr[lastAccessArr.index(offset):]:
                del self.inMemoryStorage[patIndx]


    # find the value close to Target
    def binarySearch(self, searchArr, searchVar):
        if not searchArr or len(searchArr) == 0:
            return -1

        if len(searchArr) < 2:
            return searchArr[0]

        mid = int(len(searchArr) / 2)
        if searchVar < searchArr[mid]:
            val = self.binarySearch(searchArr[:mid], searchVar)
        else:
            val = self.binarySearch(searchArr[mid:], searchVar)
        return val

    def findByNameData(self, name):
        outputs = seq_ids = []
        if len(self.nameIndex) > 0:
            seq_ids = self.nameIndex[name]

        # Take all of them buffer
        if len(seq_ids) > 0:
            outputs = self.readData(seq_ids)
        return outputs

    def findByAgeData(self, age):
        outputs = []
        if len(self.ageIndex) == 0:
            return None

        ages = sorted(list(map(lambda ag: int(ag.strip()), self.ageIndex.keys())))
        # ages = list(self.ageIndex.keys()).sort()
        findVal = self.binarySearch(ages, age)  # Find all records age is less than #Target
        if findVal == -1:
            return None

        idxExist = ages.index(findVal)
        eligbl_ages = ages[:(idxExist + 1)]

        # Get all seq
        seq_ids = []
        for ag in eligbl_ages :
            seq_ids.extend(self.ageIndex[str(ag)])

        # Take all of them buffer
        if len(seq_ids) > 0:
            outputs = self.readData(seq_ids)
        return outputs

    # Report
    def printReport(self, patientArr, seperator):
        for p in patientArr:
            print(seperator.join(p))


def main():
    range = int(input())
    inMob = InMemoryDB(range)
    # CleanUpJob
    sch = sched.scheduler(time.time, time.sleep)
    event = sch.enterabs(inMob.timeOut, 1, inMob.cleanUpData, ())
    sch.run()

    # manual data transfer
    inMob.readData()

    while True:
        popedVal = None
        try :
            print("Enter: 1. FindAll Patient By Name 'John' , 2. Find all Patient Age below 77 and 0. Exctentt")
            swipeIn = int(input())
            if swipeIn == 0:
                sch.cancel(event)  # cancel cleanup
                break
            elif swipeIn == 1:
                print("Enter Name")
                popedVal = inMob.findByNameData(str(input()))
            elif swipeIn == 2:
                print("Enter Age")
                popedVal = inMob.findByAgeData(int(input()))

            if not popedVal or len(popedVal) == 0:
                print("Data Not Found")
            else:
                inMob.printReport(popedVal, '-->')  # Print transactions

        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()



# Sample DB File :
# patient,age,cancer
# John,77,prost
# John1,78,prost
# John2,79,prost
# John,77,prost
# John1,78,prost
#
# > python3 <filename>.py
# > -1 # Get all Data
#
# # For Name Aggregation
# > 1
# # For Age Aggregation
# > 2
