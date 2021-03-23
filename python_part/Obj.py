import os
import pybullet as p
import subprocess

MINIMIZER = 'minimizeWithBlendr.py'

class Obj:
    
    def __init__(self, fn, scale):
        self.filename = os.getcwd()+fn
        self.smaller_filename = None
        self.v = []
        self.meshScale = [scale, scale, scale]
        self.obj = None

        return    


    def smaller(self, ratio):
        name, suff = self.filename.split(".")
        self.smaller_filename = name + "_" + str(ratio) + "." + suff
        subprocess.run(["blender", "-b", "-P", MINIMIZER, str(ratio), self.filename])
        # Once process has completed, we can grab the new dimensions??? 

        return None
    

    def createObject(self, position):
        #TODO: Add information about the number of vertices!
        
        _, suff = self.filename.split('.')
        uniqueID = -1
        if suff == "obj":
            # creating an obj
            visualShapeID = p.createVisualShape(
                shapeType = p.GEOM_MESH,
                filename = self.filename,
                rgbaColor = [1, 1, 1, 1],
                specularColor = [0.4, 0.4, 0],
                visualFramePosition = position,
                meshScale = self.meshScale
            )
            collisionShapeID = p.createCollisionShape (
                shapeType = p.GEOM_MESH,
                filename = self.filename,
                collisionFramePosition = position,
                meshScale = self.meshScale,
                flags = p.GEOM_FORCE_CONCAVE_TRIMESH
            )
            uniqueID = p.createMultiBody(
                baseMass = 1, #TODO: make a variable!
                baseInertialFramePosition = [0, 0, 0], #TODO: make a variable
                baseCollisionShapeIndex=collisionShapeID,
                baseVisualShapeIndex=visualShapeID,
                # basePosition=[meshScale[0] * 2, meshScale[1] * 2, 1],
                useMaximalCoordinates=True,
                useFixedBase = True
            )
        elif suff == "urdf":
            uniqueID = p.loadURDF()
        
        return uniqueID

    def move_x_y(self, x, y):
        if self.obj == None: 
            # TODO: Set up as an error
            print("Object not initialized!")
            return -1 
        #else, obj is a unique ID!
        pos, orient = p.getBasePositionAndOrientation(self.obj)
        _, _, oldZ = pos
        p.resetBasePositionAndOrientation(self.obj, [x, y, oldZ], orient)
        
        
    def change_position(self,roll, pitch, yaw):
        if self.obj == None:
            print("Object not initialized!")
            return -1

        # Otherwise, change it's position :) 
        pos, _ = p.getBasePositionAndOrientation(self.obj)
        orientation = p.getQuaternionFromEuler([roll, pitch, yaw])
        p.resetBasePositionAndOrientation(self.obj, pos, orientation)



