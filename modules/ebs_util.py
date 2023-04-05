import bpy

def object_mode() -> None:
    if bpy.context.object is not None and bpy.context.object.mode != "OBJECT":
        bpy.ops.object.mode_set(mode="OBJECT")
        
def edit_mode() -> None:
    if bpy.context.object is not None and bpy.context.object.mode != "EDIT":
        bpy.ops.object.mode_set(mode="EDIT")