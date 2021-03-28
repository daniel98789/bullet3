import pybullet as p
import pybullet_data as pd
import math
import time
import numpy as np
from pybullet_envs.examples import panda_sim
import profiler

p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_Y_AXIS_UP,1)
p.setAdditionalSearchPath(pd.getDataPath())

timeStep=1./120.
p.setTimeStep(timeStep)
p.setGravity(0,-9.8,0)
 
panda = panda_sim.PandaSim(p,[0,0,0])

prof = profiler.Profiler(p,[panda.panda])
prof.select_object_to_get_pos_ori(panda.panda)

p.resetDebugVisualizerCamera( cameraDistance=1.4, cameraYaw=40, cameraPitch=-30, cameraTargetPosition=[0,0,0])

while (1):
	panda.step()
	p.stepSimulation()
	
	prof.profile(127)
	time.sleep(timeStep)

	
