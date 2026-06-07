from datetime import datetime

path = (r"C:\PythonFiles\ZooData.csv")

# This application displays a spreadsheet automation menu
# and converts temperature data from Fahrenheit to Celsius.

print("corger5719 Spreadsheet Automation Menu")
print("1. Input Data")
print("2. View Current Data")
print("3. Generate Report\n")

# The next line retrieves the inputted option and stores into the variable choice.
choice = input("Enter your menu option: \n")


# This function converts Fahrenheit temperature data to Celsius.
def convertData(fahrenheit):
    celsius = f"{(fahrenheit - 32) * 5 / 9:.0f}"
    return celsius


# This function appends comma-separated data to a csv file.
def insertData(data, path = r"C:\PythonFiles\ZooData.csv"):
    try:
        file = open(path, "a")
        file.write(data + "\n")
        file.close()
        return True
    except:
        print("Error: Data could not be written to the file.")
        return False


# This function reads and displays the contents of a csv file.
def viewData(path):
    try:
        file = open(path, "r")
        print("\nReading file from:", path)
        print(file.read())
        file.close()
    except:
        print("Error: File could not be read.")


# This function gathers user input, converts the data, and saves it to ZooData.csv.
def getInput():
    try:
        entries = int(input("How many entries are being entered? \n"))

        for entry in range(entries):
            date = input("Enter the date: \n")
            temperature = float(input("Enter the highest temperature for the inputted date in Fahrenheit: \n"))

            convertedValue = convertData(temperature)

            data = date + "," + str(temperature) + "," + str(convertedValue)

            saved = insertData(data, "ZooData.csv")

            if saved:
                print("The following data was saved at", datetime.now(), ":", data)

    except:
        print("Error: Invalid data was entered.")


# Conditional logic controls which menu option runs.
if choice == "1":
    getInput()
elif choice == "2":
    viewData("ZooData.csv")
else:
    print("Error: The chosen functionality is not implemented yet")
