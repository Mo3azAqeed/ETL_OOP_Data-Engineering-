import os 
import pandas as pd 




class DataSource:
    def __init__ (self,file_path,schema):
        self.schema=schema
        self.file_path=file_path
    def load_data (self):
        pass
