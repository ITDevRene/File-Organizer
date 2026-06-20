from pathlib import Path 
from datetime import date
from datetime import datetime
import time
from pathlib import PosixPath
import shutil
import sys

class NotADirectory(BaseException):
    def __init__(self,directory):
        super().__init__(f"{directory} is not a directory.")

class NotAFile(BaseException):
    default_err_mess = "The path does not represent a file."

    def __init__(self,err_message=default_err_mess):
        super().__init__(err_message)


class InvalidPath(BaseException):
    
    def __init__(self,path :Path):
        super().__init__(f'{path} is not a valid path')
        print('Issued from InvalidPath')

class FileDoesNotExist(BaseException):

    def __init__(self, path : Path):
        super().__init__(f'{path} File does not exist.')

# Class that represents a file 
class File():

    # The Path object contains all the information
    # related to the file it locates 
    def __init__(self,path :Path):

        if not isinstance(path,Path):
            raise InvalidPath(path)

        if not path.exists():
            raise FileDoesNotExist(path)

        if not path.is_file():
            raise NotAFile()

        self.name :string = path.name 
        self._path :Path = path

        #Date objects
        self.year_modified = self.get_date_modified().year
        self.month_modified = self.get_date_modified().month
        self.day_modified = self.get_date_modified().day

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
    def get_month_modified(self,month_name = False):
       m_names = ['January','February','March','April','May','June', \
        'July','August','September','Octorber','November', 'December']

       if not month_name:
         return self.get_date_modified().month
       else:
         return m_names[int(self.month_modified) - 1]    

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
    # since there are alot of formats it might be a
    # good idea to provide a file with the supported picture formats
    # this file could be encrypted to prevent others from reading it
    def is_picture(self):
       
       # Path object representing this file's path
       this_file_path = Path(__file__)

       # Path string of a parent directory
       str_fpath = str(this_file_path.parents[1]) 
    
       # Path string of the data file for picture formats
       data_file_path = str_fpath + '/data/input/picture_format.txt'

       # File containing picture formats
       f = open(data_file_path,'rb')
       
       # The extension of the file
       # self.path is a getter function created with @property
       suffix = self.path.suffix

       if suffix in str(f.read()) and suffix != '':
          
         f.close()
         return True
       else: 
         f.close()
         return None

    def is_video(self):

        #This is the file path for this file 
        this_file_path = Path(__file__)
        
        # the path string for one of the parents of this file
        # this will be used for finding the data files 
        str_par_path = str(this_file_path.parents[1])

        # Opening the file were the formats are stored
        f = open(str_par_path + '/data/input/video_formats.txt','rb')
        
        # The file type. This is the extension of the file
        # self.path is a property function
        suffix = self.path.suffix

        if suffix in str(f.read()) and suffix != '':
            
            f.close()
            return True
        else:
            f.close()
            return None



        

    

