import os
import pybullet as p
import subprocess
import object2urdf

MINIMIZER = 'minimizeWithBlendr.py'

class Obj:
    
    def __init__(self, fn, scale):
        self.filename = fn
        self.smaller_filename = None
        self.scale = scale
        self.meshScale = [scale, scale, scale]
        self.obj = None

        return    


    def smaller(self, ratio):
        name, suff = self.filename.split(".")
        self.smaller_filename = name + "_" + str(ratio) + "." + suff
        ps = subprocess.Popen(["blender", "-b", "-P", MINIMIZER, "--", str(ratio), self.filename], stdout = subprocess.PIPE)
        output = subprocess.check_output(["grep", "after decimation"], stdin = ps.stdout)
        print(output)
        # Parse output to find new 
       # Find verts, edges, polys
        return None
    
    def toURDF(self):
        # TODO: Fix lol 
        builder = object2urdf.ObjectUrdfBuilder("data/cow")
        builder.build_urdf(filename=self.filename, force_overwrite=True, decompose_concave=False, force_decompose =False, center = "bottom")
        p.loadURDF("data/cow/data.urdf", globalScaling=self.scale, useFixedBase=True, basePosition = [0, 1, 3], baseOrientation=[1,1,1,1])

    def createObject(self, position):
        #TODO: Add information about the number of vertices!

        _, suff = self.filename.split('.')
        uniqueID = -1
        if suff == "obj":
            # creating an obj
            print(self.filename)
            visualShapeID = p.createVisualShape(
                shapeType = p.GEOM_MESH,
                fileName = self.filename,
                rgbaColor = [3, 1, 1, 1],
                specularColor = [0.4, 0.4, 0.4],
                visualFramePosition = position,
                meshScale = self.meshScale
            )
            print("TEST1")
            collisionShapeID = p.createCollisionShape (
                shapeType = p.GEOM_MESH,
                fileName = self.filename,
                #collisionFramePosition = position,
                meshScale = self.meshScale,
                #flags = p.GEOM_FORCE_CONCAVE_TRIMESH
            )

            #orn = p.getQuaternionFromEuler([0, 0, 0])
            uniqueID = p.createMultiBody(
                baseMass = 1, #TODO: make a variable!
                baseInertialFramePosition = [0, 0, 0], #TODO: make a variable
                baseCollisionShapeIndex=collisionShapeID,
                baseVisualShapeIndex=visualShapeID,
                basePosition = position,
                # useMaximalCoordinates=True,
            #    baseOrientation = orn
                #useFixedBase = True
            )
        elif suff == "urdf":
            uniqueID = p.loadURDF(self.filename)
        
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



