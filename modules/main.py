import bpy  # gives access to Blender function from Python
import math

import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)

import vector_creator
import cube_creator
from e_point import Point



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
    clearScene()

    # cubeTest()
    vector_creator.two_point_edge(Point(0, 0, 0), Point(0, 2, 5))
    vector_creator.path_from_points((Point(0, 0, 0), Point(0, 2, 2), Point(0, 3, 5), Point(2,4,2)))


main()
