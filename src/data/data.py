import pandas as pd
import os

class DataHandler:
  def __init__(self, data_name=None, file_path=None, file_path_save=None, columns=[], skiprows=[], attributes=None):
    print(file_path)
    self.name = data_name
    self.file_path = file_path
    self.file_path_save = file_path_save
    self.columns = columns
    self.skiprows = skiprows 
    self.attributes = attributes or {}
    self.dataframe = None

    self._read_from_csv()
    self._save_to_parquet()

  def _read_from_csv(self):
    try:
      self.dataframe = pd.read_csv(
          self.file_path, 
          sep=self.attributes.get('separator', ','), 
          header=self.attributes.get('header', None), 
          names=self.columns, 
          skiprows=self.skiprows
      )
      print(f"Data {self.name} is successfully read.")
    except FileNotFoundError:
      print(f"File {self.file_path} is not found.")
    except pd.errors.ParserError as e:
      print(f"An error occurred while reading file: {e}")

  def _save_to_parquet(self):
    if self.dataframe is None:
      print("Dataframe is empty.")
      return

    try:
      self.dataframe.to_parquet(self.file_path_save, compression='snappy', index=False)
      print(f"Data {self.name} is successfully saved to {self.file_path_save}.")
    except Exception as e:
      print(f"Failed to save data in Parquet: {e}")

  def get_dataframe(self):
    if self.dataframe is None:
      print("Dataframe is empty.")
      return
    
    return self.dataframe.head(10)
