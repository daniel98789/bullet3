from pySimplify import pySimplify
import trimesh as tr

bunny = tr.load_mesh('Stanford_Bunny_sample.stl')
simplify = pySimplify()
simplify.setMesh(bunny)
simplify.simplify_mesh(target_count = 1000, aggressiveness=7, preserve_border=True, verbose=10)