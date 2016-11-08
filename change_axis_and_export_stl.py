import bpy
import os

PROJECT_DIR = "/Users/vladimirsivanovs/Downloads/test/"


def clean_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)


def import_all_stl_files(directory):
    stl_files = [file for file in os.listdir(directory) if file.endswith(".stl")]
    for stl in stl_files:
        bpy.ops.import_mesh.stl(filepath=(directory + stl))


def export_each_selected_to_stl(directory):
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.export_mesh.stl(filepath=directory+"rotated_", check_existing=True, axis_forward='X', axis_up='Y',
                            filter_glob="*.stl", use_selection=True, global_scale=1.0, use_scene_unit=False,
                            ascii=False, use_mesh_modifiers=False, batch_mode='OBJECT')


def main():
    clean_scene()
    import_all_stl_files(PROJECT_DIR)
    export_each_selected_to_stl(PROJECT_DIR)


main()
