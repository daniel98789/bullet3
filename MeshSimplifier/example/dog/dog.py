import pybullet as p
import time
import pybullet_data
import pathlib

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(str(pathlib.Path(__file__).parent.absolute()) + "/simple_dog")

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
dog = p.loadURDF("simple_dog0.obj.urdf", [0, 0, 0.1], [0, 0, 0, 1])
#dog1 = p.loadURDF("simple_dog1.obj.urdf", [-10, 0, 0.1], [0, 0, 0, 1])
#dog2 = p.loadURDF("simple_dog2.obj.urdf", [-6, 0, 0.1], [0, 0, 0, 1])
#dog3 = p.loadURDF("simple_dog3.obj.urdf", [-2, 0, 0.1], [0, 0, 0, 1])
#dog4 = p.loadURDF("simple_dog4.obj.urdf", [2, 0, 0.1], [0, 0, 0, 1])
#dog5 = p.loadURDF("simple_dog5.obj.urdf", [6, 0, 0.1], [0, 0, 0, 1])
#dog6 = p.loadURDF("simple_dog6.obj.urdf", [10, 0, 0.1], [0, 0, 0, 1])
dt = 1./60.
p.setTimeStep(dt)

dogCounter = 0

last_time = time.time()

while (1):
    if time.time() - last_time >= 2:
        dogCounter += 1
        if dogCounter == 7:
            dogCounter = 0
        position = p.getBasePositionAndOrientation(dog)[0]
        print(position)
        dog_temp = p.loadURDF("simple_dog"+str(dogCounter)+".obj.urdf", position, [0, 0, 0, 1])
        p.removeBody(dog)
        dog = dog_temp
        last_time = time.time()

    p.stepSimulation()
    time.sleep(dt)