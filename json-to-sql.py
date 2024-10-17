# source .venv/bin/activate
# deactivate

import pandas as pd
import sqlalchemy
import json
import os, glob

path = os.getcwd() + '/output'

def convert(file):
    df = pd.DataFrame(json.load(file)['items'])
    conn = sqlalchemy.create_engine('mysql+pymysql://root:4542@localhost:3306/Seco_Pages')
    df.to_sql('Test_Table', con = conn, if_exists = "append", dtype = sqlalchemy.types.JSON) 
    print(df)

if __name__ == '__main__':
    for filename in glob.glob(os.path.join(path, '*.json')):
        with open(filename, "r") as file:
            convert(file)