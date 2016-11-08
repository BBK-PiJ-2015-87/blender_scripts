import bpy
import os


# get file names
stl_files = [file for file in os.listdir(PROJECT_DIR) if file.endswith(".stl")]

# import models
for model in stl_files:
    bpy.ops.import_mesh.stl(filepath=("/Users/vladimirsivanovs/Downloads/test/" + model))

# get model names
object_names = [obj.name for obj in bpy.data.objects]

# select all objects
bpy.ops.object.select_all(action='SELECT')

# rotate all selected objects by 90 degrees (vaule is in radians)
bpy.ops.transform.rotate(value=1.5708, axis=(0, 1, 0))

# save file
blender_filename="blender_file_name"
bpy.ops.save_as_mainfile("/Users/vladimirsivanovs/Downloads/test/" + blender_filename)

# export stl files
for obj in object_names:
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[obj].select = True
    bpy.ops.export_mesh.stl(filepath="/Users/vladimirsivanovs/Downloads/test/rotated_" + obj + ".stl", check_existing=True, ascii=False)


#rotate object
bpy.ops.transform.rotate(value=1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)


# get mesh object names
candidate_list = [item.name for item in bpy.data.objects if item.type == "MESH"]

# select objects from the list
for object_name in candidate_list:
    bpy.data.objects[object_name].select = True

# remove all selected objects
bpy.ops.object.delete()

# remove the meshes, they have no users anymore.
for item in bpy.data.meshes:
    bpy.data.meshes.remove(item)

# select / deslect all objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_all(action='SELECT')

# move object
bpy.context.object.location = (1, 2, 3)

# set origin to center of mass
bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')

#move selected objects
bpy.ops.transform.translate(value=(41.1424, -21.18, 16.678), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)


# set pivot point of transformations
bpy.context.space_data.pivot_point = 'MEDIAN_POINT'

# get cursor location
bpy.context.scene.cursor_location


#get selected objects
bpy.context.selected_objects

# all scene objects in a list
list(bpy.data.objects)


# all scene objects
bpy.data.objects['name_of_the_object'].location


manipulator