import PyQt5
from PyQt5 import QtWidgets
import processing
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1360, 726)
        self.centralwidget = PyQt5.QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("display: flex;\n"
                                         "position: absolute;\n"
                                         "width: 1366px;\n"
                                         "height: 726px;\n"
                                         "left: 0px;\n"
                                         "top: 0px;\n"
                                         "\n"
                                         "background: rgba(43, 43, 43, 0.63);")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = PyQt5.QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(PyQt5.QtCore.QRect(0, 0, 1366, 726))
        self.frame.setStyleSheet("display: flex;\n"
                                 "\n"
                                 "position: absolute;\n"
                                 "width: 1366px;\n"
                                 "height: 726px;\n"
                                 "left: 0px;\n"
                                 "top: 0px;\n"
                                 "\n"
                                 "background: rgba(43, 43, 43, 0.63);")
        self.frame.setFrameShape(PyQt5.QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(PyQt5.QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = PyQt5.QtWidgets.QLabel(self.frame)
        self.label.setGeometry(PyQt5.QtCore.QRect(0, -170, 1981, 1061))
        self.label.setStyleSheet("display: flex;\n"
                                 "position: absolute;\n"
                                 "width: 1366px;\n"
                                 "height: 726px;\n"
                                 "left: 0px;\n"
                                 "top: 0px;\n"
                                 "\n"
                                 "background: rgba(43, 43, 43, 0.63);")
        self.label.setText("")
        self.label.setPixmap(PyQt5.QtGui.QPixmap("Group 1.png"))
        self.label.setObjectName("label")
        self.pushButton = PyQt5.QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(PyQt5.QtCore.QRect(154, 480, 480, 72))
        font = PyQt5.QtGui.QFont()
        font.setFamily("Work Sans")
        font.setPointSize(1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "color: #FFFFFF;\n"
                                      "font-family: \'Work Sans\';\n"
                                      "font-style: normal;\n"
                                      "font-weight: 600;\n"
                                      "font-size: 24px;\n"
                                      "/*display: flex;\n"
                                      "flex-direction: row;\n"
                                      "justify-content: center;\n"
                                      "align-items: center;\n"
                                      "padding: 0px 50px;\n"
                                      "gap: 12px;*/\n"
                                      "position: absolute;\n"
                                      "width: 460px;\n"
                                      "height: 72px;\n"
                                      "background: #A259FF;\n"
                                      "border-radius: 20px;\n"
                                      "}\n"
                                      "")
        icon = PyQt5.QtGui.QIcon()
        icon.addPixmap(PyQt5.QtGui.QPixmap("img.png"), PyQt5.QtGui.QIcon.Normal, PyQt5.QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.clicked.connect(self.open_file)
        self.pushButton.setObjectName("pushButton")

        self.pushButtondir = PyQt5.QtWidgets.QPushButton("ЗАГРУЗИТЬ ПАПКУ",self.frame)
        self.pushButtondir.setGeometry(PyQt5.QtCore.QRect(154, 560, 480, 72))
        font = PyQt5.QtGui.QFont()
        font.setFamily("Work Sans")
        font.setPointSize(1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButtondir.setFont(font)
        self.pushButtondir.setAutoFillBackground(False)
        self.pushButtondir.setStyleSheet("QPushButton{\n"
                                      "color: #FFFFFF;\n"
                                      "font-family: \'Work Sans\';\n"
                                      "font-style: normal;\n"
                                      "font-weight: 600;\n"
                                      "font-size: 24px;\n"
                                      "/*display: flex;\n"
                                      "flex-direction: row;\n"
                                      "justify-content: center;\n"
                                      "align-items: center;\n"
                                      "padding: 0px 50px;\n"
                                      "gap: 12px;*/\n"
                                      "\n"
                                      "position: absolute;\n"
                                      "width: 460px;\n"
                                      "height: 72px;\n"
                                      "background: #A259FF;\n"
                                      "border-radius: 20px;\n"
                                      "}\n"
                                      "")
        icon = PyQt5.QtGui.QIcon()
        icon.addPixmap(PyQt5.QtGui.QPixmap("img.png"), PyQt5.QtGui.QIcon.Normal, PyQt5.QtGui.QIcon.Off)
        self.pushButtondir.setIcon(icon)
        self.pushButtondir.clicked.connect(self.open_dir)
        self.pushButtondir.setObjectName("pushButtondir")

        self.label_2 = PyQt5.QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(PyQt5.QtCore.QRect(118, 158, 533, 303))
        self.label_2.setStyleSheet(
            "box-sizing: border-box;\n"
            "/*display: flex;\n"
            "flex-direction: column;\n"
            "justify-content: center;\n"
            "align-items: flex-start;*/\n"
            
            "position: relative;\n"
            "width: 533px;\n"
            "height: 303px;\n"
            "background: linear-gradient(180deg, #9E68E3 0%, rgba(215, 56, 240, 0) 100%);\n"
            "background-blend-mode: overlay;\n")
        self.label_2.setText("")
        self.label_2.setPixmap(PyQt5.QtGui.QPixmap("New Member 4.png"))
        self.label_2.setObjectName("label_2")

        self.label_4 = PyQt5.QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(PyQt5.QtCore.QRect(300, 220, 151, 161))
        self.label_4.setStyleSheet("position: absolute;\n"
                                   "width: 50.47px;\n"
                                   "height: 49.94px;\n"
                                   "background: url(cross(1).png);\n"
                                   "transform: rotate(-45deg);\n"
                                   "")
        self.label_4.setText("")
        self.label_4.setPixmap(PyQt5.QtGui.QPixmap("img_1.png"))
        self.label_4.setObjectName("label_4")

        self.label_5 = PyQt5.QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(PyQt5.QtCore.QRect(700, 150, 600, 300))
        self.label_5.setLayoutDirection(PyQt5.QtCore.Qt.LeftToRight)
        self.label_5.setStyleSheet(
            "background-color: rgb();\n"
            "\n"
            "\n"
            "width: 592px;\n"
            "height: 210px;\n"
            "\n"
            "font-family: \'Work Sans\';\n"
            "font-style: normal;\n"
            "font-weight: 600;\n"
            "font-size: 64px;\n"
            "line-height: 110%;\n"
            "\n"
            "display: flex;\n"
            "align-items: center;\n"
            "text-transform: uppercase;\n"
            "color: #FFFFFF;\n"
            "flex: none;\n"
            "order: 0;\n"
            "flex-grow: 0;")
        self.label_5.setObjectName("label_5")
        self.label_6 = PyQt5.QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(PyQt5.QtCore.QRect(700, 450, 931, 181))
        self.label_6.setStyleSheet("width: 506px;\n"
                                   "height: 140px;\n"
                                   "\n"
                                   "font-family: \'Work Sans\';\n"
                                   "font-style: normal;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 22px;\n"
                                   "line-height: 160%;\n"
                                   "/* or 35px */\n"
                                   "\n"
                                   "font-variant: small-caps;\n"
                                   "\n"
                                   "/* White */\n"
                                   "\n"
                                   "color: #FFFFFF;\n"
                                   "\n"
                                   "flex: none;\n"
                                   "order: 1;\n"
                                   "align-self: stretch;\n"
                                   "flex-grow: 0;\n"
                                   "background-color: rgb();")
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        PyQt5.QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def open_file(self):
        from tkinter import filedialog
        _translate = PyQt5.QtCore.QCoreApplication.translate
        self.filename = filedialog.askopenfilename(filetypes=(
            ('jpg file', '*.jpg'),
            ('png file', '*.png')
        ))
        print(self.filename)
        if self.filename == None or self.filename == '':
            _translate = PyQt5.QtCore.QCoreApplication.translate
            self.label_4.setPixmap(PyQt5.QtGui.QPixmap("img_1.png"))
            self.label_2.setPixmap(PyQt5.QtGui.QPixmap("New Member 4.png"))
            self.label_5.setText(_translate("MainWindow",
                                            "<html><head/><body><p>Узнай вид </p><p>лебедя по </p><p>фотографии </p></body></html>"))
            self.label_6.setText(_translate("MainWindow",
                                            "<html><head/><body><p>Обученная нейросеть позволяет распознать </p><p>виды лебедей и отличать их друг от друга. </p><p>Для получения резутатов требуется </p><p>загрузить изображение.</p></body></html>"))
        elif self.filename != None and self.filename != '':
            self.label_2.setPixmap(PyQt5.QtGui.QPixmap(self.filename))
            self.label_2.setScaledContents(True)
            self.answer = processing.open_file(self.filename)
            self.label_4.setPixmap(PyQt5.QtGui.QPixmap(" "))
            self.label_6.setText(_translate("MainWindow", ''))
            self.label_5.setText(_translate("MainWindow", self.answer))


    def open_dir(self):
        _translate = PyQt5.QtCore.QCoreApplication.translate
        from tkinter import filedialog
        self.dirname = filedialog.askdirectory()
        self.label_2.setPixmap(PyQt5.QtGui.QPixmap("New Member 4.png"))
        self.label_6.setText(_translate("MainWindow", "Вы выбрали папку \n" + str(self.dirname)))
        self.label_5.setText(_translate("MainWindow", ' '))
        self.label_4.setPixmap(PyQt5.QtGui.QPixmap("3.png"))
        self.label_4.setScaledContents(True)
        processing.work_with_directory(self.dirname)
        self.label_5.setText(_translate("MainWindow", 'Ваши фото \nобработаны!'))



    def retranslateUi(self, MainWindow):
        _translate = PyQt5.QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Мин Природы Х ЦП ИИ"))
        self.pushButton.setText(_translate("MainWindow", "ЗАГРУЗИТЬ ИЗОБРАЖЕНИЕ"))
        self.label_5.setText(_translate("MainWindow",
                                        "<html><head/><body><p>Узнай вид </p><p>лебедя по </p><p>фотографии </p></body></html>"))
        self.label_6.setText(_translate("MainWindow",
                                        "<html><head/><body><p>Обученная нейросеть позволяет распознать </p><p>виды лебедей и отличать их друг от друга. </p><p>Для получения резутатов требуется </p><p>загрузить изображение.</p></body></html>"))




if __name__ == "__main__":

    app = PyQt5.QtWidgets.QApplication(sys.argv)
    MainWindow = PyQt5.QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
