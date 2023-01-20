from tkinter import *
from tkinter import ttk

"""Code for the currency converter, supports basic convertion (as of January 2023) addition of new currency (does not suppport favorite currency)"""

#MainWindow parameter
mainWindow = Tk()
mainWindow.geometry("440x200")
mainWindow.title("Currency Change")

#Dict of available currency, changes when you're adding a new one
currencies = {"EUR":1.0, "USD":0.92, "JPY":0.0071, "CNY":0.14}

#Variables for the different features, amount, result and rate are straightforward, but change is there to store to currency that were chosen for the conversion
amount = 0.0
rate = 0.0
change = ["", ""]
result = 0

#Configures the frame, could have worked without it but got used to work in this way, resultLabel is what it says to be
entriesFrame = Frame(mainWindow)
entriesFrame.pack(expand=True, fill="both")
resultLabel = Label(entriesFrame, text=f"{result}", font=("Arial", 15, "bold"))
resultLabel.grid(row=4, column=1, pady=10)

#Function that actually converts the amount and prints it in resultLabel, handles errors
def Convert():
    global amount, change, result
    try:
        if amount.get().isalnum():
            result = float(amount.get()) * float(currencies[change[0].get().upper()]) / float(currencies[change[1].get().upper()])
            resultLabel.config(text=f"{round(result, 2)} {change[1].get()}", font=("Arial", 15, "bold"), foreground="black")
    except:
        resultLabel.config(text=f"Invalid amount input", font=("Arial", 10), foreground="red")

#Function that adds a new currency to the dict, checks if the inputed currency is already present in the dict and adds it, handles errors as well
def Add():
    global rate, change
    try:
        if rate.get().isalnum() == False and change[0].get().upper() in currencies:
            resultLabel.config(text=f"Rate invalid or currency exists", font=("Arial", 10), foreground="red")
        else:
            currencies.update({change[0].get().upper():rate.get()})
            resultLabel.config(text=f"New currency added", font=("Arial", 10), foreground="green")
        for i in range(2):
            change[i].config(values=list(currencies.keys()))
    except:
        resultLabel.config(text=f"Rate invalid or currency exists", font=("Arial", 10), foreground="red")

#Sets up all the different widgets in the frame
def SetUpFrame():
    global amount, change, rate
    combox = ["From: ", "To: "]
    paddingY = 5
    paddingX = 10
    for i in range(3):
        if i == 0:
            amountLabel = Label(entriesFrame, text="Amount: ")
            amountLabel.grid(row=0, column=0, padx=paddingX, pady=paddingY)
            amountEntry = Entry(entriesFrame)
            amountEntry.grid(row=0, column=1)
            amount = amountEntry
        else:
            currencyLabel = Label(entriesFrame, text=combox[i-1])
            currencyLabel.grid(row=i, column=0, padx=paddingX, pady=paddingY)
            if i == 1:
                rateLabel = Label(entriesFrame, text="Rate: ")
                rateLabel.grid(row=i, column=2, padx=paddingX, pady=paddingY)
                rateEntry = Entry(entriesFrame, width=10)
                rateEntry.grid(row=i, column=3)
                addCurr = Button(entriesFrame, text="Add", command=Add)
                addCurr.grid(row=i, column=4, padx=paddingX)
                rate = rateEntry

            currCombo = ttk.Combobox(entriesFrame, values=list(currencies.keys()))
            currCombo.grid(row=i, column=1)
            change[i-1] = currCombo

    converter = Button(entriesFrame, text="Convert", command=Convert)
    converter.grid(row=3, column=1)



def main():
    SetUpFrame()
    mainWindow.mainloop()





if __name__ == "__main__":
    main()