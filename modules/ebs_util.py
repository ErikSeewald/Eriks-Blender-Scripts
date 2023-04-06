import bpy

def object_mode() -> None:
    if bpy.context.object is not None and bpy.context.object.mode != "OBJECT":
        bpy.ops.object.mode_set(mode="OBJECT")
        
def edit_mode() -> None:
    if bpy.context.object is not None and bpy.context.object.mode != "EDIT":
        bpy.ops.object.mode_set(mode="EDIT")
        
def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()
    
    for collection in bpy.data.collections[:]:
        collection.user_clear()
        bpy.data.collections.remove(collection, do_unlink=True)
