# ------------------------------------------------------
# ---------------------- main.py -----------------------
# ------------------------------------------------------
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

import numpy as np
import random
import logo

import roboticstoolbox as rtb

import matplotlib.pyplot as plt

from PIL import Image

class MatplotlibWidget(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self)

        loadUi("qt_braco_robo.ui",self)
        width = 1004
        height = 702

        # Colocando tamanho da janela fixo
        self.setFixedSize(width, height)
        self.setWindowTitle("Controle Manipulador Robótico - RE")

        self.play_bt.clicked.connect(self.update_graph)

        #Liga o menu do matplot
        #self.addToolBar(NavigationToolbar(self.MpWidget.canvas, self))

        self.elo1 = rtb.RevoluteDH(d=0.088, a=0,     alpha = np.pi/2)
        self.elo2 = rtb.RevoluteDH(d=0,     a=0.106, alpha = 0, offset = np.pi/2)
        self.elo3 = rtb.RevoluteDH(d=0,     a=0.101, alpha = 0, offset = -np.pi/2)
        self.elo4 = rtb.RevoluteDH(d=0,     a=0,     alpha = -np.pi/2)
        self.elo5 = rtb.RevoluteDH(d=0.171, a=0,     alpha = 0)

        self.lista_elos = [self.elo1, self.elo2, self.elo3, self.elo4, self.elo5]

        self.robot = rtb.DHRobot(self.lista_elos, name = 'manip_roboticaNaEscola')


    def update_graph(self):
        '''
        fs = 500
        f = random.randint(1, 100)
        ts = 1/fs
        length_of_signal = 100
        t = np.linspace(0,1,length_of_signal)

        cosinus_signal = np.cos(2*np.pi*f*t)
        sinus_signal = np.sin(2*np.pi*f*t)

        self.MpWidget.canvas.axes.clear()
        self.MpWidget.canvas.axes.plot(t, cosinus_signal)
        self.MpWidget.canvas.axes.plot(t, sinus_signal)
        self.MpWidget.canvas.axes.legend(('cosinus', 'sinus'),loc='upper right')
        self.MpWidget.canvas.axes.set_title('Cosinus - Sinus Signal')
        self.MpWidget.canvas.draw()
        '''
        self.robot.plot([0,0,0,0,0], block=False, movie='teste.gif')

        img = Image.open("teste.gif")
        plt.imshow(img)
        #self.MpWidget.canvas.axes.plot(img)
        #self.canvas.axes = self.canvas.figure.add_subplot(img)
        #self.MpWidget.canvas.draw()


app = QApplication([])
window = MatplotlibWidget()
window.show()
app.exec_()
