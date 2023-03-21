import bpy
from e_point import Point


def two_point_edge(p1: Point, p2: Point) -> None:
    
    name: str = "Edge " +  str(p1) + " - " + str(p2)
    mesh = bpy.data.meshes.new(name)

    # CREATE TWO VERTICES AT AT P1 AND P2
    verts: list[(float)] = [(-p1.x, p1.y, p1.z), (-p2.x, p2.y, p2.z)]
    mesh.from_pydata(verts, [], [])

    _path_from_verts(mesh, verts, name)
    

def path_from_points(points: tuple[Point]) -> None:
    
    name = "Path " + str(points[0]) + " - " + str(points[len(points)-1]) 
    mesh = bpy.data.meshes.new(name)

    # CREATE VERTICES OUT OF POINTS
    verts: list[(float)] = list()
    for point in points:
        verts.append((-point.x, point.y, point.z))
    mesh.from_pydata(verts, [], [])
    
    _path_from_verts(mesh, verts, name)
    
def _path_from_verts(mesh, verts: list[(float)], name: str) -> None:
    
    mesh.vertices.add(len(verts))
    mesh.edges.add(len(verts) -1)
    for i, v in enumerate(verts):
        mesh.vertices[i].co = v
        
        if i < len(verts) -1:
           mesh.edges[i].vertices = [i, i+1] 

    # CREATE OBJECT WITH THE MESH
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.scene.collection.objects.link(obj)
    obj.data = mesh