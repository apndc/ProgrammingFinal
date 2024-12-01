from graphics import *

class Menu:
    def __init__(self, win):
        #Initialize variables
        self.dishes = []  # Stores dish names
        self.prices = []  # Stores dish prices
        self.allOrders = []  #Stores all orders
        self.entries = []  #Stores quantity of dish

        '''Get dishes and prices from input file'''
        inputFile = open("menuInput.txt", "r")
        for line in inputFile:
            words = line.strip().split(",")
            self.dishes.append(words[0])
            self.prices.append(float(words[1]))
        inputFile.close()

        '''Prints each dish and entry point, allows for dishes to be added in the text file'''
        y_position = 7
        for i in range(len(self.dishes)):
            Text(Point(2, y_position), self.dishes[i]).draw(win)
            entry = Entry(Point(3, y_position), 5) #Entry is where user inputs number
            entry.setText("0") #Set original value of entry to 0
            entry.draw(win)
            self.entries.append(entry) #Add the number user enters into entries
            y_position -= 0.5 #Change the y value so that dishes are not printed on top of each other


    '''Gets the inputted values from user'''
    def getValues(self):
        quantities = []
        for entry in self.entries:
            quantity = entry.getText()
            if quantity.isdigit(): #Checks if quantity is a digit as it's a string
                quantities.append(int(quantity))
            else: #Accounts for 0 being entered
                quantities.append(0)
        return quantities


    '''Gets the price values from list and returns them'''
    def getPrice(self):
        return self.prices


    '''Calculates the cost and tax for current order submitted'''
    def calcBill(self):
        cost = 0
        tax = 0.05
        quantities = self.getValues()
        prices = self.getPrice()

        for i in range(len(quantities)):
            quantity = int(quantities[i])
            price = float(prices[i])
            itemCost = quantity * price
            cost += itemCost

        costTaxed = cost * (1+tax)
        self.allOrders.append(costTaxed) #Adds order to keep track of every order placed by user


    '''Prints the Bill and Average in output file'''
    def printBill(self):
        finalTotal = 0
        outFile = open("menuOutput.txt", "w")

        for order in self.allOrders: #Repeat for each order in allOrders
            print("Order Total (with tax) = $", format(order, '.2f'), file=outFile) #format and '.2f' makes it print to the 2nd decimal place
            finalTotal += order

        average = finalTotal / len(self.allOrders)
        print("\nTotal Cost (all orders) = $", format(finalTotal, '.2f'), file=outFile)
        print("Average Cost of Bill = $", format(average, '.2f'), file=outFile)


    '''Resets the entry number to 0 so user can see that its a new order'''
    def resetOrder(self):
        for entry in self.entries:
            entry.setText("0")