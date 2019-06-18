import bpy
file_loc = 'top.obj'
imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
obj_object = bpy.context.selected_objects[0] ####<--Fix

file_loc2 = 'bottom.obj'
imported_object2 = bpy.ops.import_scene.obj(filepath=file_loc2)
obj_object2 = bpy.context.selected_objects[1] ####<--Fix

bpy.ops.object.join()

print('Imported name: ', obj_object.name)
print('Imported name: ', obj_object2.name)

bpy.ops.export_scene.obj(filepath="merged.obj")