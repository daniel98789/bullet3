import pybullet as p
import pybullet_data as pd
import math
import time
import numpy as np
from pybullet_envs.examples import panda_sim
import profiler
import debugvisualizer

p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_Y_AXIS_UP,1)
p.setAdditionalSearchPath(pd.getDataPath())

timeStep=1./120.
p.setTimeStep(timeStep)
p.setGravity(0,-9.8,0)
 
panda = panda_sim.PandaSim(p,[0,0,0])
start_time = time.time()
prev_loc = None
prof = profiler.Profiler(p,[panda.panda])
prof.select_object_to_get_pos_ori(panda.panda)

p.resetDebugVisualizerCamera( cameraDistance=1.4, cameraYaw=40, cameraPitch=-30, cameraTargetPosition=[0,0,0])
x = 1
y = 0
z = 0
while (1):
	curr_time = time.time()
	# if curr_time - start_time > 2:
	# 	found, loc = debugvisualizer.object_is_in_frame(p, panda.panda, prev_loc)
	# 	if found:
	# 		prev_loc = loc
	# 	start_time = curr_time
	# 	x = x + 1
	# 	cam_info = p.getDebugVisualizerCamera()

	panda.step()
	p.stepSimulation()
	
	# prof.profile(127)
	time.sleep(timeStep)

	
