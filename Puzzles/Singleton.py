class Singleton:
    __instance = None
    # @staticmethod
    def getInstance():
        data = 'Initiated123'
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def getDataInstance(self):
        return self.data

    def __init__(self):
        self.data = 'Initiated'
        """ Virtually private constructor. """
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self


# s = Singleton()
# print(s.data)

s = Singleton.getInstance()
print(s.data)

s = Singleton.getInstance()
print(s.getDataInstance())
