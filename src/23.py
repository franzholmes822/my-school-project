import numpy as np

class DataProcessor:
    def __init__(self):
        self.data = []

    def add_data(self, data):
        self.data.append(data)

    def get_data(self):
        return self.data

# Example usage
data_processor = DataProcessor()
data_processor.add_data([[1, 2], [3, 4]])
print("The processed data is:", data_processor.get_data())
