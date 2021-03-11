import pybullet_data
import time
import pybullet as p
import os

class PyBulletEnv:
    #camera = Camera()

    def __init__(self):
        print("Hello")

    def setup(self):
        p.connect(p.GUI)
        p.setGravity(0, 0, -9.8)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        #p.setAdditionalSearchPath(os.getcwd()+"data/")
        #p.resetSimulation()
        # Make the floor...
        p.loadURDF("plane100.urdf", useMaximalCoordinates=True)

        #disable rendering during creation.
        p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 0)
        p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
        #disable tinyrenderer, software (CPU) renderer, we don't use it here
        p.configureDebugVisualizer(p.COV_ENABLE_TINY_RENDERER, 0)

    def run(self):
        p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 1)
        p.setRealTimeSimulation(1)
        while(1):
            time.sleep(1./240.)
