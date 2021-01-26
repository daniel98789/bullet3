import pybullet as p
import time
import pybullet_data

def makeClient():
    physicsClient = p.connect(p.GUI)
    p.setGravity(0, 0, -9.8)

    # p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setPhysicsEngineParameter(numSolverIterations=10)
    p.setTimeStep(1. / 120.)
    # logId = p.startStateLogging(p.STATE_LOGGING_PROFILE_TIMINGS, "visualShapeBench.json")
    #useMaximalCoordinates is much faster then the default reduced coordinates (Featherstone)
    p.loadURDF("plane100.urdf", useMaximalCoordinates=True)
    #disable rendering during creation.
    p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 0)
    p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
    #disable tinyrenderer, software (CPU) renderer, we don't use it here
    p.configureDebugVisualizer(p.COV_ENABLE_TINY_RENDERER, 0)

    return physicsClient


def makeshape():
    shift = [1, 1, 1]
    meshScale = [0.01, 0.01, 0.01]
    #the visual shape and collision shape can be re-used by all createMultiBody instances (instancing)
    pClient = makeClient()
    
    # CREATE FROM FILE, visual shape different from collision shape 
    #visualShapeId = p.createVisualShape(shapeType=p.GEOM_MESH,
    #                                    fileName="duck.obj",
    #                                    rgbaColor=[1, 1, 1, 1],
    #                                    specularColor=[0.4, .4, 0],
    #                                    visualFramePosition=shift,
    #                                    meshScale=meshScale)
    collisionShapeId = p.createCollisionShape(shapeType=p.GEOM_MESH,
                                          #fileName="teddy2_VHACD_CHs.obj",
                                          #fileName="duck_vhacd.obj",
                                          #fileName="data/cow.obj",
                                          fileName="data/deer.obj",
                                          collisionFramePosition=shift,
                                          meshScale=meshScale,
                                          flags=p.GEOM_FORCE_CONCAVE_TRIMESH)


    p.createMultiBody(baseMass = 1,
                      baseInertialFramePosition=[0, 0, 0],
                      baseCollisionShapeIndex=collisionShapeId,
                      #baseVisualShapeIndex=visualShapeId,
                      basePosition=[meshScale[0] * 2,
                                    meshScale[1] * 2, 
                                    1],
                        useMaximalCoordinates=True)
    p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 1)
    p.setRealTimeSimulation(1)
    while(1):
        time.sleep(1./240.)

    print("visual shape is:")
    #print(visualShapeId)


if __name__ == "__main__":
    makeshape()


