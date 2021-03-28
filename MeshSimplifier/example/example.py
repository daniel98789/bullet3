import pybullet as p
import time
import pybullet_data
import profiler
import pathlib

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(str(pathlib.Path(__file__).parent.absolute()) + "/pig")

p.setGravity(0,0,-9.8)
#planeId = p.loadURDF("plane.urdf")
pigId = p.loadURDF("pig.obj.urdf", [0, 0, 0.4])
dt = 1./240.
p.setTimeStep(dt)
print(pigId)
prof = profiler.Profiler(p,[pigId])
prof.select_object_to_get_pos_ori(pigId)

while (1):
    p.stepSimulation()
    time.sleep(dt)
    prof.profile(127)