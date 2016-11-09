import bpy
import os

PROJECT_DIR="/Users/vladimirsivanovs/Downloads/test/"

def clean_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def main():

    clean_scene()

    # get file names
    stl_files = [file for file in os.listdir(PROJECT_DIR) if file.endswith(".stl")]

    # import models
    for model in stl_files:
        bpy.ops.import_mesh.stl(filepath=("/Users/vladimirsivanovs/Downloads/test/" + model))

    # get model names
    object_names = [obj.name for obj in bpy.data.objects]

    # select all objects
    bpy.ops.object.select_all(action='SELECT')

    # rotate all objects
    bpy.ops.transform.rotate(value=1.5708, axis=(0, 1, 0))

    # export stl files
    for obj in object_names:
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects[obj].select = True
        bpy.ops.export_mesh.stl(filepath="/Users/vladimirsivanovs/Downloads/test/rotated_" + obj + ".stl", check_existing=True, ascii=False)

main()

