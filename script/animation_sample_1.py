import bpy
import time

# blenderでアニメーションをさせるオブジェクトを一つ指定する
obj = bpy.context.scene.objects[0]

locations = (
    (0, 0, 2),
    (0, 3, 4),
    (0, 3, 8),
    (0, 13, 8),
    (5, 13, 8),
    (5, 23, 8),

)

i = 0
for location in locations:
    obj.location = location
    obj.keyframe_insert(data_path="location", frame=5.0*i)
    i += 1
