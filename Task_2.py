import os 
import pandas as pd 
from abc import ABC, abstractmethod
import requests 
import json
import csv
import requests

class DataSource(ABC):
    def __init__(self, schema):
        self.schema = schema

    @abstractmethod
    def load_data(self):
        pass
    abstractmethod
    def get_sample(self):
        pass

class FileSource(DataSource): #It Might Be CSV,JSOn,XML Files
    def __init__(self, file_path, schema):
        self.file_path = file_path
        super().__init__(schema)

    @property
    def DataSource_type(self):
        try:
            file_name, file_extension = os.path.splitext(self.file_path)
            return file_extension
        except:
            raise Exception("File extension check failed")


class SchemaMismatchError(Exception):
    raise ValueError ("The Schema is unmatched")

class FileFormatError(Exception):
    raise TypeError("The File Has A Wrong Format")

class CSVSource(FileSource):

    def __init__(self, file_path, schema):
        super().__init__(file_path, schema)
        self.df = self.load_data() #Here I intialize a Daatframe So I Don't Have to use pd.reaed_csv(self.file_path) in the Other class body/ methoed (except )

    def load_data(self):
        if self.DataSource_type == ".csv":
            print(f"Loading CSV file from: {self.file_path}")

            # Check if the number of columns matches the expected schema
            if len(pd.read_csv(self.file_path).columns) == int(self.schema):
                return pd.read_csv(self.file_path) #
            else:
                raise SchemaMismatchError
        else:
            raise FileFormatError 

    def Transform_Data(self):
        print(f"Transforming data from file: {self.file_path}")
        return f"This file has not specified any transformations. File path: {self.file_path}"

    def display(self):
        print(f"Displaying data from file: {self.file_path}")
        print(self.df)  # Print the head of the DataFrame

    def get_sample(self):
        return (self.df.head())


class JSONSource(FileSource):
    def __init__(self,file_path,schema):
        super().__init__(file_path,schema)
        self.df=self.load_data()


    def load_data(self,file_path):
        if self.DataSource_type== ".json" :
            print(f"Loading Json file from: {self.file_path}")
            if len(list(self.file_path.keys())) == int(self.schema):
                 return pd.read_json(self.file_path)
            else: 
                raise SchemaMismatchError 
        else:
            raise FileFormatError

            
class SQLSource(DataSource):
    def __init__(data_base_key,schema):
        super().__init__(file_path,schema) 

    

