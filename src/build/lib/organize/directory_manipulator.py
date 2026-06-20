from pathlib import Path 
from file_info_extractor import InvalidPath, NotADirectory

#This is to look for mounted directories if any from 
# the current directory up 
def find_mount_points(path):
    if isinstance(path,Path):
      #Store a absolute path
      absolute_p = path.absolute()
      
      #Stores the directories names of the absolute path
      #in a list 
      dirs_list =absolute_p.__repr__().split('/')

      del(dirs_list[0]) # first element is not a directory

      # A string representing a path 
      # Directories names will be added to build a path 
      # This paths will be evaluated
      path_builder = ''

      # A list for Path objects
      mounted_dirs = []

      for dirr in dirs_list:
        #Appending a directory name
        path_builder = path_builder + '/'+ dirr
        

        # If the path built so far is mounted,
        # add it to a list of Path objects
        if Path(path_builder).is_mount():
            mounted_dirs.append(Path(path_builder))
        
      return mounted_dirs
    
    else:
      print(f'Nothing was done because {path} is not a Path object')


class Directory:
  
  def __init__(self,path :Path):

    if not isinstance(path, Path):
      raise InvalidPath(path)

    self.path = path
    
  def add_directories(self,directory :str):

    for d in directory.split('/'):
     if d:
      self.path = Path(str(self.get_path()) + '/' + d)

      try:
        self.path.mkdir()
      except FileExistsError:
        pass

  def remove_directory(self):
    self.get_path().rmdir()
    self.path = self.get_path().parent
      
  def get_path(self):
    return self.path


