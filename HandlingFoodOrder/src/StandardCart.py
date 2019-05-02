class StandardCart() :

    # Load Queue as per request
    def splitMore(self , itemsFromMenu , numOfParallelProcess): raise NotImplementedError

    def persistIn(self, object, filePath):raise NotImplementedError

    def __len__(self):  raise NotImplementedError

    def __contains__(self, member):  raise NotImplementedError
