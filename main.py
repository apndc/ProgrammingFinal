from graphics import *
from button import *
from Menu import *

def main():
    '''Establish window'''
    win = GraphWin("Restaurant", 1000, 800)
    win.setCoords(0,0,10,10)
    win.setBackground("purple")

    '''Draw buttons'''
    enterButton = Button(win,Point(2, 2), 2, 1, "Done!")
    quitButton = Button(win,Point(8,2), 2,1,"Close!")

    #Call menu
    showmenu = Menu(win)

    #Receive click from user
    point = win.getMouse()

    '''While there is a click / click is valid'''
    while point:
        '''If enter was clicked'''
        if enterButton.clicked(point):
            showmenu.calcBill() #Calculate the bill
            showmenu.resetOrder()  #Reset the entered numbers to 0

        #If close button was clicked
        elif quitButton.clicked(point):
            showmenu.printBill() #Print bill in output file
            win.close() #Close window
            break #End code
        '''Receive next click from user'''
        point = win.getMouse()

main()