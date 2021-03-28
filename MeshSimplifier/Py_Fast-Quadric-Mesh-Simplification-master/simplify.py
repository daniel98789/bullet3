from pySimplify import pySimplify
import trimesh as tr


obj_file = open('pig.obj','r')
kwargs = tr.exchange.obj.load_obj(obj_file)
pig_mesh = tr.exchange.load.load_kwargs(kwargs)


simplify = pySimplify()
simplify.setMesh(pig_mesh)
simplify.simplify_mesh(target_count = 1000, aggressiveness=7, preserve_border=True, verbose=10)
smallPig = simplify.getMesh()

small_file = open('small_pig.obj','w')
small_obj = tr.exchange.obj.export_obj(smallPig,include_color=True)

small_file.write(small_obj)