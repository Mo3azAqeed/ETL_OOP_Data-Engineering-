import pandas as pd
from datetime import datetime

class MyDataFrame(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_csv(self, *args, **kwargs):
        temp = self.copy()
        temp['stamp'] = self.stamp
        temp.to_csv(*args, **kwargs)

    @classmethod
    def read_csv(cls, *args, **kwargs):
        """
        Class method to read a CSV file into an instance of MyDataFrame.
        """
        # Read the CSV into a regular DataFrame
        df = pd.read_csv(*args, **kwargs)
        # Convert it into an instance of MyDataFrame
        return cls(df)

# Now you can use read_csv to create an instance of MyDataFrame
test = MyDataFrame.read_csv('test.csv')
print(test)
test.to_csv('otput_3.csv')