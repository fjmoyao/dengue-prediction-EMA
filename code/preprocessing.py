# Se cargan y transforman los datos 

import os
import pandas as pd
import numpy as np

wd = os.getcwd()
data_path = os.path.join(wd, "data")
raw = pd.read_csv(os.path.join(data_path, "raw","dengue_data_all_municipalities.csv" ))