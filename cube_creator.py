import bpy


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
