import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import ImageView
from UI_Output import Ui_Output
from image_processor import ImageProcessor


class Ui_MainWindow(object):

    def __init__(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Output(self.window)
        self.ui.setupUi(self.window)

    def open_window(self):
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1151, 904)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "background-color: #1e1e2f;\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_9.setObjectName("gridLayout_9")

        # Add title label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setObjectName("label")
        self.gridLayout_9.addWidget(self.label, 0, 0, 1, 1)

        # Create Tab Widget
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        # Add styling to make tab text black
        self.tabWidget.setStyleSheet("""
            QTabBar::tab { 
                color: black; 
                background-color: #f0f0f0;
                padding: 5px;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
                width: 50px;                     
            }
            QTabBar::tab:selected { 
                background-color: #ffffff;
                font-weight: bold;
            }
            QTabWidget::pane { 
                border-top: 1px solid #ffffff;
                background-color: #1e1e2f;
            }
        """)

        # First Tab - DFT
        self.tab_dft = QtWidgets.QWidget()
        self.tab_dft.setObjectName("tab_dft")
        self.tab_dft_layout = QtWidgets.QVBoxLayout(self.tab_dft)
        self.tab_dft_layout.setObjectName("tab_dft_layout")

        # Add existing UI to the first tab
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.ImagesBox = QtWidgets.QGroupBox(self.tab_dft)  # Changed parent to tab_dft
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImagesBox.sizePolicy().hasHeightForWidth())
        self.ImagesBox.setSizePolicy(sizePolicy)
        self.ImagesBox.setStyleSheet("QGroupBox {\n"
                                     "background-color: #1e1e2f;\n"
                                     "border: 1.2px solid #ffffff;\n"
                                     "border: none;\n"
                                     "border-style: outset;\n"
                                     "border-radius: 15px;\n"
                                     "}\n"
                                     "QGroupBox::title  {\n"
                                     "    subcontrol-origin: margin;\n"
                                     "    subcontrol-position: top left;\n"
                                     "    padding: -5px 0px 0px 0px;\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "}")
        self.ImagesBox.setObjectName("ImagesBox")

        # Rest of existing UI elements
        # ... (keep all your existing UI elements but change parent to tab_dft where needed)

        # Setup Images box and grid layout
        self.gridLayout_7 = QtWidgets.QGridLayout(self.ImagesBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")

        # Image 1
        self.groupBox_image1_2 = QtWidgets.QGroupBox(self.ImagesBox)
        self.groupBox_image1_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_image1_2.sizePolicy().hasHeightForWidth())
        self.groupBox_image1_2.setSizePolicy(sizePolicy)
        self.groupBox_image1_2.setMinimumSize(QtCore.QSize(400, 0))
        self.groupBox_image1_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_image1_2.setStyleSheet("QGroupBox {\n"
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
        self.groupBox_image1_2.setObjectName("groupBox_image1_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_image1_2)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(199, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Image1_component_comboBox = QtWidgets.QComboBox(self.groupBox_image1_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Image1_component_comboBox.sizePolicy().hasHeightForWidth())
        self.Image1_component_comboBox.setSizePolicy(sizePolicy)
        self.Image1_component_comboBox.setMinimumSize(QtCore.QSize(176, 22))
        self.Image1_component_comboBox.setStyleSheet("QComboBox\n"
                                                     "{\n"
                                                     "    border-radius: 3px;\n"
                                                     "background-color: #1e1e2f;\n"
                                                     "}\n"
                                                     "\n"
                                                     "QComboBox::drop-down\n"
                                                     "{\n"
                                                     "    border-left-color: transparent;\n"
                                                     " }\n"
                                                     "\n"
                                                     "QComboBox::down-arrow, QSpinBox::down-arrow, QTimeEdit::down-arrow, QDateEdit::down-arrow\n"
                                                     "{\n"
                                                     "     image: url(:/icons/Arrowhead-nottop-256.png);\n"
                                                     "     width: 7px;\n"
                                                     "     height: 6px;\n"
                                                     "}\n"
                                                     "\n"
                                                     "QComboBox QAbstractItemView\n"
                                                     "{\n"
                                                     "    selection-background-color: transparent;\n"
                                                     "}")
        self.Image1_component_comboBox.setMaxCount(2147483646)
        self.Image1_component_comboBox.setObjectName("Image1_component_comboBox")
        self.Image1_component_comboBox.addItem("")
        self.Image1_component_comboBox.addItem("")
        self.horizontalLayout.addWidget(self.Image1_component_comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Image_1 = ImageView(self.groupBox_image1_2)
        self.Image_1.setObjectName("Image_1")
        self.horizontalLayout_4.addWidget(self.Image_1)
        self.Image1_component = ImageView(self.groupBox_image1_2)
        self.Image1_component.setObjectName("Image1_component")
        self.horizontalLayout_4.addWidget(self.Image1_component)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_14 = QtWidgets.QLabel(self.groupBox_image1_2)
        self.label_14.setStyleSheet("background-color: transparent;")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_3.addWidget(self.label_14)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.image1_component1_slider = QtWidgets.QSlider(self.groupBox_image1_2)
        self.image1_component1_slider.setMinimumSize(QtCore.QSize(160, 0))
        self.image1_component1_slider.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.image1_component1_slider.setStyleSheet("QSlider{\n"
                                                    "    background-color: transparent;\n"
                                                    "}\n"
                                                    "\n"
                                                    "QSlider::handle {\n"
                                                    "    background-color: qradialgradient(\n"
                                                    "        cx: 0.7, cy: 1.4, fx: 0.7, fy: 1.4,\n"
                                                    "        radius: 1, stop: 0 #fff, stop: 1 #424242\n"
                                                    "        );\n"
                                                    "    border-radius: 2px;\n"
                                                    "    height: 40px;\n"
                                                    "    width: 40px;\n"
                                                    "    margin: -15px 0px;\n"
                                                    "    }\n"
                                                    "\n"
                                                    "QSlider::handle::hover{\n"
                                                    "    border: inset;\n"
                                                    "     background-color: qradialgradient(\n"
                                                    "        cx: 0.7, cy: 1.4, fx: 0.7, fy: 1.4,\n"
                                                    "        radius: 1, stop: 0 #bbb, stop: 1 #000\n"
                                                    "        );\n"
                                                    "}")
        self.image1_component1_slider.setMaximum(100)
        self.image1_component1_slider.setProperty("value", 0)
        self.image1_component1_slider.setOrientation(QtCore.Qt.Horizontal)
        self.image1_component1_slider.setObjectName("image1_component1_slider")
        self.horizontalLayout_6.addWidget(self.image1_component1_slider)
        self.image1_component1_LCD = QtWidgets.QLCDNumber(self.groupBox_image1_2)
        self.image1_component1_LCD.setObjectName("image1_component1_LCD")
        self.horizontalLayout_6.addWidget(self.image1_component1_LCD)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_35.addWidget(self.groupBox_image1_2)

        # Image 2
        self.groupBox_image1_3 = QtWidgets.QGroupBox(self.ImagesBox)
        self.groupBox_image1_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_image1_3.sizePolicy().hasHeightForWidth())
        self.groupBox_image1_3.setSizePolicy(sizePolicy)
        self.groupBox_image1_3.setMinimumSize(QtCore.QSize(400, 0))
        self.groupBox_image1_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_image1_3.setStyleSheet("QGroupBox {\n"
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
        self.groupBox_image1_3.setObjectName("groupBox_image1_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_image1_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem1 = QtWidgets.QSpacerItem(199, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        self.Image2_component_comboBox = QtWidgets.QComboBox(self.groupBox_image1_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Image2_component_comboBox.sizePolicy().hasHeightForWidth())
        self.Image2_component_comboBox.setSizePolicy(sizePolicy)
        self.Image2_component_comboBox.setMinimumSize(QtCore.QSize(176, 22))
        self.Image2_component_comboBox.setStyleSheet("QComboBox\n"
                                                     "{\n"
                                                     "    border-radius: 3px;\n"
                                                     "background-color: #1e1e2f;\n"
                                                     "}\n"
                                                     "\n"
                                                     "QComboBox::drop-down\n"
                                                     "{\n"
                                                     "    border-left-color: transparent;\n"
                                                     " }\n"
                                                     "\n"
                                                     "QComboBox::down-arrow, QSpinBox::down-arrow, QTimeEdit::down-arrow, QDateEdit::down-arrow\n"
                                                     "{\n"
                                                     "     image: url(:/icons/Arrowhead-nottop-256.png);\n"
                                                     "     width: 7px;\n"
                                                     "     height: 6px;\n"
                                                     "}\n"
                                                     "\n"
                                                     "QComboBox QAbstractItemView\n"
                                                     "{\n"
                                                     "    selection-background-color: transparent;\n"
                                                     "}")
        self.Image2_component_comboBox.setMaxCount(2147483646)
        self.Image2_component_comboBox.setObjectName("Image2_component_comboBox")
        self.Image2_component_comboBox.addItem("")
        self.Image2_component_comboBox.addItem("")
        self.horizontalLayout_12.addWidget(self.Image2_component_comboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.Image_2 = ImageView(self.groupBox_image1_3)
        self.Image_2.setObjectName("Image_2")
        self.horizontalLayout_14.addWidget(self.Image_2)
        self.Image2_component = ImageView(self.groupBox_image1_3)
        self.Image2_component.setObjectName("Image2_component")
        self.horizontalLayout_14.addWidget(self.Image2_component)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_17 = QtWidgets.QLabel(self.groupBox_image1_3)
        self.label_17.setStyleSheet("background-color: transparent;")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_15.addWidget(self.label_17)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.image2_component1_slider = QtWidgets.QSlider(self.groupBox_image1_3)
        self.image2_component1_slider.setMinimumSize(QtCore.QSize(160, 0))
        self.image2_component1_slider.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.image2_component1_slider.setStyleSheet("QSlider{\n"
                                                    "    background-color: transparent;\n"
                                                    "}\n"
                                                    "\n"
                                                    "QSlider::handle {\n"
                                                    "    background-color: qradialgradient(\n"
                                                    "        cx: 0.7, cy: 1.4, fx: 0.7, fy: 1.4,\n"
                                                    "        radius: 1, stop: 0 #fff, stop: 1 #424242\n"
                                                    "        );\n"
                                                    "    border-radius: 2px;\n"
                                                    "    height: 40px;\n"
                                                    "    width: 40px;\n"
                                                    "    margin: -15px 0px;\n"
                                                    "    }\n"
                                                    "\n"
                                                    "QSlider::handle::hover{\n"
                                                    "    border: inset;\n"
                                                    "     background-color: qradialgradient(\n"
                                                    "        cx: 0.7, cy: 1.4, fx: 0.7, fy: 1.4,\n"
                                                    "        radius: 1, stop: 0 #bbb, stop: 1 #000\n"
                                                    "        );\n"
                                                    "}")
        self.image2_component1_slider.setMaximum(100)
        self.image2_component1_slider.setProperty("value", 0)
        self.image2_component1_slider.setOrientation(QtCore.Qt.Horizontal)
        self.image2_component1_slider.setObjectName("image2_component1_slider")
        self.horizontalLayout_19.addWidget(self.image2_component1_slider)
        self.image2_component1_LCD = QtWidgets.QLCDNumber(self.groupBox_image1_3)
        self.image2_component1_LCD.setObjectName("image2_component1_LCD")
        self.horizontalLayout_19.addWidget(self.image2_component1_LCD)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_19)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.horizontalLayout_20.addLayout(self.horizontalLayout_21)
        self.verticalLayout_3.addLayout(self.horizontalLayout_20)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_35.addWidget(self.groupBox_image1_3)
        self.verticalLayout.addLayout(self.horizontalLayout_35)
        self.gridLayout_7.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_10.addWidget(self.ImagesBox)

        # Apply button layout
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem6)

        self.apply_button = QtWidgets.QPushButton(self.tab_dft)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apply_button.sizePolicy().hasHeightForWidth())
        self.apply_button.setSizePolicy(sizePolicy)
        self.apply_button.setMaximumSize(QtCore.QSize(234, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.apply_button.setFont(font)
        self.apply_button.setStyleSheet(" QPushButton#apply_button {\n"
                                        "                background-color: #28a745;\n"
                                        "                color: white;\n"
                                        "                border: none;\n"
                                        "                padding: 5px 10px;\n"
                                        "                border-radius: 5px;\n"
                                        "            }\n"
                                        "            \n"
                                        "            QPushButton#apply_button:hover {\n"
                                        "                background-color: #218838;\n"
                                        "            }\n"
                                        "            \n"
                                        "            QPushButton#apply_button:pressed {\n"
                                        "                background-color: #1e7e34;\n"
                                        "            }")
        self.apply_button.setObjectName("apply_button")
        self.horizontalLayout_11.addWidget(self.apply_button)

        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.verticalLayout_10.addLayout(self.verticalLayout_8)

        # Add verticalLayout_10 to tab_dft
        self.tab_dft_layout.addLayout(self.verticalLayout_10)

        # Second Tab - Harris with 3 horizontal images
        self.tab_harris = QtWidgets.QWidget()
        self.tab_harris.setObjectName("tab_harris")
        self.tab_harris_layout = QtWidgets.QVBoxLayout(self.tab_harris)
        self.tab_harris_layout.setObjectName("tab_harris_layout")

        # Create horizontal layout for the three images
        self.harris_horizontal_layout = QtWidgets.QHBoxLayout()
        self.harris_horizontal_layout.setObjectName("harris_horizontal_layout")

        # Original Image
        self.harris_original_groupbox = QtWidgets.QGroupBox(self.tab_harris)
        self.harris_original_groupbox.setObjectName("harris_original_groupbox")
        self.harris_original_groupbox.setStyleSheet("QGroupBox {\n"
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
        self.harris_original_layout = QtWidgets.QVBoxLayout(self.harris_original_groupbox)
        self.harris_original_layout.setObjectName("harris_original_layout")
        self.harris_original_image = ImageView(self.harris_original_groupbox)
        self.harris_original_image.setObjectName("harris_original_image")
        self.harris_original_layout.addWidget(self.harris_original_image)
        self.harris_horizontal_layout.addWidget(self.harris_original_groupbox)

        # Built-in Harris
        self.harris_builtin_groupbox = QtWidgets.QGroupBox(self.tab_harris)
        self.harris_builtin_groupbox.setObjectName("harris_builtin_groupbox")
        self.harris_builtin_groupbox.setStyleSheet("QGroupBox {\n"
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
        self.harris_builtin_layout = QtWidgets.QVBoxLayout(self.harris_builtin_groupbox)
        self.harris_builtin_layout.setObjectName("harris_builtin_layout")
        self.harris_builtin_image = ImageView(self.harris_builtin_groupbox)
        self.harris_builtin_image.setObjectName("harris_builtin_image")
        self.harris_builtin_layout.addWidget(self.harris_builtin_image)
        self.harris_horizontal_layout.addWidget(self.harris_builtin_groupbox)

        # Manual Harris
        self.harris_manual_groupbox = QtWidgets.QGroupBox(self.tab_harris)
        self.harris_manual_groupbox.setObjectName("harris_manual_groupbox")
        self.harris_manual_groupbox.setStyleSheet("QGroupBox {\n"
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
        self.harris_manual_layout = QtWidgets.QVBoxLayout(self.harris_manual_groupbox)
        self.harris_manual_layout.setObjectName("harris_manual_layout")
        self.harris_manual_image = ImageView(self.harris_manual_groupbox)
        self.harris_manual_image.setObjectName("harris_manual_image")
        self.harris_manual_layout.addWidget(self.harris_manual_image)
        self.harris_horizontal_layout.addWidget(self.harris_manual_groupbox)

        # Add horizontal layout to tab
        self.tab_harris_layout.addLayout(self.harris_horizontal_layout)

        # Add k-value slider layout
        self.harris_slider_layout = QtWidgets.QHBoxLayout()
        self.harris_slider_layout.setObjectName("harris_slider_layout")

        # K-value label
        self.k_label = QtWidgets.QLabel(self.tab_harris)
        self.k_label.setStyleSheet("background-color: transparent;")
        self.k_label.setObjectName("k_label")
        self.harris_slider_layout.addWidget(self.k_label)

        # K-value slider
        self.k_slider = QtWidgets.QSlider(self.tab_harris)
        self.k_slider.setMinimumSize(QtCore.QSize(250, 0))
        self.k_slider.setStyleSheet("QSlider{\n"
                                    "    background-color: transparent;\n"
                                    "}\n"
                                    "\n"
                                    "QSlider::handle {\n"
                                    "    background-color: qradialgradient(\n"
                                    "        cx: 0.7, cy: 1.4, fx: 0.7, fy: 1.4,\n"
                                    "        radius: 1, stop: 0 #fff, stop: 1 #424242\n"
                                    "        );\n"
                                    "    border-radius: 2px;\n"
                                    "    height: 40px;\n"
                                    "    width: 40px;\n"
                                    "    margin: -15px 0px;\n"
                                    "    }\n"
                                    "\n"
                                    "QSlider::handle::hover{\n"
                                    "    border: inset;\n"
                                    "     background-color: qradialgradient(\n"
                                    "        cx: 0.7, cy: 1.4, fx: 0.7, fy: 1.4,\n"
                                    "        radius: 1, stop: 0 #bbb, stop: 1 #000\n"
                                    "        );\n"
                                    "}")
        self.k_slider.setMinimum(40)  # Represents 0.04
        self.k_slider.setMaximum(60)  # Represents 0.06
        self.k_slider.setValue(40)    # Default to 0.04
        self.k_slider.setOrientation(QtCore.Qt.Horizontal)
        self.k_slider.setObjectName("k_slider")
        self.harris_slider_layout.addWidget(self.k_slider)

        # K-value LCD display
        self.k_value_LCD = QtWidgets.QLCDNumber(self.tab_harris)
        self.k_value_LCD.setObjectName("k_value_LCD")
        self.k_value_LCD.setDigitCount(4)  # To show values like "0.04"
        self.k_value_LCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.k_value_LCD.setStyleSheet("background-color: #2c2c2c;")
        self.harris_slider_layout.addWidget(self.k_value_LCD)

        # Add slider layout to the tab layout
        self.tab_harris_layout.addLayout(self.harris_slider_layout)

        # Connect slider value change to LCD
        self.k_slider.valueChanged.connect(lambda val: self.k_value_LCD.display(val / 1000))

        # Add load and detect buttons
        self.harris_buttons_layout = QtWidgets.QHBoxLayout()
        self.harris_buttons_layout.setObjectName("harris_buttons_layout")

        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.harris_buttons_layout.addItem(spacerItem8)

        self.harris_load_button = QtWidgets.QPushButton(self.tab_harris)
        self.harris_load_button.setObjectName("harris_load_button")
        self.harris_load_button.setStyleSheet(" QPushButton {\n"
                                              "                background-color: #007bff;\n"
                                              "                color: white;\n"
                                              "                border: none;\n"
                                              "                padding: 5px 10px;\n"
                                              "                border-radius: 5px;\n"
                                              "            }\n"
                                              "            \n"
                                              "            QPushButton:hover {\n"
                                              "                background-color: #0069d9;\n"
                                              "            }\n"
                                              "            \n"
                                              "            QPushButton:pressed {\n"
                                              "                background-color: #0062cc;\n"
                                              "            }")
        self.harris_buttons_layout.addWidget(self.harris_load_button)

        self.harris_detect_button = QtWidgets.QPushButton(self.tab_harris)
        self.harris_detect_button.setObjectName("harris_detect_button")
        self.harris_detect_button.setStyleSheet(" QPushButton {\n"
                                                "                background-color: #28a745;\n"
                                                "                color: white;\n"
                                                "                border: none;\n"
                                                "                padding: 5px 10px;\n"
                                                "                border-radius: 5px;\n"
                                                "            }\n"
                                                "            \n"
                                                "            QPushButton:hover {\n"
                                                "                background-color: #218838;\n"
                                                "            }\n"
                                                "            \n"
                                                "            QPushButton:pressed {\n"
                                                "                background-color: #1e7e34;\n"
                                                "            }")
        self.harris_buttons_layout.addWidget(self.harris_detect_button)

        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.harris_buttons_layout.addItem(spacerItem9)

        self.tab_harris_layout.addLayout(self.harris_buttons_layout)

        # Add tabs to tab widget
        self.tabWidget.addTab(self.tab_dft, "")
        self.tabWidget.addTab(self.tab_harris, "")

        # Add tabWidget to main layout
        self.gridLayout_9.addWidget(self.tabWidget, 1, 0, 1, 1)

        # Setup status bar
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label.setBuddy(self.ImagesBox)

        # Set up connections
        self.retranslateUi(MainWindow)
        self.Image1_component_comboBox.setCurrentIndex(0)
        self.Image2_component_comboBox.setCurrentIndex(0)
        self.image1_component1_slider.valueChanged['int'].connect(self.image1_component1_LCD.display)  # type: ignore
        self.image2_component1_slider.valueChanged['int'].connect(self.image2_component1_LCD.display)  # type: ignore

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ImageViews = [self.Image_1, self.Image1_component, self.Image_2, self.Image2_component]

        for image in ImageViews:
            image.ui.histogram.hide()
            image.ui.roiBtn.hide()
            image.ui.menuBtn.hide()
            image.view.setMouseEnabled(x=False, y=False)

        # Hide unwanted UI elements in Harris images
        harris_image_views = [self.harris_original_image, self.harris_builtin_image, self.harris_manual_image]
        for image in harris_image_views:
            image.ui.histogram.hide()
            image.ui.roiBtn.hide()
            image.ui.menuBtn.hide()
            image.view.setMouseEnabled(x=False, y=False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Mixer"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Image Mixer</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dft), _translate("MainWindow", "DFT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_harris), _translate("MainWindow", "Harris"))
        self.groupBox_image1_2.setTitle(_translate("MainWindow", "Image 1"))
        self.Image1_component_comboBox.setCurrentText(_translate("MainWindow", "FT Magnitude"))
        self.Image1_component_comboBox.setItemText(0, _translate("MainWindow", "FT Magnitude"))
        self.Image1_component_comboBox.setItemText(1, _translate("MainWindow", "FT Phase"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Component :</span></p></body></html>"))
        self.groupBox_image1_3.setTitle(_translate("MainWindow", "Image 2"))
        self.Image2_component_comboBox.setCurrentText(_translate("MainWindow", "FT Magnitude"))
        self.Image2_component_comboBox.setItemText(0, _translate("MainWindow", "FT Magnitude"))
        self.Image2_component_comboBox.setItemText(1, _translate("MainWindow", "FT Phase"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Component :</span></p></body></html>"))
        self.apply_button.setText(_translate("MainWindow", "Apply"))
        self.harris_original_groupbox.setTitle(_translate("MainWindow", "Original Image"))
        self.harris_builtin_groupbox.setTitle(_translate("MainWindow", "Built-in Harris"))
        self.harris_manual_groupbox.setTitle(_translate("MainWindow", "Manual Harris"))
        self.harris_load_button.setText(_translate("MainWindow", "Load Image"))
        self.harris_detect_button.setText(_translate("MainWindow", "Detect Features"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dft), _translate("MainWindow", "DFT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_harris), _translate("MainWindow", "Harris"))
        self.k_label.setText(_translate("MainWindow", "K-value:"))
        self.k_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">k-value:</span></p></body></html>"))


class MainApplication(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialize image processor with UI reference
        self.processor = ImageProcessor(self.ui)

        # Connect additional UI signals that aren't handled in the processor
        self.setup_additional_connections()

    def setup_additional_connections(self):
        """Set up connections for all UI elements to their handler methods"""
        # Create and add load buttons for images in DFT tab
        self.load_btn1 = QtWidgets.QPushButton("Load Image 1")
        self.load_btn2 = QtWidgets.QPushButton("Load Image 2")

        # Style buttons
        button_style = """
            QPushButton {
                background-color: #007bff;
                color: white;
                border: none;
                padding: 5px 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #0069d9;
            }
            QPushButton:pressed {
                background-color: #0062cc;
            }
        """
        self.load_btn1.setStyleSheet(button_style)
        self.load_btn2.setStyleSheet(button_style)

        # Add buttons to UI
        self.ui.verticalLayout_2.insertWidget(0, self.load_btn1)
        self.ui.verticalLayout_3.insertWidget(0, self.load_btn2)
        
        # Connect DFT tab buttons
        self.load_btn1.clicked.connect(lambda: self.processor.load_image(0))
        self.load_btn2.clicked.connect(lambda: self.processor.load_image(1))
        self.ui.apply_button.clicked.connect(self.processor.mix_components)
        
        # Connect Harris tab buttons
        self.ui.harris_load_button.clicked.connect(self.processor.load_harris_image)
        self.ui.harris_detect_button.clicked.connect(self.processor.detect_harris_corners)
        
        # Connect k-value slider to processor's update method
        self.ui.k_slider.valueChanged.connect(self.processor.update_k_value)
        
        # Connect component comboboxes to update display
        self.ui.Image1_component_comboBox.currentIndexChanged.connect(
            lambda: self.update_component_view(0)
        )
        self.ui.Image2_component_comboBox.currentIndexChanged.connect(
            lambda: self.update_component_view(1)
        )

    def update_component_view(self, index):
        """Update component view when selection changes"""
        # Skip if image not loaded
        if self.processor.original_images[index] is None:
            return

        # Update the component display
        comp_type = self.ui.Image1_component_comboBox.currentIndex() if index == 0 else self.ui.Image2_component_comboBox.currentIndex()
        img = self.processor.original_images[index]
        self.processor.compute_dft_components(img, index)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApplication()
    window.show()
    sys.exit(app.exec_())
