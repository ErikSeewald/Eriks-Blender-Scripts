import bpy  # gives access to Blender function from Python
import math

import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)

import cube_creator
from ebs_point import Point
from ebs_path import Path
import ebs_util



def clearScene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def cubeTest() -> None:
    for i in range(5):
        cube_creator.add_cube(location=[i * 5, 0, 0])
        newcube = bpy.context.object
        newcube.name = "Cube -" + str(i)

        newcube.rotation_euler = [0, 0, 0]
        newcube.keyframe_insert(data_path="rotation_euler", frame=1)

        newcube.rotation_euler = [0, 0, math.radians(45 + i * 15)]
        newcube.keyframe_insert(data_path="rotation_euler", frame=30)


def main():
            
    ebs_util.object_mode()
    ebs_util.clearScene()
    
    path = Path((Point(0, 0, 0), Point(0, 2, 2), Point(1, 4, 4), Point(1,4,6)))
    path.add_volume()
    path.add_arrow()

main()
