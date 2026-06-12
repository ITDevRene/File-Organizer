from pathlib import Path 
from datetime import date
from datetime import datetime
import time
from pathlib import PosixPath
import shutil
import sys

class NotAFile(BaseException):
    default_err_mess = "The path does not represent a file."

    def __init__(self,err_message=default_err_mess):
        super().__init__(err_message)

class NotADirectory(BaseException):
    def __init__(self,directory):
        super().__init__(f"{directory} is not a directory.")

class InvalidPath(BaseException):
    
    def __init__(self,path):
        super().__init__(f'{path} is not a valid path')

# Class that represents a file 
class File():

    # The Path object contains all the information
    # related to the file it locates 
    def __init__(self,
                 path,
                 name = None,
                 date_created = None,
                 date_modified = None,
                 date_accessed = None):

        
        if not isinstance(path,Path):
            raise InvalidPath(path)

        if not path.is_file():
            raise NotAFile()

        self.name :string = name 
        self._path :Path = path

        #Date objects
        self.date_created :date = date_created
        self.date_modified :date = date_modified
        self.date_accessed :date = date_accessed
    
    @property
    def path(self):

        if isinstance(self._path,Path):
          return self._path 
        else:
           return None

    #Converts seconds elapsed from the epoch into date
    def convert_to_date(self,seconds):
        return date.fromtimestamp(seconds)

    #Gives the most recent content modification date
    def get_date_modified(self):
        if self.path:
            return date.fromtimestamp(self.path.stat().st_mtime)
        else:
            return None

    # Returns the day the file was created.
    # If no day exits, it returns None
    # the day is returned as string 
    def get_day_created(self):

        day = None

        

        return day



    @path.setter
    def path(self,value):

        if not isinstance(value,Path):
            raise InvalidPath(value)

        self._path = value

    #Copies the file to a directory represented by a path 
    # directory is a Path object that 
    def move_to(self,directory :Path):

        #directory must be a path.
        # If not an exception is raised.    
        if not isinstance(directory,Path):
          raise InvalidPath(directory)

        #An exception is raised if the path does not
        # represents a directory
        if not directory.is_dir():
          raise NotADirectory(directory)
         
         
        self.path = Path(shutil.move(self.path,directory))

    # If the file is a picture, returns true 
    # otherwise it return false
    # since there are alot of formats it might be
    # good idea to provide a file with the supported picture formats
    def is_picture(self):
       
       f = open('./data/input/picture_format.txt','rb')

       if self.path.suffix in str(f.read()):
         
         f.close()
         return True

       
       

 #_________________       
path_string = '/media/lorescruzrene/recovery/recovered_files/recup_dir.1/t0176896.jpg'

#Create a path
dir_path = Path(path_string)

file = File(Path(path_string))

print(file.get_date_modified())
print(file.is_picture())





