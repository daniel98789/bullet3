import pybullet as p
import time
import pybullet_data
import pathlib
import debugvisualizer

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(str(pathlib.Path(__file__).parent.absolute()) + "/simple_pig")

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")

dt = 1./60.
p.setTimeStep(dt)

lastCameraDistance = p.getDebugVisualizerCamera()[10]

pig = p.loadURDF("simple_pig0.obj.urdf", [0, 0, 0.1], [0, 0, 0, 1])
pigNum = 0
prev_loc = None

prev_state = True
start_time = time.time()
x = 1

while (1):
    cameraDistance = p.getDebugVisualizerCamera()[10]
    if abs(cameraDistance-lastCameraDistance) >= 1:
        
        pigNum = cameraDistance-4
        if pigNum > 6:
            pigNum = 6
        elif pigNum < 0:
            pigNum = 0
        else:
            print("swapping pig to:" + str(int(pigNum)))
            position = p.getBasePositionAndOrientation(pig)[0]

            pig_temp = p.loadURDF("simple_pig"+str(int(pigNum))+".obj.urdf", position, [0, 0, 0, 1])
            p.removeBody(pig)
            pig = pig_temp
            lastCameraDistance = cameraDistance
    
    curr_time = time.time()
    if curr_time - start_time > 2:
        found, loc = debugvisualizer.object_is_in_frame(
            p, pig, prev_loc)
        if found != prev_state:
            
            if found:
                
                pigNum = cameraDistance-4-2
                if pigNum > 6:
                    pigNum = 6
                elif pigNum < 0:
                    pigNum = 0

                print("in view upgrading pig to: " + str(int(pigNum)))
                position = p.getBasePositionAndOrientation(pig)[0]

                pig_temp = p.loadURDF("simple_pig"+str(int(pigNum))+".obj.urdf", position, [0, 0, 0, 1])
                p.removeBody(pig)
                pig = pig_temp
                lastCameraDistance = cameraDistance
                
            else:
                pigNum = cameraDistance-4+2
                if pigNum > 6:
                    pigNum = 6
                elif pigNum < 0:
                    pigNum = 0

                print("out of view downgrading pig to: " + str(int(pigNum)))
                position = p.getBasePositionAndOrientation(pig)[0]

                pig_temp = p.loadURDF("simple_pig"+str(int(pigNum))+".obj.urdf", position, [0, 0, 0, 1])
                p.removeBody(pig)
                pig = pig_temp
                lastCameraDistance = cameraDistance

        start_time = curr_time
        x = x + 1
        cam_info = p.getDebugVisualizerCamera()
        prev_state = found

    p.stepSimulation()
    time.sleep(dt)