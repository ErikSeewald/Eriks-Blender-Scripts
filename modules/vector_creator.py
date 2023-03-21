import bpy
from e_point import Point


def two_point_edge(p1: Point, p2: Point) -> None:
    
    name: str = str(p1) + " - " + str(p2)
    mesh = bpy.data.meshes.new(name)

    # CREATE TWO VERTICES AT AT P1 AND P2
    verts: list[(float)] = [(-p1.x, p1.y, p1.z), (-p2.x, p2.y, p2.z)]
    mesh.from_pydata(verts, [], [])

    _path_from_verts(mesh, verts, name)
    

def path_from_points(points: tuple[Point]) -> None:
    
    mesh = bpy.data.meshes.new("Edge")

    # CREATE VERTICES OUT OF POINTS
    verts: list[(float)] = list()
    for point in points:
        verts.append((-point.x, point.y, point.z))
    mesh.from_pydata(verts, [], [])
    
    _path_from_verts(mesh, verts, "Edge")
    
def _path_from_verts(mesh, verts: list[(float)], name: str) -> None:
    
    # ADD VERTICES TO MESH
    mesh.vertices.add(len(verts))
    for i, v in enumerate(verts):
        mesh.vertices[i].co = v
        
    # ADD EDGES TO MESH
    mesh.edges.add(len(verts) -1)
    for i, v in enumerate(verts):
        if i == len(verts) -1:
            break
        mesh.edges[i].vertices = [i, i+1]

    # CREATE OBJECT WITH THE MESH
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.scene.collection.objects.link(obj)
    obj.data = mesh