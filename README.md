# 🛠️ Miles to Kilometer Converter

This program is a simple GUI-based application built with Python's `tkinter` library. It converts a user-entered value in miles to kilometers, using a conversion factor of 1 mile = 1.609 kilometers.

## 📂 Project Structure

- **Input Field**: Entry box for user input in miles.
- **Labels**: Display text labels for "Miles," "Is Equal To," and "Km."
- **Result Display**: Shows the converted value in kilometers.
- **Calculate Button**: Button to trigger the conversion.

---

## 🔧 Code Explanation

### 1. Conversion Function
```python
def milesToKilometer():
    miles = float(milesInput.get())
    km = round(miles * 1.609)
    kilometerResultLabel.config(text=f"{km}")
```
- milesToKilometer: Converts the miles input to kilometers and updates the result label with the computed value.

### 2. GUI Setup
```python
from tkinter import *

window = Tk()
window.title('Miles To Kilometer Converter')
window.configure(padx=20, pady=20)
```
- Window Configuration: Creates a Tkinter window, sets the title, and adds padding for spacing.

### 3. Widgets
```python
# Input for miles
milesInput = Entry(width=7)
milesInput.grid(column=1, row=0)

# Labels for Miles, Km, and "Is Equal To"
milesLabel = Label(text='Miles')
milesLabel.grid(column=2, row=0)

isEqualLabel = Label(text='Is Equal To')
isEqualLabel.grid(column=0, row=1)

kilometerResultLabel = Label(text='0')
kilometerResultLabel.grid(column=1, row=1)

kilometerLabel = Label(text='Km')
kilometerLabel.grid(column=2, row=1)
```
- Entry Widget: Accepts the user’s miles input.
- Label Widgets: Display static text for labels and show the result in kilometers.

### 4. Calculate Button
```python
calculateButton = Button(text='Calculate', command=milesToKilometer)
calculateButton.grid(column=1, row=2)
```
- Button: The "Calculate" button, which triggers the milesToKilometer function


## 🚀 How to Run
1. Make sure Python is installed on your system.
2. Run the program with:
```bash
python main.py
```
3. Enter a value in miles and click "Calculate" to see the equivalent distance in kilometers.

## 📝 Notes
- Conversion Formula: This uses the formula km = miles * 1.609.
- Rounded Output: The result is rounded for simplicity.

## 🔗 Additional Resources
- tkinter Documentation
- Miles to Kilometers Conversion
