'''
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH
from numpy import pi
import matplotlib.pyplot as plt

elo1 = RevoluteDH(d=0.088, a=0,     alpha = pi/2)
elo2 = RevoluteDH(d=0,    a=0.106, alpha = 0)
elo3 = RevoluteDH(d=0,    a=0.101, alpha = 0)
elo4 = RevoluteDH(d=0,    a=0,     alpha = -pi/2)
elo5 = RevoluteDH(d=0.171, a=0,     alpha = 0)

lista_elos = [elo1, elo2, elo3, elo4, elo5]

robot = DHRobot(lista_elos, name = 'manip_roboticaNaEscola')
robot.plot([0,0,0,0,0], block=True, name=False)
'''

import roboticstoolbox as rtb
from roboticstoolbox.backends.PyPlot import PyPlot
from numpy import pi

elo1 = rtb.RevoluteDH(d=0.088, a=0,     alpha = pi/2)
elo2 = rtb.RevoluteDH(d=0,     a=0.106, alpha = 0)
elo3 = rtb.RevoluteDH(d=0,     a=0.101, alpha = 0)
elo4 = rtb.RevoluteDH(d=0,     a=0,     alpha = -pi/2)
elo5 = rtb.RevoluteDH(d=0.171, a=0,     alpha = 0)

lista_elos = [elo1, elo2, elo3, elo4, elo5]

robot = rtb.DHRobot(lista_elos, name = 'manip_roboticaNaEscola')
robot.plot([0,0,0,0,0], block=True)
# pyplot = PyPlot()  # create a PyPlot backend
# pyplot.add(robot)              # add the robot to the backend
# robot.q = robot.qz             # set the robot configuration
# pyplot.step()                  # update the backend and graphical view
