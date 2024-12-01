from graphics import *

class Button:

    def __init__(self, win, center, width, height, label):
        '''Calculated the half of width and height to calculate the points to define the rectangle'''
        w, h = width / 2, height / 2
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x + w, x - w
        self.ymax, self.ymin = y + h, y - h

        '''Creating the points that will help to define the rectangle'''
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.active = True
        self.rect = Rectangle(p1, p2)
        self.rect.setFill("lightblue")
        self.rect.draw(win)

        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    '''checks if the button is clicked'''
    def clicked (self, p):
        insideX = self.xmin <= p.getX() and p.getX() <= self.xmax
        insideY = self.ymin <= p.getY() and p.getY() <= self.ymax
        self.active = True
        return self.active and insideX and insideY

    '''gets the button label'''
    def getLabel(self):
        return self.label.getText()

    '''activates button'''
    def activate(self):
        self.label.setFill("black")
        self.rect.setWidth(2)
        self.active = True

    '''deactivates button'''
    def deactivate(self):
        self.label.setFill("red")
        self.rect.setWidth(1)
        self.active = False