from PyQt4 import QtGui, QtCore
import sys
import design_new
import time
import xlrd
import functions
import os
import shutil

sys.setrecursionlimit(1500)

class ExampleApp(QtGui.QMainWindow, design_new.Ui_MainWindow, functions.Functions):
	def __init__(self):
		self.flag = 1
		self.folder_path = "/home/pratik/Documents/PyQt/PickProjection/in/"

		super(self.__class__, self).__init__()
		self.setupUi(self)
		self.pushButton.clicked.connect(self.next)
	
	def check(self,x,y):
		
		if y==x:
			self.label.setText("Good Job")
			self.quantity.setText("Pick")
			self.go(x)
			QtCore.QCoreApplication.processEvents()
			time.sleep(2)
			self.reset()
			QtCore.QCoreApplication.processEvents()
			self.i += 1

			if self.i < self.len_sheet:
				self.next()
			else:
				self.label.setText("All items of the sheet completed")
				self.flag = 1
				shutil.move(self.folder_path + self.list[0], "/home/pratik/Documents/PyQt/PickProjection/out/" + self.list[0])
				self.next()

		
		else:
			self.label.setText("Pick from the Yellow Blinking Box")
			self.wrong()
			QtCore.QCoreApplication.processEvents()
			time.sleep(2)
			self.reset()
			QtCore.QCoreApplication.processEvents()
			prev_y = y
			
			while y == prev_y:

				self.Boxes[x-1].setAutoFillBackground(True)
					
				self.flashLbl(x-1)
				QtCore.QCoreApplication.processEvents()

				f = open("test.txt", "r")
				data = f.read()
				y = int(data)
				f.close()

				QtCore.QCoreApplication.processEvents()
				time.sleep(0.25)
			
			self.check(x,y)

	def sogaya(self):
		time.sleep(5)
		self.flag = 1
		self.next()


	def next(self):

		if self.flag == 1:
			self.list = (os.listdir(self.folder_path))
			if len(self.list) == 0:
				self.sogaya()

			else:
				self.wb = xlrd.open_workbook(self.folder_path + self.list[0])
				self.sheet = self.wb.sheet_by_index(0)
				self.i = 0
				self.len_sheet = self.sheet.nrows

		self.flag = 0
        	
		f = open("test.txt", "w")
		f.write('0')
		f.close()

		x = (int(self.sheet.cell_value(self.i, 0)))
		pick = (int(self.sheet.cell_value(self.i, 1)))
		self.label.setText("Pick from the Blinking Box")
		self.quantity.setText("Pick {} Units".format(pick))

		f = open("test.txt", "r")
		data = f.read()
		y = int(data)
		f.close()

		self.lblWhite=True

		while y == 0:
			self.Boxes[x-1].setAutoFillBackground(True)
				
			self.flashLbl(x-1)
			QtCore.QCoreApplication.processEvents()

			f = open("test.txt", "r")
			data = f.read()
			y = int(data)
			f.close()
				
			QtCore.QCoreApplication.processEvents()
			time.sleep(0.25)

		self.check(x,y)	

		return



def main():
	app = QtGui.QApplication(sys.argv)
	form = ExampleApp()
	form.show()
	app.exec_()

if __name__ =='__main__':
	main()
