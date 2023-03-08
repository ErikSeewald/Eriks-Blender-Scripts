import bpy
from e_point import Point


def makeTwoPointEdge(p1: Point, p2: Point) -> None:
    # Create a new mesh object
    mesh = bpy.data.meshes.new(str(p1) + " - " + str(p2))

    # Create two vertices at the specified coordinates
    verts: list[(float)] = [(-p1.x, p1.y, p1.z), (-p2.x, p2.y, p2.z)]
    mesh.from_pydata(verts, [], [])

    # Add the vertices to the mesh
    mesh.vertices.add(len(verts))
    for i, v in enumerate(verts):
        mesh.vertices[i].co = v

    # Create an edge between the two vertices
    mesh.edges.add(1)
    mesh.edges[0].vertices = [0, 1]

    # Create a new object and add the mesh to it
    obj = bpy.data.objects.new(str(p1) + " - " + str(p2), mesh)
    bpy.context.scene.collection.objects.link(obj)
    obj.data = mesh
