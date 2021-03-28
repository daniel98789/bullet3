import os
import sys
import pathlib

from object2urdf import ObjectUrdfBuilder

# Build single URDFs
object_folder = str(pathlib.Path(__file__).parent.absolute())

builder = ObjectUrdfBuilder(object_folder, urdf_prototype="_prototype.urdf")

builder.build_urdf(filename=object_folder + "/couch.obj", force_overwrite=True, decompose_concave=True, force_decompose=False, center = 'None')

object_folder = str(pathlib.Path(__file__).parent.absolute()) + "/simple_couch"

builder = ObjectUrdfBuilder(object_folder)

builder.build_library(force_overwrite=True, decompose_concave=True, force_decompose=False, center = 'None')