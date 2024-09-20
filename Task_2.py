import os 
import pandas as pd 
from abc import ABC, abstractmethod
import requests 
import json
import csv
import requests
import time

 

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
    pass

class FileFormatError(Exception):
    pass

class APiConnError(Exception):
    """Custom exception for API connection errors."""
    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.status_code = status_code

class CSVSource(FileSource):

    def __init__(self, file_path, schema):
        super().__init__(file_path, schema)
        self.df = self.load_data() #Here I intialize a Daatframe So I Don't Have to use pd.reaed_csv(self.file_path) in the Other class body/ methoed (except )

    def load_data(self):
        if self.DataSource_type == ".csv":
            print(f"Loading CSV file from: {self.file_path}")
            df = pd.read_csv(self.file_path)
            if set (self.schema).issubsetset(df.columns) :
                return df
            else:
                raise SchemaMismatchError
        else:
            raise FileFormatError 

    def Transform_Data(self):
        print(f"Transforming data from file: {self.file_path}")
        return f"This file has not specified any transformations. File path: {self.file_path}"

    def display(self):
        print(f"Displaying data from file: {self.file_path}")
        print(self.df)  

    def get_sample(self):
        return (self.df.head())

class JSONSource(FileSource):
    def __init__(self,file_path,schema):
        super().__init__(file_path,schema)
        self.df=self.load_data()


    def load_data(self):
        if self.DataSource_type == ".json":
            print(f"Loading JSON file from: {self.file_path}")
            try:
                df = pd.read_json(self.file_path)
                if set(self.schema).issubset(df.columns):
                    return df
                else:
                    raise SchemaMismatchError(f"Schema mismatch: File columns {list(df.columns)} don't match the expected schema {self.schema}")
            except ValueError as e:  # pandas raises a ValueError for JSON loading issues
                raise ValueError(f"Error loading JSON with pandas: {e}")
        else:
            raise FileFormatError("The file is not in JSON format")
    def get_sample(self):
        return (self.df.head())
    

class APIDataSource(DataSource):
    def __init__(self, base_url, endpoint, headers=None, params=None):
        self.base_url = base_url
        self.endpoint = endpoint
        self.headers = headers or {}
        self.params = params or {}
        super().__init__(schema)
    

    def _build_url(self):
        """Helper method to construct the full API URL"""
        return f"{self.base_url}/{self.endpoint}"


    def request_data(self, retries=3, delay=2):
        try:
            self.response = requests.get(self._build_url(), headers=self.headers, params=self.params)

            if self.response.status_code == 200:
                return self.response.json()

            
            elif self.response.status_code == 404:
                raise  APiConnError(f"API request failed with status {response.status_code}", status_code=response.status_code)

            else:
                print(f"API request failed with status code: {self.response.status_code}")

                if retries > 0:

                    print(f"Retrying... ({retries} retries left)")
                    time.sleep(delay) 
                    return self.request_data(retries - 1, delay * 2)
                else:
                     raise APiConnError(f"API request failed with status {response.status_code}", status_code=response.status_code)
                
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request error: {str(e)}")

    def validate_response(self, json_data):
        """Ensure the response follows the expected schema"""
        missing_keys = [key for key in self.schema if key not in json_data]
        if missing_keys:
            raise SchemaMismatchError(f"Missing expected fields: {missing_keys}")
        print("Response validated successfully.")


schema = ["widget", "debug", "window", "image", "text"]
# Initialize the API datasource
api_data_source = APIDataSource(
    base_url="https://example.com/api",
    endpoint="data",
    schema=schema,
    headers={"Authorization": "Bearer YOUR_TOKEN"},
    params={"query": "example"}
)
data = api_data_source.request_data(retries=3, delay=2)

class SQLSource(DataSource):
    def __init__(self,data_base_key,schema):
        self.data_base_key=data_base_key
        super().__init__(file_path,schema) 





    

