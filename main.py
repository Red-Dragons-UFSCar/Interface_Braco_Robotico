# ------------------------------------------------------
# ---------------------- main.py -----------------------
# ------------------------------------------------------
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

import numpy as np
import random
import logo

import matplotlib.pyplot as plt

import sim , simConst
import time
from numpy import pi

class MatplotlibWidget(QMainWindow):

    def __init__(self, clientid):
        error = []
        self.clientID = clientid
        

        _,self.joint0h = sim.simxGetObjectHandle(self.clientID, "/PhantomXPincher/joint0/" ,sim.simx_opmode_blocking)
        _,self.joint1h = sim.simxGetObjectHandle(self.clientID, "/PhantomXPincher/joint0/link/joint1/" ,sim.simx_opmode_blocking)
        _,self.joint2h = sim.simxGetObjectHandle(self.clientID, "/PhantomXPincher/joint0/link/joint1/link/joint2" ,sim.simx_opmode_blocking)
        _,self.joint3h = sim.simxGetObjectHandle(self.clientID, "/PhantomXPincher/joint0/link/joint1/link/joint2/link/joint3" ,sim.simx_opmode_blocking)
        _,self.joint4h = sim.simxGetObjectHandle(self.clientID, "/PhantomXPincher/joint0/link/joint1/link/joint2/link/joint3/link/joint4" ,sim.simx_opmode_blocking)
        error,self.gripper1h = sim.simxGetObjectHandle(self.clientID, "/PhantomXPincher/joint0/link/joint1/link/joint2/link/joint3/link/joint4/base/gripperCenter_joint/" ,sim.simx_opmode_blocking)
        _,self.gripper2h = sim.simxGetObjectHandle(self.clientID, "/PhantomXPincher/joint0/link/joint1/link/joint2/link/joint3/link/joint4/base/gripperCenter_joint/fingerLeft/gripperClose_joint" ,sim.simx_opmode_blocking)
        
        if error != 0:
            print("Deu ruim!")
            print(error)
        else:
            print("Foi mlk!")

        QMainWindow.__init__(self)

        loadUi("qt_braco_robo.ui",self)
        width = 1004
        height = 702

        # Colocando tamanho da janela fixo
        self.setFixedSize(width, height)
        self.setWindowTitle("Controle Manipulador Robótico - RE")

        self.horizontalSlider.valueChanged.connect(self.set_DOF0)
        self.horizontalSlider_2.valueChanged.connect(self.set_DOF1)
        self.horizontalSlider_3.valueChanged.connect(self.set_DOF2)
        self.horizontalSlider_4.valueChanged.connect(self.set_DOF3)
        self.horizontalSlider_5.valueChanged.connect(self.set_DOF4)
        self.horizontalSlider_6.valueChanged.connect(self.set_DOF5)

    def set_DOF0(self):

        sim.simxSetJointPosition(self.clientID,self.joint0h,self.horizontalSlider.value()*(pi)/100,sim.simx_opmode_oneshot)
    def set_DOF1(self):

        sim.simxSetJointPosition(self.clientID,self.joint1h,self.horizontalSlider_2.value()*(pi)/100,sim.simx_opmode_oneshot)
    def set_DOF2(self):

        sim.simxSetJointPosition(self.clientID,self.joint2h,self.horizontalSlider_3.value()*(pi)/100,sim.simx_opmode_oneshot)
    def set_DOF3(self):

        sim.simxSetJointPosition(self.clientID,self.joint3h,self.horizontalSlider_4.value()*(pi)/100,sim.simx_opmode_oneshot)
    def set_DOF4(self):

        sim.simxSetJointPosition(self.clientID,self.joint4h,self.horizontalSlider_5.value()*(pi)/100,sim.simx_opmode_oneshot)

    def set_DOF5(self):

        g1 = 0.0184*(1 - 0.01*self.horizontalSlider_6.value())
        g2 = 0.0368*(1 - 0.01*self.horizontalSlider_6.value())

        sim.simxSetJointPosition(self.clientID,self.gripper1h,g1,sim.simx_opmode_oneshot)
        sim.simxSetJointPosition(self.clientID,self.gripper2h,g2,sim.simx_opmode_oneshot)

sim.simxFinish(-1)
clientID = sim.simxStart('127.0.0.1',19997,True,True,5000,5) # Connect to V-REP


#Se houve a comunicação com sucesso ativa a flagComunicar
if clientID!=-1:
    print ('Connected to remote API server')

#Se houve erro na comunicação não ativa
else:
    print('Connection not successful')

sim.simxStartSimulation(clientID,sim.simx_opmode_blocking)
error, joint0h = sim.simxGetObjectHandle(clientID, "/PhantomXPincher/joint0/" ,sim.simx_opmode_blocking)

app = QApplication([])
window = MatplotlibWidget(clientID)
window.show()
app.exec_()
