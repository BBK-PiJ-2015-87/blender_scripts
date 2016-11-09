import os
import sys
sys.path.insert(0, "/path/to/mm-api/python")
sys.path.insert(0, "/path/to/mm-api/distrib/python_osx")
print(sys.path)


import mmapi
from mmRemote import *
import mm;

# assumption: we are running
examples_dir = "/dir/of/models/"
part_filename1 = os.path.join( examples_dir, "model1.stl" )
part_filename2 = os.path.join( examples_dir, "model2.stl" )

# initialize connection
remote = mmRemote()
remote.connect()

cmd = mmapi.StoredCommands()


new_obj1 = mm.append_objects_from_file(remote, part_filename1);
new_obj1 = mm.append_objects_from_file(remote, part_filename2);

#done!
remote.shutdown()
