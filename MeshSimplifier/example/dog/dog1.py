import pybullet as p
import time
import pybullet_data
import pathlib

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(str(pathlib.Path(__file__).parent.absolute()) + "/simple_dog")

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")


#dog1 = p.loadURDF("simple_dog1.obj.urdf", [-10, 0, 0.1], [0, 0, 0, 1])
#dog2 = p.loadURDF("simple_dog2.obj.urdf", [-6, 0, 0.1], [0, 0, 0, 1])
#dog3 = p.loadURDF("simple_dog3.obj.urdf", [-2, 0, 0.1], [0, 0, 0, 1])
#dog4 = p.loadURDF("simple_dog4.obj.urdf", [2, 0, 0.1], [0, 0, 0, 1])
#dog5 = p.loadURDF("simple_dog5.obj.urdf", [6, 0, 0.1], [0, 0, 0, 1])
#dog6 = p.loadURDF("simple_dog6.obj.urdf", [10, 0, 0.1], [0, 0, 0, 1])
dt = 1./60.
p.setTimeStep(dt)

lastCameraDistance = p.getDebugVisualizerCamera()[10]

dog = p.loadURDF("simple_dog0.obj.urdf", [0, 0, 0.1], [0, 0, 0, 1])

while (1):
    cameraDistance = p.getDebugVisualizerCamera()[10]
    if abs(cameraDistance-lastCameraDistance) >= 1:
        print("swapping dog")
        dogNum = cameraDistance-4
        if dogNum > 6:
            dogNum = 6
        elif dogNum < 0:
            dogNum = 0
        else:
            position = p.getBasePositionAndOrientation(dog)[0]

            dog_temp = p.loadURDF("simple_dog"+str(int(dogNum))+".obj.urdf", position, [0, 0, 0, 1])
            p.removeBody(dog)
            dog = dog_temp
            lastCameraDistance = cameraDistance

    p.stepSimulation()
    time.sleep(dt)