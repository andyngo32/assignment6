from travelToolbox import readItems, readTransactions
import tkinter as tk
from tkinter import Text, END

import pprint

class myApp(tk.Tk):
    def __init__(self, itemRecords) :
        tk.Tk.__init__(self)
        self.itemRecords = itemRecords

        self.grid()

        self.entry = tk.Entry(self, state=tk.NORMAL)
        self.entry.grid(column=1,row=0)

        button1 = tk.Button(self,text="Show",
                            command=self.showStockItem)
        button1.grid(column=2,row=0)

        button2 = tk.Button(self,text="Quit",
                                command=self.quitit)
        button2.grid(column=1,row=1)

        label = tk.Label(self, anchor="w", text='Item ID')
        label.grid(column=0,row=0)

    def showStockItem(self):
        entryText = self.entry.get()

        if len(entryText) == 0:
            print("ItemID cannot be empty.")
            self.quitit()
            return
        elif str(entryText) not in self.itemRecords.keys():
            print("ItemID {} does not exist. Please enter a valid ItemID.".format(entryText))
            self.quitit()
            return
        else:
            self.clear()
            record = self.itemRecords[str(entryText)]

            self.T = Text(self, height=10, width=40)
            self.T.pack()
            self.T.insert(END, "ID\t{}\nName\t{}\nStart\t{}\nEnd\t{}\n".format(record.itemID,
                          record.itemName, record.getAvailableStart(), record.getAvailableEnd()))

        return

    def clear(self):
        for l in self.grid_slaves():
            l.destroy()


    def quitit(self):
        self.destroy()
        return


itemsFileName = "items4.csv"
transactionsFileName = "transactions4.csv"

# itemRecords is a dictionary of stockItem records indexed by item ID
itemRecords = {}

# Read the items from itemsFileName into itemRecords
readItems(itemsFileName, itemRecords)

# Read the transactions from transactionsFileName into itemRecords
readTransactions(transactionsFileName, itemRecords)

app = myApp(itemRecords)
app.title('Travel')
app.mainloop()
