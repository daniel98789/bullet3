import pybullet_data
import time
import pybullet as p
import os
import numpy as np

'''
Class PyBulletEnv:
Wrapper that contains all relevant environment information, including information about the number of
obj classes that have so far been instantiated.

Author: Stacy Gaikovaia 


Function setup:
    Initialize the GUI, set the gravity, add information into the search path,
    configure the visualizer

Function run:
    Run the simulation

'''

class PyBulletEnv:
    #camera = Camera()

    def __init__(self):
        print("Hello")

    def setup(self):
        p.connect(p.GUI)
        p.setGravity(0, 0, -9.8)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setAdditionalSearchPath(os.getcwd()+"data/") # So we can render custom shapes directly!
        # Make an infinite floor!
        p.loadURDF("plane100.urdf", useMaximalCoordinates=True)

        #disable rendering during creation.
        p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 0)
        p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
        #disable tinyrenderer, software (CPU) renderer, we don't use it here
        p.configureDebugVisualizer(p.COV_ENABLE_TINY_RENDERER, 0)


    def numBodies(self):
        return p.getNumBodies()

    def reset(self):
        p.resetSimulation()

    def run(self):
        p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 1)
        p.setRealTimeSimulation(1)
        while(1):
            time.sleep(1./240.)
            #camInfo = p.getDebugVisualizerCamera()
            #viewMat = camData[2]
            #projMat = camData[3]


    def analyze(self, obj, IDArray):
        cameraPos = np.array((0, 0, 0))
        distances = []
        positions = []


        # Get the max distance and generate a position array
        for (pos, _) in [p.getBasePositionAndOrientation(val) for val in IDArray]:
            #print(pos, orr)
            x, y, z = pos
            positions.append(pos)
            distances.append(np.linalg.norm(cameraPos - np.array((x, y, z))))

        norm = [float(i)/max(distances) for i in distances]
        
        #print(norm)
        # Replace all the old objects with new ones!
        for i, val in enumerate(IDArray):
            decRatio = max(round(1.0 - norm[i], 2), 0.1) # Don't want to decimate to any less than 10% of the origial faces
            #print(decRatio)
            p.removeBody(val)
            obj.createObjectURDF(positions[i], decRatio)
        return
