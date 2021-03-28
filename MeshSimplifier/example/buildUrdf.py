import os
import sys
import pathlib

from object2urdf import ObjectUrdfBuilder

# Build single URDFs
object_folder = str(pathlib.Path(__file__).parent.absolute()) + "/pig"

builder = ObjectUrdfBuilder(object_folder, urdf_prototype="_prototype.urdf")

builder.build_urdf(filename=str(pathlib.Path(__file__).parent.absolute()) + "/pig/pig.obj", force_overwrite=True, decompose_concave=True, force_decompose=False, center = 'None')