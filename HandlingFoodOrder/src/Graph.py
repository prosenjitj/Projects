from matplotlib import pyplot as plt

# Persist Data for Transformation the Existing CART
class Graph() :

    def __init__(self, numOfParallel, dataframe) :
        self.numOfParallel = numOfParallel
        self.dataframe = dataframe

    # Get Cost Chart Based on Services
    def totalCostBasedOnService(self):
        self.dataframe.groupby('Service')['TotalCost'].sum().plot(kind='bar')
        plt.show()

        # Join Services and get group by value
        return self.dataframe.groupby(['Service']).size().keys()


    # Get Wait Time Based on Services
    def totalWaitingTimeBasedOnService(self):
        self.dataframe.groupby('Service')['Total Wait-Time'].sum().plot(kind='bar')
        plt.show()

        # Join Services and get group by value
        return self.dataframe.groupby(['Service']).size().keys()

    def closeAll(self):
        plt.close('all')


