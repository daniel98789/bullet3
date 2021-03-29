import pybullet as p
import time
import pybullet_data
import pathlib

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(str(pathlib.Path(__file__).parent.absolute()) + "/simple_pig")

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")

dt = 1./60.
p.setTimeStep(dt)

lastCameraDistance = p.getDebugVisualizerCamera()[10]

pig = p.loadURDF("simple_pig0.obj.urdf", [0, 0, 0.1], [0, 0, 0, 1])

while (1):
    cameraDistance = p.getDebugVisualizerCamera()[10]
    if abs(cameraDistance-lastCameraDistance) >= 1:
        print("swapping pig")
        pigNum = cameraDistance-4
        if pigNum > 6:
            pigNum = 6
        elif pigNum < 0:
            pigNum = 0
        else:
            position = p.getBasePositionAndOrientation(pig)[0]

            pig_temp = p.loadURDF("simple_pig"+str(int(pigNum))+".obj.urdf", position, [0, 0, 0, 1])
            p.removeBody(pig)
            pig = pig_temp
            lastCameraDistance = cameraDistance

    p.stepSimulation()
    time.sleep(dt)