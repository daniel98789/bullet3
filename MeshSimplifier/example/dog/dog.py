import pybullet as p
import time
import pybullet_data
import pathlib

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(str(pathlib.Path(__file__).parent.absolute()) + "/simple_dog")

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
dog0 = p.loadURDF("simple_dog0.obj.urdf", [0, -5, 0.1], [0, 0, 0, 1])
dog1 = p.loadURDF("simple_dog1.obj.urdf", [-10, 0, 0.1], [0, 0, 0, 1])
dog2 = p.loadURDF("simple_dog2.obj.urdf", [-6, 0, 0.1], [0, 0, 0, 1])
dog3 = p.loadURDF("simple_dog3.obj.urdf", [-2, 0, 0.1], [0, 0, 0, 1])
dog4 = p.loadURDF("simple_dog4.obj.urdf", [2, 0, 0.1], [0, 0, 0, 1])
dog5 = p.loadURDF("simple_dog5.obj.urdf", [6, 0, 0.1], [0, 0, 0, 1])
dog6 = p.loadURDF("simple_dog6.obj.urdf", [10, 0, 0.1], [0, 0, 0, 1])
dt = 1./240.
p.setTimeStep(dt)

while (1):
    p.stepSimulation()
    time.sleep(dt)