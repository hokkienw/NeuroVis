# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import torch
from torchvision import transforms
import qimage2ndarray
# from PIL import Image
# from PIL.ImageQt import ImageQt
import numpy as np
from model import Model
import ssl
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsSceneMouseEvent
from PyQt5.QtGui import QPen, QBrush, QImage, QPixmap, QFont, QPainter
from PyQt5.QtWidgets import QGraphicsPixmapItem, QFileDialog
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context




class PaintScene(QGraphicsScene):
    def __init__(self, parent=None):
        super(PaintScene, self).__init__(parent)
        self.previous_point = None

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent):
        self.addEllipse(
            event.scenePos().x() - 5, event.scenePos().y() - 5, 20, 20,
            QPen(Qt.NoPen), QBrush(Qt.white)
        )
        self.previous_point = event.scenePos()

    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent):
        if self.previous_point:
            self.addLine(
                self.previous_point.x(), self.previous_point.y(),
                event.scenePos().x(), event.scenePos().y(),
                QPen(Qt.white, 20, Qt.SolidLine, Qt.RoundCap)
            )
        self.previous_point = event.scenePos()



class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1218, 583)
        Widget.setStyleSheet("background-color: rgb(29, 38, 51)")
        self.widget = QtWidgets.QWidget(Widget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 391, 561))
        self.widget.setStyleSheet("QWidget{\n"
"background-color:rgb(236, 237, 245);\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton{\n"
"background-color:rgb(120, 236, 154);\n"
"color:black;\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(138, 74, 227);\n"
"color:white;\n"
"border-radius: 20px;\n"
"}\n"
"QComboBox{\n"
"background-color:rgb(108, 216, 155);\n"
"color:black;\n"
"border-radius: 10px;\n"
"}\n"
"QLabel{\n"
"background-color:rgb(27, 120, 218);\n"
"color:white;\n"
"border-radius: 10px;\n"
"}\n"
"QSpinBox{\n"
"background-color:rgb(138, 74, 227);\n"
"color:white;\n"
"border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox{\n"
"background-color:rgb(138, 74, 227);\n"
"color:white;\n"
"border-radius: 10px;\n"
"}")
        self.widget.setObjectName("widget")
        self.datasetBox = QtWidgets.QComboBox(self.widget)
        self.datasetBox.setGeometry(QtCore.QRect(10, 30, 371, 32))
        self.datasetBox.setStyleSheet("")
        self.datasetBox.setObjectName("datasetBox")
        self.datasetBox.addItem("")
        self.datasetBox.addItem("")
        self.netBox = QtWidgets.QComboBox(self.widget)
        self.netBox.setGeometry(QtCore.QRect(10, 100, 371, 32))
        self.netBox.setObjectName("netBox")
        self.netBox.addItem("")
        self.netBox.addItem("")
        self.poolingBox = QtWidgets.QComboBox(self.widget)
        self.poolingBox.setGeometry(QtCore.QRect(290, 170, 91, 41))
        self.poolingBox.setObjectName("poolingBox")
        self.poolingBox.addItem("")
        self.poolingBox.addItem("")
        self.epochSpin = QtWidgets.QSpinBox(self.widget)
        self.epochSpin.setGeometry(QtCore.QRect(200, 400, 181, 21))
        self.epochSpin.setMinimum(1)
        self.epochSpin.setMaximum(100000)
        self.epochSpin.setObjectName("epochSpin")
        self.batchSpin = QtWidgets.QSpinBox(self.widget)
        self.batchSpin.setGeometry(QtCore.QRect(200, 430, 181, 22))
        self.batchSpin.setMinimum(1)
        self.batchSpin.setMaximum(200)
        self.batchSpin.setObjectName("batchSpin")
        self.lerningRateSpin = QtWidgets.QDoubleSpinBox(self.widget)
        self.lerningRateSpin.setGeometry(QtCore.QRect(200, 460, 181, 22))
        self.lerningRateSpin.setDecimals(4)
        self.lerningRateSpin.setMaximum(10.0)
        self.lerningRateSpin.setMinimum(0.0001)
        self.lerningRateSpin.setObjectName("lerningRateSpin")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(17, 400, 171, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(17, 430, 171, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(17, 460, 171, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(10, 5, 371, 21))
        self.label_4.setObjectName("label_4")
        self.activationBox = QtWidgets.QComboBox(self.widget)
        self.activationBox.setGeometry(QtCore.QRect(110, 170, 91, 41))
        self.activationBox.setObjectName("activationBox")
        self.activationBox.addItem("")
        self.activationBox.addItem("")
        self.activationBox.addItem("")
        self.convBox = QtWidgets.QComboBox(self.widget)
        self.convBox.setGeometry(QtCore.QRect(290, 220, 91, 41))
        self.convBox.setObjectName("convBox")
        self.convBox.addItem("")
        self.convBox.addItem("")
        self.batchBox = QtWidgets.QComboBox(self.widget)
        self.batchBox.setGeometry(QtCore.QRect(120, 220, 81, 41))
        self.batchBox.setObjectName("batchBox")
        self.batchBox.addItem("")
        self.batchBox.addItem("")
        self.optimazerBox = QtWidgets.QComboBox(self.widget)
        self.optimazerBox.setGeometry(QtCore.QRect(210, 350, 171, 41))
        self.optimazerBox.setObjectName("optimazerBox")
        self.optimazerBox.addItem("")
        self.optimazerBox.addItem("")
        self.gpuBox = QtWidgets.QComboBox(self.widget)
        self.gpuBox.setGeometry(QtCore.QRect(300, 300, 81, 41))
        self.gpuBox.setObjectName("gpuBox")
        self.gpuBox.addItem("")
        self.gpuBox.addItem("")
        self.lossBox = QtWidgets.QComboBox(self.widget)
        self.lossBox.setGeometry(QtCore.QRect(90, 300, 111, 41))
        self.lossBox.setObjectName("lossBox")
        self.lossBox.addItem("")
        self.lossBox.addItem("")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 371, 21))
        self.label_5.setObjectName("label_5")
        self.learnButton = QtWidgets.QPushButton(self.widget)
        self.learnButton.setGeometry(QtCore.QRect(39, 491, 321, 61))
        self.learnButton.setObjectName("learnButton")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(10, 140, 371, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(10, 270, 371, 21))
        self.label_7.setObjectName("label_7")
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setGeometry(QtCore.QRect(10, 170, 91, 41))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setGeometry(QtCore.QRect(10, 220, 101, 41))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setGeometry(QtCore.QRect(210, 170, 71, 41))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setGeometry(QtCore.QRect(210, 220, 71, 41))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setGeometry(QtCore.QRect(220, 300, 71, 41))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.widget)
        self.label_18.setGeometry(QtCore.QRect(10, 300, 71, 41))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.widget)
        self.label_19.setGeometry(QtCore.QRect(10, 350, 191, 41))
        self.label_19.setObjectName("label_19")
        self.widget_3 = QtWidgets.QWidget(Widget)
        self.widget_3.setGeometry(QtCore.QRect(410, 10, 391, 561))
        self.widget_3.setStyleSheet("QWidget{\n"
"background-color:rgb(236, 237, 245);\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton{\n"
"background-color:rgb(120, 236, 154);\n"
"color:black;\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(138, 74, 227);\n"
"color:white;\n"
"border-radius: 20px;\n"
"}\n"
"QComboBox{\n"
"background-color:rgb(108, 216, 155);\n"
"color:black;\n"
"border-radius: 10px;\n"
"}\n"
"QLabel{\n"
"background-color:rgb(27, 120, 218);\n"
"color:white;\n"
"border-radius: 10px;\n"
"}\n"
"QSpinBox{\n"
"background-color:rgb(138, 74, 227);\n"
"color:white;\n"
"border-radius: 10px;\n"
"}\n"
"QDoubleSpinBox{\n"
"background-color:rgb(138, 74, 227);\n"
"color:white;\n"
"border-radius: 10px;\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.accuracyWidget = QtWidgets.QWidget(self.widget_3)
        self.accuracyWidget.setGeometry(QtCore.QRect(20, 40, 351, 501))
        self.accuracyWidget.setStyleSheet("background-color:white;\n"
"border-radius: 20px;")
        self.accuracyWidget.setObjectName("accuracyWidget")
#         self.lossWidget = QtWidgets.QWidget(self.widget_3)
#         self.lossWidget.setGeometry(QtCore.QRect(20, 330, 351, 221))
#         self.lossWidget.setStyleSheet("background-color:white;\n"
# "border-radius: 20px;")
#         self.lossWidget.setObjectName("lossWidget")
        self.label_8 = QtWidgets.QLabel(self.widget_3)
        self.label_8.setGeometry(QtCore.QRect(20, 10, 351, 21))
        self.label_8.setObjectName("label_8")
        # self.label_9 = QtWidgets.QLabel(self.widget_3)
        # self.label_9.setGeometry(QtCore.QRect(20, 300, 351, 21))
        # self.label_9.setObjectName("label_9")
        self.widget_2 = QtWidgets.QWidget(Widget)
        self.widget_2.setGeometry(QtCore.QRect(810, 10, 401, 561))
        self.widget_2.setStyleSheet("QWidget{\n"
"background-color:rgb(78, 63, 210);\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton{\n"
"background-color:rgb(120, 236, 154);\n"
"color:black;\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(138, 74, 227);\n"
"color:white;\n"
"border-radius: 20px;\n"
"}\n"
"QComboBox{\n"
"background-color:white;\n"
"color:black;\n"
"border-radius: 10px;\n"
"}\n"
"QLabel{\n"
"background-color:white;\n"
"color:black;\n"
"border-radius: 10px;\n"
"}\n"
"QSpinBox{\n"
"background-color:white;\n"
"}\n"
"QDoubleSpinBox{\n"
"background-color:white;\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.paint = QtWidgets.QGraphicsView(self.widget_2)
        self.paint.setGeometry(QtCore.QRect(20, 50, 200, 200))
        self.paint.setMinimumSize(QtCore.QSize(200, 200))
        self.paint.setMaximumSize(QtCore.QSize(250, 250))
        self.paint.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.paint.setStyleSheet("background-color: black;\n"
"border-radius: 20px;")
        self.paint.setObjectName("paint")
        self.paint_scene = PaintScene()
        self.paint.setScene(self.paint_scene)
        # self.paint.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # self.paint.setFixedSize(200, 200)
        self.resaultLabel = QtWidgets.QLabel(self.widget_2)
        self.resaultLabel.setGeometry(QtCore.QRect(20, 310, 361, 241))
        self.resaultLabel.setText("")
        self.resaultLabel.setObjectName("resaultLabel")
        font = QFont()
        font.setPointSize(18)
        self.resaultLabel.setFont(font)
        self.label_11 = QtWidgets.QLabel(self.widget_2)
        self.label_11.setGeometry(QtCore.QRect(20, 270, 361, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.widget_2)
        self.label_12.setGeometry(QtCore.QRect(20, 20, 361, 21))
        self.label_12.setObjectName("label_12")
        self.clearButton = QtWidgets.QPushButton(self.widget_2)
        self.clearButton.setGeometry(QtCore.QRect(230, 110, 151, 41))
        self.clearButton.setObjectName("clearButton")
        self.LoadButton = QtWidgets.QPushButton(self.widget_2)
        self.LoadButton.setGeometry(QtCore.QRect(230, 60, 151, 41))
        self.LoadButton.setObjectName("LoadButton")
        self.goButton = QtWidgets.QPushButton(self.widget_2)
        self.goButton.setGeometry(QtCore.QRect(230, 160, 151, 81))
        self.goButton.setObjectName("goButton")
        # self.goButton.setEnabled(False)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)
        Widget.setTabOrder(self.lerningRateSpin, self.batchSpin)
        Widget.setTabOrder(self.batchSpin, self.paint)
        Widget.setTabOrder(self.paint, self.epochSpin)
        Widget.setTabOrder(self.epochSpin, self.poolingBox)
        Widget.setTabOrder(self.poolingBox, self.netBox)
        Widget.setTabOrder(self.netBox, self.datasetBox)

        self.accuracy_canvas = FigureCanvas(Figure())
        self.accuracy_canvas.setGeometry(QtCore.QRect(0, 0, 350, 500))
        self.accuracy_canvas.setParent(self.accuracyWidget)

        # Add a FigureCanvas for the loss plot
        # self.loss_canvas = FigureCanvas(Figure())
        # self.loss_canvas.setGeometry(QtCore.QRect(20, 330, 341, 211))
        # self.loss_canvas.setParent(self.lossWidget)

        self.learnButton.clicked.connect(self.on_learn_click)
        self.clearButton.clicked.connect(self.on_clear_click)
        self.goButton.clicked.connect(self.on_go_click)
        self.LoadButton.clicked.connect(self.on_load_button_click)

    def on_learn_click(self):
        if  self.convBox.currentText() == "5x5":
                self.conv_s = 5
        else:
                self.conv_s = 3

        self.model = Model(self.activationBox.currentText(), self.poolingBox.currentText(), self.conv_s, self.batchBox.currentIndex(), self.netBox.currentText(), self.epochSpin.value(), self.datasetBox.currentText(), self.lossBox.currentText(), self.gpuBox.currentText(), self.batchSpin.value(), self.optimazerBox.currentText(), self.lerningRateSpin.value())
        accuracies, losses = self.model.Train()
        
        self.accuracy_canvas.figure.clear()

        ax_accuracy = self.accuracy_canvas.figure.add_subplot(211)
        ax_accuracy.plot(accuracies)
        ax_accuracy.set_title('Accuracy Over Epochs')
        ax_accuracy.set_xlabel('Epochs')
        ax_accuracy.set_ylabel('Accuracy')

        ax_loss = self.accuracy_canvas.figure.add_subplot(212)
        ax_loss.plot(losses)
        ax_loss.set_title('Loss Over Epochs')
        ax_loss.set_xlabel('Epochs')
        ax_loss.set_ylabel('Loss')

        self.accuracy_canvas.draw()
        # self.loss_canvas.figure.clear()

        # ax_accuracy = self.accuracy_canvas.figure.add_subplot(111)
        # ax_accuracy.plot(accuracies)
        # ax_accuracy.set_xlabel('Epochs')
        # ax_accuracy.set_ylabel('Accuracy')

        # ax_loss = self.loss_canvas.figure.add_subplot(112)
        # ax_loss.plot(losses)
        # ax_loss.set_xlabel('Epochs')
        # ax_loss.set_ylabel('Loss')

        # self.loss_canvas.draw()
        # self.accuracy_canvas.draw()
        self.goButton.setEnabled(True)


    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.datasetBox.setItemText(0, _translate("Widget", "CIFAR10"))
        self.datasetBox.setItemText(1, _translate("Widget", "MNIST"))
        self.netBox.setItemText(0, _translate("Widget", "LeNet5"))
        self.netBox.setItemText(1, _translate("Widget", "LeNet6"))
        self.poolingBox.setItemText(0, _translate("Widget", "Max"))
        self.poolingBox.setItemText(1, _translate("Widget", "Average"))
        self.label.setText(_translate("Widget", "   кол-во эпох"))
        self.label_2.setText(_translate("Widget", "  размер батча"))
        self.label_3.setText(_translate("Widget", "  learning rate"))
        self.label_4.setText(_translate("Widget", "    Выберете датасет для обучениия"))
        self.activationBox.setItemText(0, _translate("Widget", "ReLu"))
        self.activationBox.setItemText(1, _translate("Widget", "Sigmoid"))
        self.activationBox.setItemText(2, _translate("Widget", "Tanh"))
        self.convBox.setItemText(0, _translate("Widget", "5x5"))
        self.convBox.setItemText(1, _translate("Widget", "2x 3x3"))
        self.batchBox.setItemText(0, _translate("Widget", "Да"))
        self.batchBox.setItemText(1, _translate("Widget", "Нет"))
        self.optimazerBox.setItemText(0, _translate("Widget", "Adam"))
        self.optimazerBox.setItemText(1, _translate("Widget", "SGD"))
        self.gpuBox.setItemText(0, _translate("Widget", "GPU"))
        self.gpuBox.setItemText(1, _translate("Widget", "CPU"))
        self.lossBox.setItemText(0, _translate("Widget", "Cross Entropy"))
        self.lossBox.setItemText(1, _translate("Widget", "MSE"))
        self.label_5.setText(_translate("Widget", "    Выберете нейросеть"))
        self.learnButton.setText(_translate("Widget", "Обучить нейросеть"))
        self.label_6.setText(_translate("Widget", "   Настройки нейросети:"))
        self.label_7.setText(_translate("Widget", "   Настройки обучения:"))
        self.label_13.setText(_translate("Widget", " Функция \n"
" активации:"))
        self.label_14.setText(_translate("Widget", " С батч-\n"
" нормализацией"))
        self.label_15.setText(_translate("Widget", " Pooling:"))
        self.label_16.setText(_translate("Widget", " Свертка:"))
        self.label_17.setText(_translate("Widget", " Запустить\n"
" на:"))
        self.label_18.setText(_translate("Widget", " Loss \n"
" функция:"))
        self.label_19.setText(_translate("Widget", "  Оптимизатор:"))
        self.label_8.setText(_translate("Widget", "    Изменение точности/loss от эпох"))
        # self.label_9.setText(_translate("Widget", "    Изменение  Loss функции от эпох"))
        self.label_11.setText(_translate("Widget", "  Результат:"))
        self.label_12.setText(_translate("Widget", " Нарисовать или загрузить картинку:"))
        self.clearButton.setText(_translate("Widget", "Очистить"))
        self.LoadButton.setText(_translate("Widget", "Загрузить картинку"))
        self.goButton.setText(_translate("Widget", "Обработать"))

    def on_clear_click(self):
         self.paint_scene.clear()
    
    def on_go_click(self):
        self.img = self.paint.grab()
        if self.datasetBox.currentText() == "MNIST":
                self.img = self.img.scaled(28, 28).toImage()
                self.img = qimage2ndarray.rgb_view(self.img)
                # self.img =self.img.mean(axis=-1)
        else:
             self.img = self.img.scaled(32, 32).toImage()
             self.img = qimage2ndarray.rgb_view(self.img)
        transform = transforms.ToTensor()
        self.img = transform(self.img.copy())
        print(self.img[0].shape())
        self.resaultLabel.setText(self.model.ManTest(self.img))

#     def on_go_click(self):
#           pixmap = self.paint.grabWindow(0, self._x, self._y, self._width, self._height)
#           print(pixmap)
#         self.pixmap2 = self.paint.grab(self.paint.sceneRect().toRect())
#         print(self.pixmap2)
#         # Check the current dataset
#         if self.datasetBox.currentText() == "MNIST":
#                 self.img = self.pixmap2.scaled(28, 28).toImage()
#                 width = self.img.width()
#                 height = self.img.height()

#                 # Convert QImage to numpy array
#                 buffer = self.img.bits()
#                 print(buffer)
#                 # buffer.setsize(self.img.byteCount())
#                 # numpy_array = np.frombuffer(buffer, dtype=np.uint8).reshape((height, width, 4))

#                 # # Convert numpy array to torch.FloatTensor
#                 # float_tensor = torch.from_numpy(numpy_array).float()
#                 # print(float_tensor)
#                 # self.img = ImageQt(self.img)
#                 # transform = transforms.ToTensor()
#                 # self.img = transform(self.img)

#         else:
#                 self.img = self.pixmap2.scaled(32, 32).toImage()
#                 # self.img = Image.fromqimage(self.img)
#                 # transform = transforms.ToTensor()
#                 # self.img = transform(self.img)
#         # self.model.ManTest(self.img)
                

#     def weight_img(self, img):
#         width, height = img.width(), img.height()
#         img = img.scaled(self.scale, self.scale)
#         if
#         img = img.convertToFormat(QImage.Format_Grayscale8)
#         weight = []

#         for i in range(self.scale):
#                 for j in range(self.scale):
#                         pixel_value = img.pixelColor(i, j).black()
#                         normalized_value = pixel_value / 255.0
#                         weight.append(normalized_value)

#         return weight
    
    def on_load_button_click(self):
        msgBox = QtWidgets.QMessageBox()
        fileName, _ = QFileDialog.getOpenFileName(None, "Выберете файл", "", "*.png")

        self.paint_scene.clear()

        if fileName:
            img = QtGui.QPixmap(fileName)

            if img.isNull() or img.width() > 2512 or img.height() > 2512:
                msgBox.setText("Или картинка большая, или путь неверный")
                msgBox.exec()
            else:
                img = img.scaled(200, 200, Qt.KeepAspectRatio)
                pixmap_item = QGraphicsPixmapItem(img)
                self.paint_scene.addItem(pixmap_item)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
