import os
import sys
import pathlib
from object2urdf import ObjectUrdfBuilder

# Build single URDFs
object_folder = str(pathlib.Path(__file__).parent.absolute()) + "/basketball"

builder = ObjectUrdfBuilder(object_folder, urdf_prototype='_prototype_ball.urdf')
builder.build_urdf(filename=str(pathlib.Path(__file__).parent.absolute()) + "/basketball/ball/basketball_corrected.obj", force_overwrite=True, decompose_concave=True, force_decompose=False, center = 'mass')
