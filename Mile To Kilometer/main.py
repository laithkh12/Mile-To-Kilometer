from tkinter import *

def milesToKilometer():
    miles = float(milesInput.get())
    km = round(miles * 1.609)
    kilometerResultLabel.config(text=f"{km}")

window = Tk()
window.title('Miles To Kilometer Converter')
window.configure(padx=20, pady=20)


milesInput = Entry(width=7)
milesInput.grid(column=1, row=0)

milesLabel = Label(text='Miles')
milesLabel.grid(column=2, row=0)

isEqualLabel = Label(text='Is Equal To')
isEqualLabel.grid(column=0, row=1)

kilometerResultLabel = Label(text='0')
kilometerResultLabel.grid(column=1, row=1)

kilometerLabel = Label(text='Km')
kilometerLabel.grid(column=2, row=1)

calculateButton = Button(text='Calculate', command=milesToKilometer)
calculateButton.grid(column=1, row=2)



window.mainloop()