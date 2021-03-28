import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath("/home/daniel/bullet3/MeshSimplifier/test")

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
pigId = p.loadURDF("ball.urdf", [0, 0, 0.4])
dt = 1./240.
p.setTimeStep(dt)
print(pigId)

while (1):
    p.stepSimulation()
    time.sleep(dt)