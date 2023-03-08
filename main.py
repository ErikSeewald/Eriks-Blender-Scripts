import bpy  # gives access to Blender function from Python
import math
import E_Vectors.vector_creator as vC


# docs httpsdocs.blender.orgapicurrentbpy.ops.mesh.html#bpy.ops.mesh.primitive_cube_add
def add_cube(
        size: float = 1.0,
        location: list[float] = [0.0, 0.0, 0.0],
        rotation: list[float] = [0.0, 0.0, 0.0],
        scale: list[float] = [2.0, 2.0, 2.0]) -> None:
    bpy.ops.mesh.primitive_cube_add(
        size=size,
        calc_uvs=True,
        enter_editmode=False,
        align='WORLD',
        location=location,
        rotation=rotation,
        scale=scale,
    )


def cubeTest() -> None:
    for i in range(5):
        add_cube(location=[i * 5, 0, 0])
        newcube = bpy.context.object
        newcube.name = "Cube -" + str(i)

        newcube.rotation_euler = [0, 0, 0]
        newcube.keyframe_insert(data_path="rotation_euler", frame=1)

        newcube.rotation_euler = [0, 0, math.radians(45 + i * 15)]
        newcube.keyframe_insert(data_path="rotation_euler", frame=30)


def clearScene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def main():
    clearScene()

    # cubeTest()
    vC.makeTwoPointEdge(vC.Point(0, 0, 0), vC.Point(0, 2, 2))


main()
