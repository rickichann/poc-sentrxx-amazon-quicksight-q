import pandas as pd
import os

folder_path = r'dataset'
file_list = []

# detect file on the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        file_list.append(filename)

def load_to_rds(table_name):
    df = pd.read(table_name)
    
    
