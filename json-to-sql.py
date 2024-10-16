# source .venv/bin/activate
# deactivate

import pandas as pd
import sqlalchemy
import json

def convert(file):
    df = pd.DataFrame(json.load(file)['items'])
    conn = sqlalchemy.create_engine('mysql+pymysql://root:4542@localhost:3306/Seco_Pages')
    df.to_sql('Test_Table', con = conn, if_exists = "replace", dtype = sqlalchemy.types.JSON) 
    print(df)

if __name__ == '__main__':
    with open("output/git-pages.json", "r") as file:
        convert(file)