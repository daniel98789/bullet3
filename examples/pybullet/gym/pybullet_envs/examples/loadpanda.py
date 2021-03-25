import pybullet as p
import pybullet_data as pd
import math
import time
import numpy as np
from pybullet_envs.examples import panda_sim
import time

p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_Y_AXIS_UP,1)
p.setAdditionalSearchPath(pd.getDataPath())

timeStep=1./60.
p.setTimeStep(timeStep)
p.setGravity(0,-9.8,0)
 
panda = panda_sim.PandaSim(p,[0,0,0])

frameCounter = 0

start_time = time.time()
update_interval = 1
prev_count = 0 

while (1):
	panda.step()
	p.stepSimulation()
	time.sleep(timeStep)
	frameCounter += 1
	numBodies = p.getNumBodies()
	# print(numBodies)

	curr_time = time.time()
	if curr_time - start_time > update_interval:
		start_time = curr_time

		p.addUserDebugText("framecount: " + str(frameCounter), [10, 1, 0.1],
					textColorRGB=[1, 0, 0],
					textSize=1.5,
					lifeTime=update_interval)

		p.addUserDebugText("fps: " + str((frameCounter - prev_count)/update_interval), [10, 2, 1],
					textColorRGB=[1, 0, 0],
					textSize=1.5,
					lifeTime=update_interval)
		prev_count = frameCounter

		p.addUserDebugText("numBodies: " + str(numBodies), [10, 0, 0.1],
					textColorRGB=[1, 0, 0],
					textSize=1.5,
					lifeTime=update_interval)
