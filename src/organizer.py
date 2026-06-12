#!/usr/bin/python3
from pathlib import Path 
from file_info_extractor import File
from directory_manipulator import find_mount_points


# A list of mount points
mount_points = find_mount_points(Path('.'))

print(f'This are mounted points:')

# Prints the directories that are mounted 
for point in mount_points:
    print(str(point) + '\n')

# Prints the directories in the mount points
for point in mount_points:
    print(f'Directories in {point}:')

    for dirr in point.iterdir():
        print(f"{str(dirr).split('/')[-1]}")
    
print("Which of this directories " + \
      "from the mount point do you want to organize?")

directory = input()
directory = Path('/media/lorescruzrene/recovery/recovered_files/recup_dir.1') 

# Iterating over the files in the directory
for d in directory.iterdir():
    if d.is_file():
      file = File(d)
      print(file.path.__str__())

      

    








