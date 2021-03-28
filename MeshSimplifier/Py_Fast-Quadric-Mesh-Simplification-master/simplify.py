from pySimplify import pySimplify
import trimesh as tr
import sys
import os.path
import shutil as sh

ASSETS_DIR = '../assets/'

obj_file_name = sys.argv[1]
ext = os.path.splitext(obj_file_name)[1]
if ext != '.obj':
	print("Unexpected File type: " + ext + ", please provide a valid file type")
	exit()

obj_name = os.path.splitext(obj_file_name)[0]
OBJ_DIR = ASSETS_DIR+obj_name+"/"

try:
	obj_file = open(ASSETS_DIR+'base_assets/'+obj_file_name,'r')
except:
	print("base asset \'" + ASSETS_DIR+'base_assets/'+obj_file_name + "\' does not exist")
	exit()

sys.stdout = open(os.devnull, 'w')

kwargs = tr.exchange.obj.load_obj(obj_file)
mesh = tr.exchange.load.load_kwargs(kwargs)


simplify = pySimplify()

if (os.path.exists(OBJ_DIR)):
	sh.rmtree(OBJ_DIR)
	os.mkdir(OBJ_DIR)
	print("directory existed")
else:
	os.mkdir(OBJ_DIR)
	

sh.copy(ASSETS_DIR+'base_assets/'+obj_file_name,OBJ_DIR+'simple_'+ obj_name +str(0)+'.obj')

for i in range(1,7):
	simplify.setMesh(mesh)
	simplify.simplify_mesh(target_count = 1000, aggressiveness=i, preserve_border=True, verbose=10)
	reduced_mesh = simplify.getMesh()

	reduced_file = open(OBJ_DIR+'simple_'+ obj_name +str(i)+'.obj','w')
	reduced_obj = tr.exchange.obj.export_obj(reduced_mesh,include_color=True)

	reduced_file.write(reduced_obj)

sys.stdout = sys.__stdout__