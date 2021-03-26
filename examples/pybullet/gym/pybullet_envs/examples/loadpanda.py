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

timeStep=1./120.
p.setTimeStep(timeStep)
p.setGravity(0,-9.8,0)
 
panda = panda_sim.PandaSim(p,[0,0,0])

frameCounter = 0

start_time = time.time()
update_interval = 0.5
prev_count = 0 

p.resetDebugVisualizerCamera( cameraDistance=1.4, cameraYaw=40, cameraPitch=-30, cameraTargetPosition=[0,0,0])

while (1):
	curr_time = time.time()

	panda.step()
	p.stepSimulation()
	time.sleep(timeStep)
	frameCounter += 1
	numBodies = p.getNumBodies()

	if curr_time - start_time > update_interval:
		start_time = curr_time

		p.addUserDebugText("Frame Counter: " + str(frameCounter), [10, 1.5, -0.625],
					textColorRGB=[0, 0, 0],
					textSize=1.3,
					lifeTime=update_interval+0.1)

		p.addUserDebugText("FPS: " + str((frameCounter - prev_count)/update_interval), [10, 2, -0.4],
					textColorRGB=[0, 0, 0],
					textSize=1.3,
					lifeTime=update_interval+0.1)
		prev_count = frameCounter

		p.addUserDebugText("Body Count: " + str(numBodies), [10, 1, -0.85],
					textColorRGB=[0, 0, 0],
					textSize=1.3,
					lifeTime=update_interval+0.1)
