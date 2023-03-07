import sys
from PySide6.QtWidgets import *
from main_window import Ui_MainWindow
from PySide6.QtCore import QRect , Qt 
from PySide6.QtGui import QFont , QAction
from sudokugen.solver import solve
from sudoku import Sudoku
from functools import partial 
import random 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        global font  , cell_font
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.menu_new.triggered.connect(self.new_game) # chon az noe QAction hast az triggered estefade kardim 
        self.line_edits =  [[None for i in range(9)] for j in range(9)] #yek array 9x9 khali
        self.ui.menu_openfile.triggered.connect(self.open_file)
  
        font = QFont()
        font.setPointSize(16)
        cell_font =QFont()
        cell_font.setFamily(u"MS Shell Dlg 2")
        cell_font.setPointSize(12)

        for i in range(9):
            for j in range(9):
                #az jens qlineedit chon input mikhaim bedim 
                new_cell =  QLineEdit()
                self.ui.grid_Layout.addWidget(new_cell , i , j  , 1 , 1)
                new_cell.textChanged.connect(partial(self.validation , i , j))
                self.line_edits[i][j] = new_cell

                sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
                sizePolicy.setHeightForWidth(new_cell.sizePolicy().hasHeightForWidth())
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                self.grid_Layout = QGridLayout()
                self.grid_Layout.setSpacing(0)
                self.grid_Layout.setContentsMargins(0, 0, 0, 0)
                self.grid_Layout.setHorizontalSpacing(0)
                self.grid_Layout.setVerticalSpacing(0)
                new_cell.setGeometry(QRect(  0 ,0 ,40, 40))
                new_cell.setEnabled(True)
                new_cell.setSizePolicy(sizePolicy)
                new_cell.setAlignment(Qt.AlignCenter)
                new_cell.setFont(font)

        self.new_game()


    def new_game(self) :
        puzzle = Sudoku(3 , seed = random.randint(1 , 1000)).difficulty(0.5)  
        for i in range(9):
            for j in range(9):
                if puzzle.board[i][j] != None :
                    self.line_edits[i][j].setText(str(puzzle.board[i][j]))
                    self.line_edits[i][j].setReadOnly(True)
                else :
                    self.line_edits[i][j].setText("")



    def open_file(self):
        file_path = QFileDialog.getOpenFileName(self , "Open File...")[0] #address file ro mide dar khoone 0 az tuple 
        f = open(file_path , "r")
        # 1st : divide different rows
        # 2nd : 
        file_text = f.read()
        rows = file_text.split("\n")
        puzzle_board = [ [ None for i in range(9)] for j in range(9)]
        for i in range(len(rows)) :
            cells = rows[i].split(" ") #--> str
            for j in range(len(cells)):
                puzzle_board[i][j] = int(cells[j])
        for i in range(9):
            for j in range(9):
                self.line_edits[i][j].setReadOnly(False)
                if puzzle_board[i][j] != 0 :
                    self.line_edits[i][j].setText(str(puzzle_board[i][j]))
                    self.line_edits[i][j].setReadOnly(True)
                else :
                    self.line_edits[i][j].setText("")



    def check(self):
        for i in range(0 , 9):
            i= 0
            x = 0
            num1 = self.line_edits[i][x].text()                 
            if num1!= None :
                for j in range(1,9) :
                    other_numbers_in_row = self.line_edits[i][j].text()
                    if other_numbers_in_row != None :
                        if num1 == other_numbers_in_row :
                            self.line_edits[i][j].setStyleSheet(u"color: rgb(255, 0, 67);\n""background-color: rgb(255, 170, 255);\n""font: 75 16pt \"MS Shell Dlg 2\";")
                            #return False
                        else :
                            self.line_edits[i][j].setStyleSheet(u"color: rgb(0, 0, 0);\n""background-color: rgb(255, 255, 255);\n""font: 75 16pt \"MS Shell Dlg 2\";")

            for x in range(1,9):           
                num1 = self.line_edits[i][x].text()                 
                if num1!= None :
                    for j in range(0,9):
                        if j == x:
                            continue
                        other_numbers_in_row = self.line_edits[i][j].text()
                        if other_numbers_in_row != None :
                            if num1 == other_numbers_in_row :
                                self.line_edits[i][x].setStyleSheet(u"color: rgb(255, 0, 67);\n""background-color: rgb(255, 170, 255);\n""font: 75 16pt \"MS Shell Dlg 2\";")
                                #return False
                            else :
                                self.line_edits[i][x].setStyleSheet(u"color: rgb(0, 0, 0);\n""background-color: rgb(255, 255, 255);\n""font: 75 16pt \"MS Shell Dlg 2\";")

        for j in range(0 , 9):
            j= 0
            x = 0
            num1 = self.line_edits[x][j].text()                 
            if num1!= None :
                for i in range(1,9) :
                    other_numbers_in_row = self.line_edits[i][j].text()
                    if other_numbers_in_row != None :
                        if num1 == other_numbers_in_row :
                            self.line_edits[i][j].setStyleSheet(u"color: rgb(255, 0, 67);\n""background-color: rgb(255, 170, 255);\n""font: 75 16pt \"MS Shell Dlg 2\";")
                            #return False
                        else :
                            self.line_edits[i][j].setStyleSheet(u"color: rgb(0, 0, 0);\n""background-color: rgb(255, 255, 255);\n""font: 75 16pt \"MS Shell Dlg 2\";")

            for x in range(1,9):           
                num1 = self.line_edits[x][j].text()                 
                if num1!= None :
                    for i in range(0,9):
                        if i == x:
                            continue
                        other_numbers_in_row = self.line_edits[i][j].text()
                        if other_numbers_in_row != None :
                            if num1 == other_numbers_in_row :
                                self.line_edits[x][j].setStyleSheet(u"color: rgb(255, 0, 67);\n""background-color: rgb(255, 170, 255);\n""font: 75 16pt \"MS Shell Dlg 2\";")
                                #return False
                            else :
                                self.line_edits[x][j].setStyleSheet(u"color: rgb(0, 0, 0);\n""background-color: rgb(255, 255, 255);\n""font: 75 16pt \"MS Shell Dlg 2\";")






            # i = 0 
            # #j = n = 1 , 2, ... , 9
            # for n in range(1 , 8):
            #     for j in list(range(0 , n)) + list(range(n+1 , 9)) :
            #         num1 = self.line_edits[i][n].text() #first cell 
            #         other_numbers_in_row = self.line_edits[i][j].text() # neghbours of first cell in that row
            #         print(f"{num1} + {other_numbers_in_row}")
            #         if num1 == other_numbers_in_row  and  other_numbers_in_row != None and num1 != None :
            #             self.line_edits[i][j].setStyleSheet(u"color: rgb(255, 0, 67);\n""background-color: rgb(255, 170, 255);\n""font: 75 16pt \"MS Shell Dlg 2\";")
            #             return False

            #         else :
            #             self.line_edits[i][j].setStyleSheet(u"color: rgb(0, 0, 0);\n""background-color: rgb(255, 255, 255);\n""font: 75 16pt \"MS Shell Dlg 2\";")










    def validation(self , i , j , text): #check single number - between 0 to 9 
        #text = self.line_edits[i][j].text()
        if text not in ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"] :
            self.line_edits[i][j].setText("")

        if self.check() == True :
            msg_box = QMessageBox("you won")



if __name__ == "__main__":
    app = QApplication(sys.argv)  
    window = MainWindow()
    window.show()
    app.exec()
