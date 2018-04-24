class travelItem :
    def __init__(self, itemID, itemName, itemCount):
        self.itemID = itemID
        self.itemName = itemName
        self.itemCount = itemCount
        self.transactions = list()

    def getID(self) :
        return self.itemID

    def getName(self) :
        return self.itemName

    def setName(self, newName) :
        self.itemName = newName

    def getAvailableStart(self) :
        # todo: double check this
        return self.itemCount

    def appendTransaction(self, num) :
        self.transactions.append(num)

    def getTransactions(self) :
        return self.transactions

    def getReservations(self) :
        reservations = list()
        for num in self.transactions:
            if num >= 0:
                reservations.append(num)
        return reservations

    def getCancellations(self) :
        cancellations = list()
        for num in self.transactions:
            if num < 0:
                cancellations.append(num)
        return cancellations

    def getAvailableEnd(self) :
        return self.itemCount - sum(self.transactions)
