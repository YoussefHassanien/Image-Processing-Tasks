import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import ImageView


class Ui_Output(object):

    def __init__(self, window):
        self.window = window
        self.appManager = None

    def abort(self):
        """Close the window and stop any ongoing processing"""
        # First close the window
        self.window.close()
        
        # Then check if appManager exists and call its abort method
        if hasattr(self, 'appManager') and self.appManager is not None:
            try:
                self.appManager.abort()
            except AttributeError:
                print("Warning: appManager does not have an abort method")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(964, 523)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "background-color: #1e1e2f;\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.OutputBox = QtWidgets.QGroupBox(self.centralwidget)
        self.OutputBox.setStyleSheet("QGroupBox {\n"
                                     "background-color: #1e1e2f;\n"
                                     "border: 1.2px solid #ffffff;\n"
                                     "border:none;\n"
                                     "border-style: outset;\n"
                                     "border-radius: 15px;\n"
                                     "}\n"
                                     "QGroupBox::title  {\n"
                                     "    subcontrol-origin: margin;\n"
                                     "    subcontrol-position: top left;\n"
                                     "    padding: -5px 0px 0px 0px;\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "}")
        self.OutputBox.setObjectName("OutputBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.OutputBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        # Keep only one output image group box
        self.groupBox_image1_5 = QtWidgets.QGroupBox(self.OutputBox)
        self.groupBox_image1_5.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_image1_5.sizePolicy().hasHeightForWidth())
        self.groupBox_image1_5.setSizePolicy(sizePolicy)
        # Allow the group box to expand to full width
        self.groupBox_image1_5.setMinimumSize(QtCore.QSize(400, 0))
        self.groupBox_image1_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_image1_5.setStyleSheet("QGroupBox {\n"
                                             "background-color: #1e1e2f;\n"
                                             "border: 1.2px solid #ffffff;\n"
                                             "border-style: outset;\n"
                                             "border-radius: 15px;\n"
                                             "}\n"
                                             "QGroupBox::title  {\n"
                                             "    subcontrol-origin: margin;\n"
                                             "    subcontrol-position: top left;\n"
                                             "    padding: -5px 0px 0px 0px;\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "}")
        self.groupBox_image1_5.setObjectName("groupBox_image1_5")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_image1_5)
        self.gridLayout.setContentsMargins(-1, 16, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.output_1 = ImageView(self.groupBox_image1_5)
        self.output_1.setObjectName("output_1")
        self.gridLayout.addWidget(self.output_1, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.groupBox_image1_5)
        
        # Remove the second image group box (groupBox_image1_7)
        
        self.gridLayout_3.addWidget(self.OutputBox, 0, 0, 1, 1)
        self.ProgressBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProgressBox.sizePolicy().hasHeightForWidth())
        self.ProgressBox.setSizePolicy(sizePolicy)
        self.ProgressBox.setStyleSheet("QGroupBox {\n"
                                       "background-color: #1e1e2f;\n"
                                       "border: 1.2px solid #ffffff;\n"
                                       "border-style: outset;\n"
                                       "border-radius: 15px;\n"
                                       "}\n"
                                       "QGroupBox::title  {\n"
                                       "    subcontrol-origin: margin;\n"
                                       "    subcontrol-position: top left;\n"
                                       "    padding: -5px 0px 0px 0px;\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "}")
        self.ProgressBox.setObjectName("ProgressBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.ProgressBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_14 = QtWidgets.QLabel(self.ProgressBox)
        self.label_14.setStyleSheet("background-color: transparent;")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout.addWidget(self.label_14)
        spacerItem = QtWidgets.QSpacerItem(248, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.progressBar = QtWidgets.QProgressBar(self.ProgressBox)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_4.addWidget(self.progressBar)
        self.cancel_button = QtWidgets.QPushButton(self.ProgressBox, clicked = lambda : self.abort())
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cancel_button.setFont(font)
        self.cancel_button.setStyleSheet("QPushButton#cancel_button {\n"
                                         "                background-color: #dc3545;\n"
                                         "                color: white;\n"
                                         "                border: none;\n"
                                         "                padding: 5px 10px;\n"
                                         "                border-radius: 5px;\n"
                                         "            }\n"
                                         "            \n"
                                         "            QPushButton#cancel_button:hover {\n"
                                         "                background-color: #c82333;\n"
                                         "            }\n"
                                         "            \n"
                                         "            QPushButton#cancel_button:pressed {\n"
                                         "                background-color: #bd2130;\n"
                                         "            }")
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_4.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.ProgressBox, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.output_1.ui.histogram.hide()
        self.output_1.ui.roiBtn.hide()
        self.output_1.ui.menuBtn.hide()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mixing Output"))
        self.groupBox_image1_5.setTitle(_translate("MainWindow", "Output 1"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Progress Bar:</span></p></body></html>"))
        self.cancel_button.setText(_translate("MainWindow", "Cancel"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Output()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
