from travelToolbox import readItems, readTransactions
import tkinter as tk
from tkinter import Text, END

class myApp(tk.Tk):
    def __init__(self, itemRecords) :
        tk.Tk.__init__(self)
        self.itemRecords = itemRecords

        self.grid()

        self.entry = tk.Entry(self)
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
        self.clear()
        content = self.entry.get()
        print(content)
        IDLabel = tk.Label(self, anchor="w", text='ID', font = "Calibri 14 bold")
        IDLabel.grid(column=0,row=0)
        NameLabel = tk.Label(self, anchor="w", text='Name', font = "Calibri 14 bold")
        NameLabel.grid(column=0,row=1)
        StartLabel = tk.Label(self, anchor="w", text='Start', font = "Calibri 14 bold")
        StartLabel.grid(column=0,row=2)
        EndLabel = tk.Label(self, anchor="w", text='End', font = "Calibri 14 bold")
        EndLabel.grid(column=0,row=3)
        # self.T = Text(self, height=4, width=50)
        # self.T.grid(column=0,row=2)
        # self.T.insert(END, "hello")
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
