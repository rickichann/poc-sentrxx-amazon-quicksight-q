import pandas as pd
import os
from sqlalchemy import create_engine


# folder name
folder_path = r'dataset'
file_list = []

# detect file on the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        file_list.append(filename)

def load_to_rds(table_name):
    df = pd.read_csv(f'dataset/{table_name}')
    us, ps, host, port, db = 'admin', 'admin!223344', 'localhost', 3306, 'poc_sentral_q'
    engine = create_engine(f'mysql+pymysql://{us}:{ps}@{host}:{port}/{db}')
    table_name = table_name.split(".")[0]
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print(table_name,"200 Inserted")
    
for tbl in file_list:
    load_to_rds(tbl)


