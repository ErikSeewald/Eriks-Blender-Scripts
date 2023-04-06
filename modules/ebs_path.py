import bpy
from ebs_point import Point
import ebs_util
from mathutils import Vector

class Path:

    def __init__(self, points: tuple[Point]) -> None:

        self.points = points
        
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
        self.obj.data = mesh
        
        self.collection = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(self.collection)
        self.collection.objects.link(self.obj)


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
    
    
    def add_arrow(self, thickness: float = 0.1) -> None:
       
        # ADD TO LAST POINT IN PATH
        point = self.obj.data.vertices[len(self.points)-1]
        
        vec = Vector() # vector (second to last) -> (last point)
        for i in range(3):
            vec[i] = point.co[i] - self.obj.data.vertices[len(self.points) -2].co[i]

        # CONE OBJECT
        bpy.ops.mesh.primitive_cone_add(vertices=32, depth=2.0, location=point.co)
        cone = bpy.context.object
        cone.name = "Arrow"
        cone.scale = (thickness, thickness, thickness)
        
        # align Z axis of cone with vector (y axis as "up" for quat)
        cone.rotation_mode = "QUATERNION"
        cone.rotation_quaternion = vec.to_track_quat("Z", "Y")
        
        
        # ADD TO PATH COLLECTION
        self.collection.objects.link(cone)
        bpy.context.scene.collection.objects.unlink(cone) # remove from main collection