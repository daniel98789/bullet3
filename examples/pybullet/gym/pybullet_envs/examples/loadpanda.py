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

while (1):
	start_time = time.time()
	panda.step()
	p.stepSimulation()
	#time.sleep(timeStep)
	frameCounter += 1
	#print(frameCounter)
	numBodies = p.getNumBodies()
	print(numBodies)
	"""p.addUserDebugText(str(frameCounter), [10, 0, 0.1],
				textColorRGB=[1, 0, 0],
				textSize=1.5,
				lifeTime=0.5)

	p.addUserDebugText(str(1.0/(time.time() - start_time)), [10, 0, 1],
				textColorRGB=[1, 0, 0],
				textSize=1.5,
				lifeTime=0.5)
"""
	p.addUserDebugText(str(numBodies), [10, 0, 1],
				textColorRGB=[1, 0, 0],
				textSize=1.5,
 				lifeTime=0.5)
