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
	position = p.getBasePositionAndOrientation(panda.panda)
	numJoints = p.getNumJoints(panda.panda)
	#velocity = p.getBaseVelocity(panda.ball1)

	if curr_time - start_time > update_interval:
		start_time = curr_time

		p.addUserDebugText("Joint Count: " + str(numJoints), 
					[10, -0.5, -1.5],
					textColorRGB=[0, 0, 0],
					textSize=1.3,
					lifeTime=update_interval+0.1)

		p.addUserDebugText("Position: " + "x: " + str(position[0][0]) + " y: " + str(position[0][1]) + " z: " + str(position[0][2]), 
					[10, 0.5, -1.07],
					textColorRGB=[0, 0, 0],
					textSize=1.3,
					lifeTime=update_interval+0.1)
		
		p.addUserDebugText("Orientation: " "x: " + "{:.2f}".format(position[1][0]) + " y: " + str(position[1][1]) + " z: " + str(position[1][2]), 
					[10, 0, -1.29],
					textColorRGB=[0, 0, 0],
					textSize=1.3,
					lifeTime=update_interval+0.1)

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
