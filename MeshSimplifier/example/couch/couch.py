import pybullet as p
import time
import pybullet_data
import pathlib

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(str(pathlib.Path(__file__).parent.absolute()))

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
couchId = p.loadURDF("couch.obj.urdf", [0, 0, 0.2], [1, 0, 0, 1])
dt = 1./240.
p.setTimeStep(dt)

while (1):
    p.stepSimulation()
    time.sleep(dt)