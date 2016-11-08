#Blender scripts

To run a script in Blander with a background mode (no UI):

/Applications/blender.app/Contents/MacOS/blender --background --python "script_name.py"


#Blender hotkeys

A - select/deselect all
B - select region
Shift + C - zoom selected
Alt + Shift + Q - four quadrant mode
Ctrl + Alt + Shift + C → Origin to 3D Cursor to update or change the object origin to the location of the 3D cursor.



move pivot points to center of objects
find position of 1 pivot point  (bpy.data.objects['Sphere1'].location)
find position of 2 pivot point (bpy.data.objects['Sphere2'].location)
find the mid point of these pivot points
move (or translate ) objects using coordinates of mid point 

1. moveto = bpy.data.objects['Sphere'].location * (-1) //find inverse vector to use in translation
2. bpy.ops.transform.translate(value=moveto)