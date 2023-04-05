import bpy
from ebs_point import Point
import ebs_util

class Path:

    def __init__(self, points: tuple[Point]) -> None:

        ebs_util.object_mode()
        
        name = "Path " + str(points[0]) + " - " + str(points[len(points)-1]) 
        mesh = bpy.data.meshes.new(name)

        # CREATE VERTICES OUT OF POINTS
        verts: list[(float)] = list()
        for point in points:
            verts.append((-point.x, point.y, point.z))
        mesh.from_pydata(verts, [], [])
        
        self._path_from_verts(mesh, verts, name)

        
    def _path_from_verts(self, mesh, verts: list[(float)], name: str) -> None:
        
        mesh.vertices.add(len(verts))
        mesh.edges.add(len(verts) -1)
        for i, v in enumerate(verts):
            mesh.vertices[i].co = v
            
            if i < len(verts) -1:
               mesh.edges[i].vertices = [i, i+1] 

        # CREATE OBJECT WITH THE MESH
        self.obj = bpy.data.objects.new(name, mesh)
        bpy.context.scene.collection.objects.link(self.obj)
        self.obj.data = mesh


    # --MESH FUNCTIONS--

    def add_volume(self, thickness: float = 0.1) -> None:
        
        ebs_util.object_mode()
        
        # SET SELF.OBJ TO ACTIVE OBJECT
        bpy.context.view_layer.objects.active = self.obj
        
        # SKIN MODIFIER
        skin_modifier = self.obj.modifiers.new(name="Skin", type="SKIN")
        
        ebs_util.edit_mode()
        bpy.ops.transform.skin_resize(value=(thickness, thickness, thickness))
        ebs_util.object_mode()