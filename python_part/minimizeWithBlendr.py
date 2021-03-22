import bpy

DECIMATION_RATIO = 0.001

'''
Class MeshDecimator:
Calls headless blender in order to decimate relevant Obj instance
Author: Stacy Gaikovaia 


'''
class MeshDecimator:
    def __init__(self):

        return

    def delete_crap(self):
        bpy.ops.object.select_all(action="DESELECT")
        # Blender has a bunch of pre-done objects
        # stuff = ["Camera", "Cube", "Lamp"]
        stuff = ["Cube"]
        for s in stuff: 
            bpy.data.objects[s].select = True
            bpy.ops.object.delete()

    def get_meshes(self):
        meshes = []
        for obj in bpy.data.objects:
            if (obj.type == "MESH") and obj.name != 'Cube':
                meshes.append(obj)
        return meshes


    def main(self, input_model):
        inpa, inpb = input_model.split('.')
        output_model = inpa + "_SMALLER" + '.' + inpb
        #self.delete_crap()
        bpy.ops.import_scene.obj(filepath=input_model)

        meshes = self.get_meshes()

        print("meshes: ")
        print(meshes)
        

        for (_, obj) in enumerate(meshes):
            #bpy.context.scene.objects.active = obj
            modifier = obj.modifiers.new('DecimateMod', 'DECIMATE')
            modifier.ratio = DECIMATION_RATIO
            modifier.use_collapse_triangulate = True
            # NEW API uses: 
            bpy.ops.object.modifier_apply(modifier = 'DecimateMod')
            # Old API : 
            # bpy.ops.object.modifier_apply(apply_as='DATA', modifier = 'DecimateMod')
            print("{} has {} verts, {} edges, {} polys after decimation".format(obj.name, len(obj.data.vertices), len(obj.data.edges), len(obj.data.polygons)))

        bpy.ops.export_scene.obj(filepath=output_model)
        print("Written to file " + output_model)

# main('data/trees9.obj')

md = MeshDecimator()
md.main('data/deer.obj')


