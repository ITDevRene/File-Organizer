#!/usr/bin/python3
from pathlib import Path 
from file_info_extractor import File
from directory_manipulator import find_mount_points, Directory


# A list of mount points
mount_points = find_mount_points(Path('/media/lorescruzrene/recovery/recovered_files/recup_dir.1'))

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

# The program should be run from this directory
# to organize it
directory = Path.cwd() #The current directory

# Iterating over the files in the directory
for d in directory.iterdir():
    if d.is_file():
      file = File(d)

      if file.is_picture():
        dirr = Directory(directory)
        dirr.add_directories('Picture/' + \
                              str(file.year_modified) + '/' + \
                              str(file.get_month_modified(month_name = True)) + '/' + \
                              str(file.day_modified))
        file.move_to(dirr.path)
      

    








