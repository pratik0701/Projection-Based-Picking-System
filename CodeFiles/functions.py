

class Functions:

    def flashLbl(self,i):
        if self.lblWhite == True:
            self.Boxes[i].setStyleSheet("QLabel{background-color : yellow;}")
            self.lblWhite = False
        else:
            self.Boxes[i].setStyleSheet("QLabel{background-color : white;}")
            self.lblWhite = True

    def go(self, x):
        self.Boxes[x-1].setStyleSheet("QLabel{background-color : green;}")
    

    def wrong(self):
        for i in range(8):
            self.Boxes[i].setStyleSheet("QLabel{background-color : red;}")

        

    def reset(self):
        for i in range(8):
            self.Boxes[i].setStyleSheet("QLabel{background-color : white;}")



