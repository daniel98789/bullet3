import pybullet as p
import time
import pybullet_data
import pathlib

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(str(pathlib.Path(__file__).parent.absolute()) + "/simple_couch")

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
couch1 = p.loadURDF("simple_couch1.obj.urdf", [0, 0, 0.2], [1, 0, 0, 1])
couch2 = p.loadURDF("simple_couch2.obj.urdf", [2, 0, 0.2], [1, 0, 0, 1])
couch3 = p.loadURDF("simple_couch3.obj.urdf", [4, 0, 0.2], [1, 0, 0, 1])
couch4 = p.loadURDF("simple_couch4.obj.urdf", [6, 0, 0.2], [1, 0, 0, 1])
couch5 = p.loadURDF("simple_couch5.obj.urdf", [8, 0, 0.2], [1, 0, 0, 1])
couch6 = p.loadURDF("simple_couch6.obj.urdf", [10, 0, 0.2], [1, 0, 0, 1])
dt = 1./240.
p.setTimeStep(dt)

while (1):
    p.stepSimulation()
    time.sleep(dt)