import os
import pandas as pd

class DataFile:
    def __init__(self,type,file):
        self.file=file
        self.type=type
    def read(self):
        try:
            f=open(self.file,"r")
            return f.read()
        except:
            raise Exception ("The File is Unreadable")
    def validate(self,type):
        file_name,file_extension=os.path.splitext(self.file)
        if str((file_extension).lower()) == type.lower():
            print ("Everything' Looks Good")
        else:
           raise Exception ("Ummatched Type")
        return True

class CSVFile(DataFile):
    def __init__(self,columns=[]):
        self.columns =columns
        super().__init__(type,file)
    def validate(self):
        file_name,file_extension=os.path.splitext(self.file)
        if str((file_extension).lower()) == ".csv":
            print ("Everything' Looks Good")
            df = pd.read_csv(self.file)
            list_of_column_names = list(df.columns)
            for col in self.columns:
                if col in list_of_column_names :
                    pass
                else:
                    raise Exception (f" {col} isn't a column in the {self.file} ")
            return list_of_column_names
        