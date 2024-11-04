import pandas as pd

class DataFrame_:
  def __init__(self, data, columns):
    self.df = pd.DataFrame(data, columns=columns)

  @classmethod
  def from_parquete(cls, file_path, columns):
    data = pd.read_parquet(file_path)
    return cls(data, columns)