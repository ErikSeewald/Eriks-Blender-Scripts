import bpy
from ebs_point import Point
from ebs_path import Path
import ebs_util

 
ebs_util.object_mode()
ebs_util.clear_scene()
    
path = Path((Point(0, 0, 0), Point(0, 1, 2), Point(1, 3, 4), Point(1,4,6), Point(.,5,6.3)))
path.add_volume()
path.add_arrow()
