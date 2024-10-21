import pandas as pd
import os

class DataHandler:
    def __init__(self, file, columns, skiprows=[], attributes=None):
        self.columns = columns
        self.skiprows = skiprows
        self.attributes = attributes or {}
        self.dataframe = None
        self.file_name = os.path.join(file['dirname'], file['file_name'])
        self.file_name_save = os.path.join(file['dirname'], file['file_name_save']) or 'data.parquete'

        self._read_from_csv()
        self._save_to_parquet()

    def _read_from_csv(self):
        try:
            self.dataframe = pd.read_csv(
                self.file_name, 
                sep=self.attributes.get('separator', ','), 
                header=self.attributes.get('header', None), 
                names=self.columns, 
                skiprows=self.skiprows
            )
            print("Data is successfully read.")
        except FileNotFoundError:
            print(f"File {self.file_name} is not found.")
        except pd.errors.ParserError as e:
            print(f"An error occurred while reading file: {e}")

    def _save_to_parquet(self):
        if self.dataframe is None:
            print("Dataframe is empty.")
            return

        try:
            self.dataframe.to_parquet(self.file_name_save, compression='snappy', index=False)
            print(f"Data is successfully saved to {self.file_name_save}.")
        except Exception as e:
            print(f"Failed to save data in Parquet: {e}")

    def get_dataframe(self):
        if self.dataframe is None:
            print("Dataframe is empty.")
            return
        
        return self.dataframe.head(10)
