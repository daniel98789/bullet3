import bpy

DECIMATION_RATIO = 0.1


def delete_crap():
    bpy.ops.object.select_all(action="DESELECT")
    stuff = ["Camera", "Cube", "Lamp"]
    for s in stuff: 
        bpy.data.objects[s].select = True
        bpy.ops.object.delete()

def get_meshes():
    meshes = []
    for obj in bpy.data.objects:
        if (obj.type == "MESH"):
            meshes.append(obj)
    return meshes


def main(input_model):
    inpa, inpb = input_model.split('.')
    output_model = inpa + "_SMALLER" + '.' + inpb
    delete_crap()
    bpy.ops.import_scene.obj(filepath=input_model)

    meshes = get_meshes()

    #print("meshes: ")
    #print(meshes)

    for (_, obj) in enumerate(meshes):
        bpy.context.scene.objects.active = obj
        modifier = obj.modifiers.new('DecimateMod', 'DECIMATE')
        modifier.ratio = DECIMATION_RATIO
        modifier.use_collapse_triangulate = True
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier = 'DecimateMod')
        print("{} has {} verts, {} edges, {} polys after decimation".format(obj.name, len(obj.data.vertices), len(obj.data.edges), len(obj.data.polygons)))

    bpy.ops.export_scene.obj(filepath=output_model)

main('data/trees9.obj')


